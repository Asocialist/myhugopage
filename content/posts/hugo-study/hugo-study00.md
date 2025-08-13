---
title: "Hugo Study Record01"
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
series: ["建站日记"]
canonicalURL: "https://canonical.url/to/page"
disableHLJS: false # to disable highlightjs
disableShare: false
hideSummary: false
searchHidden: false
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
    URL: "https://github.com/Asocialist/myhugopage/tree/main/content/"
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
     - hugo.toml下可以设置多语言模式暂时未开启
     - 在archetyoes下有默认模板default.md用于设置创建的新的页面

1. 部署
     - 部署在githubpages上
     - 通过github actions方式部署配置文件.github/workflow/develop.yal如下

     ``` yaml
      # Sample workflow for building and deploying a Hugo site to GitHub Pages
        name: Deploy Hugo site to Pages

        on:

        # Runs on pushes targeting the default branch

        push:
            branches: ["main"]

        # Allows you to run this workflow manually from the Actions tab

        workflow_dispatch:

        # Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages

        permissions:
        contents: read
        pages: write
        id-token: write

        # Allow only one concurrent deployment

        concurrency:
        group: "pages"
        cancel-in-progress: false

        # Default to bash

        defaults:
        run:
            shell: bash

        jobs:

            # Build job

            build:
            runs-on: ubuntu-latest
            steps:
            - name: Install Hugo CLI
                # Uses the latest version of Hugo specified by peaceiris/actions-hugo
                uses: peaceiris/actions-hugo@v3
                with:
                hugo-version: 'latest' # <-- Updated to 'latest' to fix version error
                extended: true

                - name: Install Dart Sass
                run: sudo snap install dart-sass

            - name: Checkout
                uses: actions/checkout@v4
                with:
                submodules: recursive
                fetch-depth: 0 # Needed for themes that rely on Git info

            - name: Setup Pages
                id: pages
                uses: actions/configure-pages@v5

            - name: Install Node.js dependencies
                run: "[[ -f package-lock.json || -f npm-shrinkwrap.json ]] && npm ci || true"

            - name: Build with Hugo
                env:
                HUGO_ENVIRONMENT: production
                HUGO_ENV: production
                run: |
                hugo \
                    --minify \
                    --baseURL "${{ steps.pages.outputs.base_url }}/"

            - name: Upload artifact
                uses: actions/upload-pages-artifact@v3
                with:
                path: ./public

            # Deployment job

            deploy:
            environment:
            name: github-pages
            url: ${{ steps.deployment.outputs.page_url }}
            runs-on: ubuntu-latest
            needs: build
            steps:
            - name: Deploy to GitHub Pages
                id: deployment
                uses: actions/deploy-pages@v4
      ```

### 未来改善

- _index.md设置暂不需要
- 多语言设置
- 评论暂不需要因为只用于记录
