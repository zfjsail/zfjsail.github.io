---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<!-- ## About Me -->

I am a postdoctoral researcher in the [Department of Computer Science and Technology](https://www.cs.tsinghua.edu.cn/csen/), [Tsinghua Univerisity](https://www.tsinghua.edu.cn/en/), collaborated with Prof. [Jie Tang](http://keg.cs.tsinghua.edu.cn/jietang/). Prior to that, I received my Ph.D. degree from [Tsinghua Univerisity](https://www.tsinghua.edu.cn/en/), and my bachelor degree from [Nanjing Univerisity](https://www.nju.edu.cn/).

My research interests generally include data mining, knowledge graph, and large language models, with an emphasis on developing **scalable** and **lightweight** data mining algorithms
primarily on academic knowledge graph to accelerate academic research and scientific innovation.
Recently, I am also working on LLM inference acceleration.  

I am looking for <u>self-motivated</u> students to work with me on the area of speculative decoding and LLM agent. If interested, please drop me a message by email.  

<span style="font-size: 75%; color:red">What's New</span>
========
* [AMiner Rumination](https://aminer.org/open/research), an academic deep research system, has launched. Feel free to try it out and ask academic questions!
* [OAG-Challenge](https://www.biendata.xyz/kdd2024/) at KDD Cup 2024 has set up long-term leaderboard.
Welcome to join the competition and address the key challenges in academic graph mining. 
* We maintain a paper sharing channel about large foundation models at <span style="color:red">!!![Xiaohongshu](xxx)</span> and [Telegram](https://t.me/CSPaperSharing). Feel free to subscribe!


## Projects 


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">LLM Agent for Academic Data</div><img src='images/aminer-dr.png' alt="sym" width="100%">


</div>
</div>
<div class='paper-box-text' markdown="1">

Large Language Model Agents make academic applications easier to build and more intelligent. We are now focusing on cutting-edge technologies and products on [AI Academic Search](https://aminer.org/), [AI Paper Reading](https://aminer.org/), and [AMiner Deep Research](https://aminer.org/open/research), toward building powerful agents that plan, search, summarize, and reflect effciently and effectively.  



</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Author Name Disambiguation (AND)</div><img src='images/whoiswho.png' alt="sym" width="50%">


</div>
</div>
<div class='paper-box-text' markdown="1">

Name disambiguation, a fundamental problem in online academic systems, is now facing greater challenges with the increasing growth of research papers. We construct a million-scale human-annotated author name disambiguation benchmark WhoIsWho, divide the AND problem into several subtasks, and develop corresponding algorithms for each subtask.

- WhoIsWho Benchmark:  [[code & data]](https://github.com/THUDM/WhoIsWho)      
- From-Scratch Name Disambiguation:
  - [WWW'24] BOND: an end-to-end method that bootstraps the global clustering and local metric learning. [[code]](https://github.com/THUDM/WhoIsWho)   
  - [KDD'18] A representation learning method that incorporates both global and local information between documents.  [[code]](https://github.com/neozhangthe1/disambiguation)    
- INcorrect Assignment Detection: [KDD'25] GuARD: a multi-modal-like multi-turn instruction tuning framework for anomaly detection. [[code & data & model]](https://github.com/THUDM/WhoIsWho/tree/main/mind)        


</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Paper Source Tracing (PST)</div><img src='images/pst.png' alt="sym" width="50%">


</div>
</div>
<div class='paper-box-text' markdown="1">

Comprehending the patterns of scientific evolution, such as the trends of topics and the flow of ideas,
are critical for researchers in knowledge discovery. However, a notable gap persists between the large-scale and semantically rich citation relations and the backbone structure of scientific evolution. We construct a high-quality and ever-increasing dataset PST-Bench in computer science and present a live demo to automatically trace the source of any target paper based on its full text. [[code & data]](https://github.com/THUDM/paper-source-trace)  [[demo]](http://pst.aminer.cn)   


</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Open Academic Graph (OAG)</div><img src='images/oab-overview-en.png' alt="sym" width="50%">


</div>
</div>
<div class='paper-box-text' markdown="1">

The overarching goal of academic data mining is to deepen our comprehension of the development, nature, and trends of science. It offers the potential to unlock enormous scientific, technological, and educational value.
We release a series of human-curated academic benchmarks to foster the develeopment of academic data mining.  


- OAG: a series of billion-scale academic knowledge graphs. [[data]](https://www.aminer.cn/open-academic-graph)   
- OAG-Bench: a comprehensive, multi-aspect, and fine-grained human-curated benchmark based
on OAG, covering 10 tasks, 20 datasets, 70+baselines, and 120+experimental results to date. [[code]](https://github.com/zfjsail/OAG-Bench/tree/main)  [[data]](https://www.aminer.cn/data/) [[data challenge]](https://www.biendata.xyz/kdd2024/)     
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GitHub Repo</div><img src='images/pst.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Awesome Simultaneous Translation](https://github.com/zhangshaolei1998/Awesome-Simultaneous-Translation) \\
**Shaolei Zhang**

[![](https://img.shields.io/github/stars/zhangshaolei1998/Awesome-Simultaneous-Translation?style=social&label=Code+Stars)](https://github.com/zhangshaolei1998/Awesome-Simultaneous-Translation)

- A repository that collects the tookits, common datasets and paper list related to the research on Simultaneous Translation, including text-to-text machine translation and speech-to-text translation.
</div>
</div>



## Publications

**Small Language Model Makes an Effective Long Text Extractor**     
*The 39th Annual AAAI Conference on Artificial Intelligence (**AAAI**) 2025*      
Yelin Chen, **Fanjin Zhang**, Jie Tang      
[[pdf]](https://arxiv.org/pdf/2502.07286)  [[code & data]](https://github.com/THUDM/scholar-profiling/tree/main/sener)   

**GuARD: Effective Anomaly Detection through a Text-Rich and Graph-Informed Language Model**          
*The 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining (**KDD**) 2025*          
Yunhe Pang, Bo Chen, **Fanjin Zhang**, Yanghui Rao, Evgeny Kharlamov, Jie Tang      
[[pdf]](https://arxiv.org/pdf/2412.03930)  [[code & data & model]](https://github.com/THUDM/WhoIsWho/tree/main/mind)        

**SAM Decoding: Speculative Decoding via Suffix Automaton**    
*The 63rd Annual Meeting of the Association for Computational Linguistics (**ACL**) 2025*      
Yuxuan Hu, Ke Wang, Xiaokang Zhang, **Fanjin Zhang**, Cuiping Li, Hong Chen, Jing Zhang    
[[pdf]](https://arxiv.org/pdf/2411.10666)  [[code]](https://github.com/hyx1999/SAM-Decoding)    
  
**OAG-Bench: A Human-Curated Benchmark for Academic Graph Mining**       
*The 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (**KDD**) 2024*     
**Fanjin Zhang**, Shijie Shi, Yifan Zhu, Bo Chen, Yukuo Cen, Jifan Yu, Yelin Chen, Lulu Wang, Qingfei Zhao, Yuqing Cheng, Tianyi Han, Yuwei An, Dan Zhang, Weng Lam Tam, Kun Cao, Yunhe Pang, Xinyu Guan, Huihui Yuan, Jian Song, Xiaoyan Li, Yuxiao Dong, and Jie Tang     
[[pdf]](https://arxiv.org/pdf/2402.15810)  [[code]](https://github.com/zfjsail/OAG-Bench/tree/main)  [[data]](https://www.aminer.cn/data/) [[data challenge]](https://www.biendata.xyz/kdd2024/)     

**PST-Bench: Tracing and Benchmarking the Source of Publications**    
*arXiv:2402.16009*    
**Fanjin Zhang**, Kun Cao, Yukuo Cen, Jifan Yu, Da Yin, Jie Tang     
[[pdf]](https://arxiv.org/pdf/2402.16009)  [[code & data]](https://github.com/THUDM/paper-source-trace)     [[demo]](http://pst.aminer.cn)     

**BOND: Bootstrapping From-Scratch Name Disambiguation with Multi-task Promoting.**     
*The Web Conference (**WWW**) 2024*     
Yuqing Cheng, Bo Chen, **Fanjin Zhang**, and Jie Tang     
[[pdf]](https://arxiv.org/pdf/2404.08322) [[code]](https://github.com/THUDM/WhoIsWho)     


**Web-Scale Academic Name Disambiguation: the WhoIsWho Benchmark, Leaderboard, and Toolkit**      
*The 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (**KDD**) 2023*     
Bo Chen, Jing Zhang, **Fanjin Zhang**, Tianyi Han, Yuqing Cheng, XiaoYan Li, Yuxiao Dong, and Jie Tang      
[[pdf]](http://keg.cs.tsinghua.edu.cn/jietang/publications/KDD23-Chen-WhoIsWho.pdf)  [[code & data]](https://github.com/THUDM/WhoIsWho)     


**OAG: Linking Entities across Large-Scale Heterogeneous Knowledge Graphs**    
*IEEE Transactions on Knowledge and Data Engineering (**TKDE**) 2022*      
**Fanjin Zhang**, Xiao Liu, Jie Tang, Yuxiao Dong, Peiran Yao, Jie Zhang, Xiaotao Gu, Yan Wang, Evgeny Kharlamov, Bin Shao, Rui Li, and Kuansan Wang     
[[pdf]](https://ieeexplore.ieee.org/abstract/document/9950622) [[data]](https://www.aminer.cn/oag-2-1)    


**Understanding WeChat User Preferences and “Wow” Diffusion**    
*IEEE Transactions on Knowledge and Data Engineering (**TKDE**) 2021*    
**Fanjin Zhang**, Jie Tang, Xueyi Liu, Zhenyu Hou, Yuxiao Dong, Jing Zhang, Xiao Liu, Ruobing Xie, Kai Zhuang, Xu Zhang, Leyu Lin, and Philip S. Yu.     
[[pdf]](https://arxiv.org/pdf/2103.02930.pdf) [[code]](https://github.com/zfjsail/wechat-wow-analysis)    


**Self-supervised Learning: Generative or Contrastive**     
*IEEE Transactions on Knowledge and Data Engineering (**TKDE**) 2021*    
Xiao Liu, **Fanjin Zhang**, Zhenyu Hou, Li Mian, Zhaoyu Wang, Jing Zhang, and Jie Tang    
[[pdf]](https://arxiv.org/pdf/2006.08218.pdf)    

**OAG_know: Self-supervised Learning for Linking Knowledge Graphs**    
*IEEE Transactions on Knowledge and Data Engineering (**TKDE**) 2021*    
Xiao Liu, Li Mian, Yuxiao Dong, **Fanjin Zhang**, Jing Zhang, Jie Tang, Peng Zhang, Jibing Gong, and Kuansan Wang    
[[pdf]](http://keg.cs.tsinghua.edu.cn/jietang/publications/TKDE21-Liu-et-al-OAG-know.pdf) [[code]](https://github.com/Xiao9905/OAG_know)    

**OAG: Toward Linking Large-scale Heterogeneous Entity Graphs**    
*The 25th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (**KDD** <span style="color:red">**Oral**</span>) 2019*    
**Fanjin Zhang**, Xiao Liu, Jie Tang, Yuxiao Dong, Peiran Yao, Jie Zhang, Xiaotao Gu, Yan Wang, Bin Shao, Rui Li, and Kuansan Wang    
[[pdf]](http://keg.cs.tsinghua.edu.cn/jietang/publications/KDD19-Zhang-et-al-Open_Academic_Graph.pdf) [[code]](https://github.com/zfjsail/OAG) [[data & website]](https://www.aminer.cn/open-academic-graph)     

**Name Disambiguation in AMiner: Clustering, Maintenance, and Human in the Loop**     
*The 24th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (**KDD** <span style="color:red">**Oral**</span>) 2018*     
Yutao Zhang, **Fanjin Zhang**, Peiran Yao, and Jie Tang     
[[pdf]](http://keg.cs.tsinghua.edu.cn/jietang/publications/kdd18_yutao-AMiner-Name-Disambiguation.pdf) [[code]](https://github.com/neozhangthe1/disambiguation)    

**Profiling Web Users Using Big Data**    
*Social Network Analysis and Mining (**SNAM**) 2018*    
Xiaotao Gu, Hong Yang, Jie Tang, Jing Zhang, **Fanjin Zhang**, Debing Liu, Wendy Hall, and Xiao Fu    
[[pdf]](http://keg.cs.tsinghua.edu.cn/jietang/publications/SNAM18-user-profiling-with-big-data.pdf)     



## Experience  

2024.01 - Now, Postdoctoral Researcher, Tsinghua University, China   

2023.07 - 2023.12,  Algorithm Engineer, Zhipu AI, Beijing, China    

2017.09 - 2023.06, Ph.D. in Computer Science and Technology, Tsinghua University, China   

  - 2019.07 - 2020.11, Research Intern, Tencent, Beijing, China     

  - 2017.05 - 2017.09, Research Intern, Microsoft Research Asia, Beijing, China   

2013.09 - 2017.06, B.E. in Computer Science and Technology, Nanjing University, China    




## Academic Service

**PC Member**:   
2025: KDD   
2024: WSDM, AAAI, WWW, KDD  
2023: WSDM, AAAI   
2020: ECML-PKDD  

**Reviewer**: IEEE Transactions on Knowledge and Data Engineering (*TKDE*), 
  IEEE Transactions on Neural Networks and Learning Systems (*TNNLS*),
  IEEE Transactions on Big Data (*TBD*), 
  Social Network Analysis and Mining (*SNAM*),
  AI Open  

## Awards
Excellent Graduate Student from Department of Computer Science and Technology, Tsinghua University (2023)   
Alumnus Scholarship of Tsinghua University (2021 & 2019)  
Second Prize of the National Science and Technology Progress Award (2020)  
CAAI Annual Outstanding Scientific and Technological Achievement Award (2020)  
National Scholarship (2014)
