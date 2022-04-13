## ソフトインストール

1. Aanaconda をインストール
   [ダウンロードサイト](https://www.anaconda.com/products/individual)からインストーラをダウンロード

2. mysql をインストール
   [ここ](https://qiita.com/houtarou/items/a44ce783d09201fc28f5)を参考に Ubuntu へ MySql をインストール

## gunicorn

- gunicorn での python アプリケーション実行について  
  [ここ](https://docs.gunicorn.org/en/latest/run.html)にアプリケーション実行の方法が記載されている。  
  多分 Flask と同じ方法になると思う。

### Web サーバーの使用方法(Gunicorn)

Web サーバーに Gunicorn を採用し開発を行う。

#### ローカル環境で動作させる手順

- サーバー起動  
  gunicorn でローカルサーバーを起動

```
$ gunicorn 'wsgi:create_app()'
```

- デーモンでローカルサーバーを起動
  gunicorn.conf.py へデーモンで動作させる設定を記載している。

```
$ gunicorn --config gunicon.conf.py
```

- デーモンで動作する gunicorn を停止させるコマンド(gunicorn のデーモン Kill コマンド)

```
$ kill -9 `ps aux | grep gunicorn | awk '{print $2}'`
```

### 　 linix サーバーで動作させる方法

サービス化せず起動させるのであれば[上記](#ローカル環境で動作させる手順)と同様。
ここではサービスとしてプログラムを常駐する手順を記載する。

1. service ファイルを作成  
   gunicorn.service の内容を確認

2. gunicorn.service を自動起動させるコマンドを実行

```
# 起動
$ systemctl start gunicorn.service
#　自動起動
$ systemctl enable gunicorn.service
```
