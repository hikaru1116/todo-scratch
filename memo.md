1. Aanaconda をインストール
   [ダウンロードサイト](https://www.anaconda.com/products/individual)からインストーラをダウンロード

2. mysql をインストール
   [ここ](https://qiita.com/houtarou/items/a44ce783d09201fc28f5)を参考に Ubuntu へ MySql をインストール

## 学習記録

- gunicorn での python アプリケーション実行について  
  [ここ](https://docs.gunicorn.org/en/latest/run.html)にアプリケーション実行の方法が記載されている。  
  多分 Flask と同じ方法になると思う。

- gunicorn のデーモン Kill コマンド

```
$ kill -9 `ps aux | grep gunicorn | awk '{print $2}'`
```

## TODO アプリ仕様

### 概要

- メモを記録する TODO アプリ
- メモには、下記の情報を載せる
  - タイトル
  - タグ
  - メモ
- メモを「閲覧」「詳細閲覧」「登録」「編集」「削除」をすることができる。
