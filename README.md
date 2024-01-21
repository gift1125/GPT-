# Wikipedia Featured Article Scraper

このプロジェクトは、Wikipediaのメインページから「Today's featured articlr」セクションのタイトルを抽出し、テキストファイルに保存するウェブスクレイピングツールです。

## セットアップ方法

このプロジェクトを実行するには、Python がインストールされている必要があります。また、必要なライブラリをインストールするために以下のコマンドを実行してください:

pip3 install requests beautifulsoup4

## 使用方法

プロジェクトのルートディレクトリで以下のコマンドを実行してください:
python scraper.py

これにより、スクレイピングされたデータが`featured_article.txt`ファイルに保存されます

