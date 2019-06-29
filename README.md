# P018-EtherscanCrawler

### 零.简介

> File Type: Coding Project
>
> Version: 2.3
>
> Last Edit: 2019-06-29 17:47:22

项目状态：已完成

功能：爬取Etherscan.io的Token评论数据，以HTTP REQUEST JSON的形式存储

### 一. 如果使用代码请一定注意以下几点！！

1. Etherscan用的DISQUS被墙了，如果要使用代码，请一定一定要小飞机，**全局模式**，不然请求 Request Timeout

2. 请保证当前文件夹下，"JSON"文件夹已建立，不然python无法新建文件夹

3. Github下载代码后请补充完依赖包，PIP3 install 一下，建议采用PyCharm安装，非常方便

### 二. 原理解释

Etherscan和Disqus均有较为严格的反爬机制，经过多种方案尝试，最终采用 API+修改Thread参数 的方法进行修改

查看网页几百行代码，多个JS文件，最终追溯到了API，以BNB为例，其API为： https://disqus.com/api/3.0/threads/listPostsThreaded?limit=50&thread=5967110845&forum=etherscan&order=popular&cursor=1%3A0%3A0&mode=2&api_key=E8Uh5l5fHZ6gD8U3KycjAIAk46f68Zw7C6eW8WSjZvCLXebZ7p0r1yrYDrLilk2F

经过多次尝试，发现不同币种修改的信息仅为Thread，在Py代码中设置完HTTP Header，加载完本地Cockie后可进行迭代爬取

TOP 200 的 TOKEN 的 THREAD ID 是人工爬取的，文件保存在Google在线文档： https://docs.google.com/spreadsheets/d/1l124hgG4abUmwkh2w88Xys_BID9dI2yjsjaYAeEXnFQ/edit?usp=sharing 
