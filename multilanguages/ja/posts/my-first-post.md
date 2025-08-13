---
title: "Study Record"
translationKey: "first-post" # 翻译的钥匙
date: 2025-08-11T20:13:51+09:00
# weight: 1
# aliases: ["/first"]
tags: ["My notes"]
author: "Liu Runzhi"
# author: ["Me", "You"] # multiple authors
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "for learning "
canonicalURL: "https://canonical.url/to/page"
disableHLJS: true # to disable highlightjs
disableShare: false
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
ShowWordCount: true
ShowRssButtonInSectionTermList: true
UseHugoToc: true

cover:
    image: "<image path/url>" # image path/url
    alt: "<alt text>" # alt text
    caption: "<text>" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: true # only hide on current single page
editPost:
    URL: "https://github.com/<path_to_repo>/content"
    Text: "Suggest Changes" # edit text
    appendFilePath: true # to append file path to Edit link
---

## hugo网站建立

- 建立一个网站用于记录学习的技术，研究计划和求职记录。
- 使用 hugo 和 git pages 实现
- 用于个人项目记录和面试展示

1. 记录网站建立

   - 安装和使用hugo <https://hugo.opendocs.io/installation/windows/>
   - install go scoop
   - cd hugo && go build

1. 使用hugo
     - `hugo new posts/my-first-post.md` 建立新的页面，模板在archetypes下进行调节。建立的文件在/content/posts下
     - content下的子文件夹会被自动识别为一个内容分区。
     - `hugo server`启动服务器
     - 在hugo.toml下进行配置 启用Profile进入名片模式
     - 
