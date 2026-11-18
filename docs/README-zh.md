
<h1 align="center">
AcadHomepage
</h1>

<div align="center">

[![](https://img.shields.io/github/stars/RayeRen/acad-homepage.github.io)](https://github.com/RayeRen/acad-homepage.github.io)
[![](https://img.shields.io/github/forks/RayeRen/acad-homepage.github.io)](https://github.com/RayeRen/acad-homepage.github.io)
[![](https://img.shields.io/github/issues/RayeRen/acad-homepage.github.io)](https://github.com/RayeRen/acad-homepage.github.io)
[![](https://img.shields.io/github/license/RayeRen/acad-homepage.github.io)](https://github.com/RayeRen/acad-homepage.github.io/blob/main/LICENSE)  | [English README](../README.md) 

</div>

<p align="center">一个现代、响应式的个人学术主页</p>


<p align="center">
    <br>
    <img src="./screenshot.png" width="100%"/>
    <br>
</p>

一些例子：
- [样例页面](https://rayeren.github.io/acad-homepage.github.io/)
- [作者的个人主页](https://rayeren.github.io/)

## 主要特点
- **自动更新谷歌学术引用**: 借助谷歌学术爬虫和github action功能，本仓库可以自动更新作者的引用数和论文引用数。
- **支持谷歌Analytics**: 你可以通过简单的配置来实现使用谷歌Analytics跟踪网页的流量。
- **响应式的**: 此主页会针对不同的屏幕尺寸自动调整布局。
- **美观而简约**: 此主页美观而简约，适合个人学术主页的搭建。
- **搜索引擎优化**: 搜索引擎优化 (SEO) 帮助搜索引擎轻松找到您在主页上发布的信息，然后将其与类似网站进行排名，并获得排名优势。

## 快速开始

1. Fork本仓库到`USERNAME/USERNAME.github.io`，其中`USERNAME`是你的github用户名。
1. 配置谷歌学术引用爬虫：
    1. 在你的谷歌学术引用页面的url里找到你的谷歌学术ID：例如，在url https://scholar.google.com/citations?user=SCHOLAR_ID 中，`SCHOLAR_ID`部分即为你的谷歌学术ID。
    1. 在[_config.yml](../_config.yml)中把`google_scholar_id`填为该ID，并把`author.googlescholar`填为你的谷歌学术主页完整URL。workflow会直接读取配置文件；也可以在`Settings -> Secrets -> Actions`里用`GOOGLE_SCHOLAR_ID`覆盖。
    1. 在 GitHub 仓库的 `Actions` 页面启用 workflows。该 action 会把谷歌学术引用统计数据 `gs_data.json` 写入本仓库的 `google-scholar-stats` 分支；每次推送 main 分支都会触发，此外每天 08:00 UTC 定时运行一次，也可在 Actions 里手动 Run workflow。
1. 使用 [favicon-generator](https://redketchup.io/favicon-generator)生成favicon（网页icon文件），并下载所有文件到`REPO/images`。
1. 修改主页配置文件[_config.yml](../_config.yml):
    1. `title`: 主页标题
    1. `description`: 主页的描述
    1. `repository`: USER_NAME/REPO_NAME  
    1. `google_analytics_id` (可选的): 谷歌Analytics ID
    1. SEO相关的键值 (可选的): 从搜索引擎的控制台里获得对应的ID (例如：Google, Bing and Baidu)，然后粘贴到这里。
    1. `author`: 主页作者信息，包括其他网页、Email、所在城市、大学等。
    1. `google_scholar_stats_use_cdn`: 使用CDN读取存储于`https://raw.githubusercontent.com/`的google scholar引用统计数据，防止中国大陆地区被墙无法访问的情况。但是CDN有缓存，因此`google_scholar_stats_use_cdn : true`时，引用数据更新会有延迟。
    1. 更多的配置信息在注释中有详细描述。
1. 将你的主页内容添加到 [_pages/about.md](../_pages/about.md).
    1. **显示单篇论文的引用数**：在论文条目末尾加一个 `<span>`，页面加载时会自动填入引用数：
        ```html
        1. 作者, "[论文标题](链接)," 期刊, 年份. <span class='show_paper_citations' data='hbWYZ4MAAAAJ:zYLM7Y9cAGgC'></span>
        ```
        `data` 填 Google Scholar 的论文 ID，格式是「作者ID:论文ID」。获取方法：在 Scholar 主页点开论文标题，地址栏 `citation_for_view=` 后面那一串就是；也可以直接查 `google-scholar-stats` 分支 `gs_data.json` 里 `publications` 的键名。
    1. 不想查 ID 也可以直接写论文标题，脚本会拿它去匹配 `gs_data.json` 里的 `bib.title`（忽略大小写、空格和标点）：
        ```html
        <span class='show_paper_citations' data-title='Fast revocable attribute-based encryption with data integrity for Internet of Things'></span>
        ```
    1. 引用数来自 GitHub Action 生成的 `gs_data.json`。Action 成功跑过一次之前数据文件是 404，此时引用数位置一律留空且不报错；之后每天自动更新，无需改动主页。
1. 你的主页将会被部署到`https://USERNAME.github.io`.

## 本地调试

1. 使用`git clone`将本项目克隆到本地。
1. 安装Jekyll的构建环境，包括`Ruby`、`RubyGems`、`GCC`和`Make`。可参考[该教程](https://jekyllrb.com/docs/installation/#requirements)。
1. 运行 `bash run_server.sh` 来启动Jekyll实时重载服务器。
1. 在浏览器里打开 [http://127.0.0.1:4000](http://127.0.0.1:4000)。如果你修改了网页的源码，服务器会自动重新编译并刷新页面。
1. 当你修改完毕你的页面以后, 使用`git`命令，`commit`你的改动并`push`到你的github仓库中。

# Acknowledges

- AcadHomepage incorporates Font Awesome, which is distributed under the terms of the SIL OFL 1.1 and MIT License.
- AcadHomepage is influenced by the github repo [mmistakes/minimal-mistakes](https://github.com/mmistakes/minimal-mistakes), which is distributed under the MIT License.
- AcadHomepage is influenced by the github repo [academicpages/academicpages.github.io](https://github.com/academicpages/academicpages.github.io), which is distributed under the MIT License.