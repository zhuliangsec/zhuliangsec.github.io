"""抓取 Google Scholar 引用统计，输出 gs_data.json / gs_data_shieldsio.json。

之前用 scholarly 库，它会对每篇论文各发一次请求并自带重试；在 GitHub Actions
的共享 IP 上极易被 Scholar 反爬挂起（Job 一直卡在 Run 步骤）。这里改成只请求
一次公开列表页、用 HTML 解析出全部字段，速度快且不会无限重试。
仅使用 Python 标准库，无需 pip install。
"""

import html
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
HOSTS = (
    "scholar.google.com",
    "scholar.google.com.hk",
    "scholar.google.co.uk",
)


def clean(text):
    return html.unescape(re.sub(r"<[^>]+>", "", text)).strip()


def fetch(scholar_id):
    errors = []
    for host in HOSTS:
        url = (
            "https://%s/citations?hl=en&user=%s&view_op=list_works"
            "&sortby=pubdate&pagesize=100" % (host, scholar_id)
        )
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": USER_AGENT, "Accept-Language": "en-US,en;q=0.9"}
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                body = resp.read().decode("utf-8", "replace")
            if 'class="gsc_a_tr"' in body or 'id="gsc_rsb_st"' in body:
                return body
            errors.append("%s: 页面缺少论文列表（可能是验证码/反爬页）" % host)
        except Exception as exc:  # noqa: BLE001 - 逐个域名记录后统一报错
            errors.append("%s: %s %s" % (host, type(exc).__name__, str(exc)[:120]))
    raise RuntimeError("所有 Scholar 域名均不可用:\n  " + "\n  ".join(errors))


def parse(body, scholar_id):
    name_match = re.search(r'id="gsc_prf_in"[^>]*>(.*?)</div>', body, re.S)
    name = clean(name_match.group(1)) if name_match else scholar_id

    # 侧栏统计表第一行 "Citations" 的 All 列即总引用数
    citedby = None
    table = re.search(r'<table id="gsc_rsb_st".*?</table>', body, re.S)
    if table:
        match = re.search(r"Citations</td>\s*<td[^>]*>\s*(\d+)", table.group(0), re.S)
        if match:
            citedby = int(match.group(1))

    publications = {}
    for row in re.findall(r'<tr class="gsc_a_tr".*?</tr>', body, re.S):
        title_match = re.search(r'class="gsc_a_at"[^>]*>(.*?)</a>', row, re.S)
        pid_match = re.search(r"citation_for_view=([A-Za-z0-9_\-:]+)", row)
        if not (title_match and pid_match):
            continue
        paper_id = pid_match.group(1)
        grays = [
            clean(g)
            for g in re.findall(r'class="gs_gray"[^>]*>(.*?)</div>', row, re.S)
        ]
        citations = re.search(r'class="gsc_a_ac[^"]*"[^>]*>(\d*)</a>', row)
        year = re.search(r'class="gsc_a_h gsc_a_hc gs_ibl">(\d*)</span>', row)
        publications[paper_id] = {
            "author_pub_id": paper_id,
            "num_citations": int(citations.group(1)) if citations and citations.group(1) else 0,
            "bib": {
                "title": clean(title_match.group(1)),
                "author": grays[0] if grays else "",
                "venue": grays[1] if len(grays) > 1 else "",
                "pub_year": year.group(1) if year else "",
            },
        }

    if not publications:
        raise RuntimeError("未解析到任何论文，可能是验证码页面或 Scholar 改版")
    if citedby is None:  # 表格缺失时用逐篇求和兜底
        citedby = sum(p["num_citations"] for p in publications.values())

    return {
        "name": name,
        "citedby": citedby,
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "publications": publications,
    }


def main():
    scholar_id = os.environ.get("GOOGLE_SCHOLAR_ID", "").strip()
    if not scholar_id:
        print("::error::GOOGLE_SCHOLAR_ID 为空，跳过", file=sys.stderr)
        return 1

    try:
        data = parse(fetch(scholar_id), scholar_id)
    except Exception as exc:  # noqa: BLE001
        print("::error::抓取 Google Scholar 失败: %s" % exc, file=sys.stderr)
        return 1

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(data["citedby"]),
    }
    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False)
    with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as fh:
        json.dump(shieldio_data, fh, ensure_ascii=False)

    print("%s | citedby=%s | publications=%d" % (data["name"], data["citedby"], len(data["publications"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
