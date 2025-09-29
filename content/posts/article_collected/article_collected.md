from datetime import datetime, timezone, timedelta
import os

# Prepare front matter based on user's template, set draft to false
tz = timezone(timedelta(hours=9))
date_str = datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%S+09:00")

content = f"""---
title: 'Article_collected'
date: {date_str}
tags: []
author: "liurunzhi"
showToc: true
TocOpen: false
draft: false
hidemeta: false
comments: false
description: "Project papers list with English titles and Japanese one-sentence summaries"
canonicalURL: ""
disableHLJS: false
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
    image: ""
    alt: ""
    caption: ""
    relative: false
    hidden: false
editPost:
    URL: "https://github.com/<path_to_repo>/content"
    Text: "Suggest Changes"
    appendFilePath: true
---

# Project Papers (English Titles) — 概要は日本語

以下は本プロジェクトで利用している論文の一覧です。各項目は **英語の論文タイトル** と **日本語の一文要約** を併記し、リンクは Hugo の `/research_article/` 配下（`static/research_article/`）を指します。

1. [Detection of Social Signals for Recognizing Engagement](/research_article/Detection%20of%20social%20signals%20for%20recognizing%20engagement.pdf)  
   人間の社会的信号を検出し、対話におけるエンゲージメントを認識する手法を提案した研究。

2. [SANG: Socially Aware Navigation Between Groups](/research_article/SANGSocially%20Aware%20Navigation%20Between%20Groups.pdf)  
   群衆内の人々のF-formationを考慮し、グループ間を社会的に適切に移動するナビゲーション手法を示した研究。

3. [Robot-Centric Perception of Human Groups](/research_article/Robot-Centric%20Perception%20of%20Human%20Groupspdf.pdf)  
   ロボット視点から人間の群れを知覚・解析し、社会的相互作用に基づいた行動を可能にする方法を検討した研究。

4. [Exploiting Temporal Information to Detect Conversational Groups](/research_article/Exploiting%20temporal%20information%20to%20detect%20conversational.pdf)  
   時系列情報を活用して会話グループを検出するアルゴリズムを提案した研究。

5. [Intelligent LiDAR Navigation](/research_article/Intelligent%20LiDAR%20Navigation.pdf)  
   LiDARを用いた知的ナビゲーション技術を紹介し、ロボットの環境認識と移動精度の向上を目的とした研究。

6. [Learning Social Cost Functions for Human-Aware Path Planning](/research_article/LEARNING%20SOCIAL%20COST%20FUNCTIONS%20FOR.pdf)  
   社会的規範（列に並ぶ、会話を妨げない等）を学習し、ロボットの経路計画に組み込む手法を提案した研究。

7. [LMNav](/research_article/LMNav.pdf)  
   大規模言語モデルを用いて複雑な環境でのロボットナビゲーションを行う新しい枠組みを示した研究。

8. [Social Type-Aware Navigation Framework for Mobile Robots](/research_article/Social%20Type-Aware%20Navigation%20Framework%20for%20Mobile%20Robots.pdf)  
   子供や高齢者など多様な人の社会的特性を考慮してロボットが異なる回避行動を取る枠組みを提案した研究。

9. [F-Formation Detection: Individuating Free-Standing Conversational Groups in Images (Setti et al., 2015)](/research_article/setti2015.pdf)  
   画像からF-formationに基づく自由会話グループを自動検出するグラフカット手法を示した研究。

10. [Real-time Trajectory-based Social Group Detection](/research_article/Real-time%20Trajectory-based%20Social%20Group%20Detectionpdf.pdf)  
    人物の移動軌跡を利用し、リアルタイムにソーシャルグループを効率的に検出する手法を提案した研究。

11. [Social Group Human-Robot Interaction: A Scoping Review](/research_article/Social%20Group%20Human-Robot%20Interaction%20A%20Scoping%20Review.pdf)  
    グループにおける人間とロボットの相互作用に関する計算的課題を包括的に整理したレビュー論文。

12. [Following Is All You Need: Robot Crowd Navigation Using People As Planners](/research_article/Following%20Is%20All%20You%20Need.pdf)  
    群衆環境でロボットが人間をリーダーとして追従することで効率的に移動する新しい戦略を提案した研究。

13. [Social Interaction Inference and Group Emergent Leadership Detection Using Head Pose (Liu, Cornell Thesis)](/research_article/Liu_cornell_0058O_11132.pdf)  
    頭部姿勢を利用して会話中の相互作用やグループ内のリーダーを推定する手法を開発した研究。

14. [SPENCER: A Socially Aware Service Robot for Passenger Guidance in Airports](/research_article/A%20Socially%20Aware%20Service%20Robot%20for.pdf)  
    空港で乗客を案内・支援するために社会的に配慮したサービスロボットを開発した大規模プロジェクト。

15. [Improving Social Awareness Through DANTE](/research_article/Improving%20Social%20Awareness%20Through%20DANTEpdf.pdf)  
    深層学習を用いたDANTEモデルにより、会話グループを高精度で検出しロボット応用に活用する研究。

16. [Do As I Can, Not As I Say (SayCan)](/research_article/2204.01691v2.pdf)  
    大規模言語モデルとロボットの実行可能スキルを組み合わせ、高次タスクを現実環境で実行可能にする手法を示した研究。
 
17. [Emotion-LLaMA](/research_article/Emotion-LLaMA.pdf)  
    音声・映像・テキストを統合したマルチモーダル大規模言語モデルで、感情認識と推論を強化する研究。

18. [Detecting Groups and Estimating F-Formations for Social Human–Robot Interactions](/research_article/Detecting%20Groups%20and%20Estimating%20F-Formations%20for%20Social%20Human.pdf)  
    ロボットがセンサ情報を用いてグループとF-formationを推定し、適切に参加する枠組みを提案した研究。

19. [Social Navigation with Pedestrian Groups](/research_article/SOCIAL%20NAVIGATION%20WITH.pdf)  
    歩行者のグループを考慮した社会的ナビゲーションモデルを提案し、群衆環境での安全性を向上させた博士論文。

20. [Let Me Join You! Real-time F-formation Recognition by a Socially Aware Robot](/research_article/letmejoinyou.pdf)  
    ロボットがリアルタイムにF-formationを認識し、社会的に適切な角度からグループに参加できる手法を提案した研究。

---

**配置ガイド（Hugo）**  
- このページ（本 Markdown）を `content/posts/article_collected.md` に置く。  
- すべての PDF を `static/research_article/` に置く（ビルド後の公開URLは `/research_article/<filename>.pdf`）。  
"""

out_path = "/mnt/data/article_collected_hugo.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(content)

out_path
