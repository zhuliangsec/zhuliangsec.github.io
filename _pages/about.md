---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

[Kaixuan Li](https://kaixuanli-ecnu.github.io/) (The "X" in "Kaixuan" is pronounced like the "sh" in "shear") is now a final-year Ph.D. candidate in the Software Engineering Institute at [East China Normal University (ECNU)](https://www.ecnu.edu.cn/), under the supervision of [Prof. Yixiang Chen](https://faculty.ecnu.edu.cn/_s43/cyx/main.psp). Before that, I received my B.S. degree in Software Engineering Institute from ECNU in 2020. 
I am also a visiting Ph.D. student and research assistant at [Nanyang Technological University](https://www.ntu.edu.sg/) under the supervision of [Prof. Yang Liu](https://personal.ntu.edu.sg/yangliu/) during 2022-2025.

My research focuses on Trustworthy Software, particularly in areas such as **Open Source Security** and **Smart Contract Security** by exploring advanced program analysis and applying large language models (LLMs) to enhance software security. 

💬 kaixuanli AT stu.ecnu.edu.cn


# 🔥 News
* October 2024: Our paper "A Comprehensive Study on Static Application Security Testing (SAST) Tools for Android" was accepted by TSE, congrats to Jingyun!
* October 2024: I am invited as a PC member @MSR4P&S 2025, co-located with SANAR 2025. Welcome to submit your papers!
* September 2024: I won the National Scholarship of Doctoral Students (China), thanks for the recognition and support from the faculty and students@SEI, ECNU!
* July 2024: I am selected as a Shadow PC member within ICSE 2025, welcome to submit your papers!
* July 2024: Our paper "PatchFinder: A Two-Phase Approach to Security Patch Tracing for Disclosed Vulnerabilities in Open-Source Software" was accepted by ISSTA 2024!
* June 2024: Our paper "Static Application Security Testing (SAST) Tools for Smart Contracts: How Far Are We?" has won an [ACM SIGSOFT Distinguished Paper award](https://2024.esec-fse.org/info/awards)! 🏆
* May 2024: Our paper "Using My Functions Should Follow My Checks: Understanding and Detecting Insecure OpenZeppelin Code in Smart Contracts" was accepted by Usenix Security 2024.
* April 2024: Our paper "Static Application Security Testing (SAST) Tools for Smart Contracts: How Far Are We?" was accepted by FSE 2024.



# 📝 Selected Publications 
^ indicates equal contribution.
- *(TSE 2024, CCF-A)* Jingyun Zhu^, **Kaixuan Li**^, Sen Chen, Lingling Fan, Junjie Wang, and Xiaofei Xie. 2024. A Comprehensive Study on Static Application Security Testing (SAST) Tools for Android. IEEE Transactions on Software Engineering. [Preprint: http://arxiv.org/abs/2410.20740](http://arxiv.org/abs/2410.20740).
- *(ISSTA 2024, CCF-A)* **Kaixuan Li**, Jian Zhang, Sen Chen, Han Liu, Yang Liu, and Yixiang Chen. "PatchFinder: A Two-Phase Approach to Security Patch Tracing for Disclosed Vulnerabilities in Open-Source Software." In Proceedings of the 33rd ACM SIGSOFT International Symposium on Software Testing and Analysis, pp. 590-602. 2024. [https://doi.org/10.1145/3650212.3680305](https://doi.org/10.1145/3650212.3680305).
- *(CAAI)* **Kaixuan Li** and Yixiang Chen. Hybrid Artificial Intelligence: Logic Reasoning for Large Language Models (混成式人工智能：面向大语言模型的逻辑推理), 人工智能学会通讯, 2024 14(7): 03-07 (In Chinese). [https://book.yunzhan365.com/poui/tcew/mobile/index.html](https://book.yunzhan365.com/poui/tcew/mobile/index.html).
- *(Preprint)* Han Liu, Jian Zhang, Cen Zhang, Xiaohan Zhang, **Kaixuan Li**, Sen Chen, Shang-Wei Lin, Yixiang Chen, Xinhua Li, and Yang Liu. 2024. "FineWAVE: Fine-Grained Warning Verification of Bugs for Automated Static Analysis Tools." arXiv preprint arXiv:2403.16032 (2024), [Preprint](https://arxiv.org/pdf/2403.16032.pdf)
- *(Preprint)* Lyueye Zhang^, **Kaixuan Li**^, Kairan Sun, Daoyuan Wu, Ye Liu, Haoye Tian, and Yang Liu. 2024. "Acfix: Guiding LLMs with mined common RBAC practices for context-aware repair of access control vulnerabilities in smart contracts." arXiv preprint arXiv:2403.06838 (2024), [Preprint](https://arxiv.org/pdf/2403.06838.pdf)
- *(Usenix Security 2024, CCF-A)* Han Liu, Daoyuan Wu, Yuqiang Sun, Haijun Wang, **Kaixuan Li**, Yang Liu, and Yixiang Chen. 2024. "Using My Functions Should Follow My Checks: Understanding and Detecting Insecure OpenZeppelin Code in Smart Contracts". In Proceedings of the 2024 USENIX Security Symposium (USENIX Security'24).
- *(FSE 2024, CCF-A)* **Kaixuan Li**, Yue Xue, Sen Chen, Han Liu, Kairan Sun, Ming Hu, Haijun Wang, Yang Liu, and Yixiang Chen. 2024. Static Application Security Testing (SAST) Tools for Smart Contracts: How Far Are We?. Proc. ACM Softw. Eng. 1, FSE, Article 65 (July 2024), 24 pages. [https://doi.org/10.1145/3660772](https://doi.org/10.1145/3660772). [<font color ="red"> ACM SIGSOFT Distinguished Paper award </font>](https://2024.esec-fse.org/info/awards) 🏆
- *(ESEC/FSE 2023, CCF-A)* Kairan Sun, Zhengzi Xu, Chengwei Liu, **Kaixuan Li**, and Yang Liu. 2023. "Demystifying the Composition and Code Reuse in Solidity Smart Contracts." United States, In Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE 2023); December 3-9 2023, Pages:796-807, [https://doi.org/10.1145/3611643.3616270](https://doi.org/10.1145/3611643.3616270).
- *(ESEC/FSE 2023, CCF-A)* **Kaixuan Li**^, Sen Chen^, Lingling Fan, Ruitao Feng, Han Liu, Chengwei Liu, Yang Liu, and Yixiang Chen. 2023. "Comparison and Evaluation on Static Application Security Testing (SAST) Tools for Java". United States, In Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering (ESEC/FSE 2023); 3 December-9 December 2023, Pages:921–933, [https://doi.org/10.1145/3611643.3616262](https://doi.org/10.1145/3611643.3616262). 
- *(ISSTA 2023, CCF-A)* Han Liu, Sen Chen, Ruitao Feng, Chengwei Liu, **Kaixuan Li**, Zhengzi Xu, Liming Nie, Yang Liu, and Yixiang Chen. 2023. "A Comprehensive Study on Quality Assurance Tools for Java", United States, In Proceedings of the 32nd International Symposium on Software Testing and Analysis (ISSTA); 17 July-21 July 2023, Pages:285–297, [https://doi.org/10.1145/3597926.3598056](https://doi.org/10.1145/3597926.3598056).
- *(JoS, CCF-A in Chinese)* Han Liu, **Kaixuan Li**, and Yixiang Chen. "Survey on Trustworthiness Measurement for Artificial Intelligence Systems". Ruan Jian Xue Bao/Journal of Software, 2023, 34(8): 3774–3792 (in Chinese), [http://www.jos.org.cn/1000-9825/6592.htm](http://www.jos.org.cn/1000-9825/6592.htm).

# 📖 Educations
- *2020.09 - 2025.06 (expected)*, Ph.D. student/candidate, Software Engineering Institute, East China Normal University.
- *2023.09 - present*, Research assistant, [Continental-NTU Corporate Lab](https://www.ntu.edu.sg/continental-ntu), Nanyang Technological University.
- *2022.09 - 2023.09*, Visiting Ph.D. student, School of Computer Science and Engineering, Nanyang Technological University.
- *2016.09 - 2020.06*, Bachelor of Software Engineering, Software Engineering Institute, East China Normal University.


# 📚 Academic Services

## Reviewer/Program Committee Member:
* [Transactions on Software Engineering and Methodology](https://dl.acm.org/journal/tosem)
* [Cybersecurity](https://cybersecurity.springeropen.com/)
* [MSR4P&S 2025](https://msr4ps.github.io/)

## Shadow/Junior Program Committee Member:
* [ICSE 2025](https://conf.researchr.org/committee/icse-2025/icse-2025-shadow-research-track-program-committee-shadow-pc)
* [MSR 2024](https://2024.msrconf.org/committee/msr-2024-junior-pc-technical-papers---junior-program-committee)

## Co-reviewer:
* [USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25)
* [ASE 2024](https://conf.researchr.org/track/ase-2024/ase-2024-research)
* [IEEE S&P 2025](https://www.ieee-security.org/TC/SP2025/cfpapers.html)
* [CCS 2024](https://www.sigsac.org/ccs/CCS2024/call-for/call-for-papers.html)
* [ISSTA 2024](https://2024.issta.org/track/issta-2024-papers)
* [ICSE 2024](https://conf.researchr.org/track/icse-2024/icse-2024-research-track?)
* [WWW 2024](https://www2024.thewebconf.org/)
* [ASE 2023](https://conf.researchr.org/home/ase-2023)
* [ESEC/FSE 2023](https://2023.esec-fse.org/)
* [ASE 2022](https://conf.researchr.org/home/ase-2022)
* [Frontiers of Computer Science](https://www.springer.com/journal/11704)
* [ESTC 2022](https://estc2022.github.io/index.html)
* [Journal of Software](https://www.jos.org.cn/jos/home)


# 🎖 Honors and Awards
* National Scholarship, Ministry of Education, China, 2024.
* ACM SIGSOFT Distinguished Paper award, FSE 2024, 2024.
* "Student Technological Excellence" Award (学生科技英才) @SEI, East China Normal University, 2024.
* Visiting Ph.D. Student Scholarship of China Scholarship Council, 2022-2023.
* Merit Student of East China Normal University, 2022-2023.
* Merit Student of East China Normal University, 2021-2022.
* Merit Student of East China Normal University, 2020-2021.
* "HUAWEI CUP" The 18th China Post-Graduate Mathematical Contest in Modelling 3rd Prize, 2021.
* "HUAWEI CUP" The 17th China Post-Graduate Mathematical Contest in Modelling 3rd Prize, 2020.
* Outstanding Graduate of Shanghai, 2020.



<style>
    #clustrmaps-container {
        /* transform: scale(0.5); */
        transform-origin: top left;
        width: 200px; /* Adjust this value based on your desired width */
        height: 150px; /* Adjust this value based on your desired height */
        overflow: hidden; /* This will hide any overflow content */
        
        /* Centering the container horizontally */
        margin-left: auto;
        margin-right: auto;
        display: block;
    }
</style>

<div id="clustrmaps-container">
    <script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=xK73SrbAAKlYLUs8vmvb2TVShV7x81eqT_FAU02nk90&cl=ffffff&w=a"></script>
</div>
