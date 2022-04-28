# todo-scratch

python で作るフルスクラッチな TODO アプリケーション

## 構成

##　利用ライブラリ

- mysql-connector-python:8.0.22

### バックエンド

- python
- gunicorn

### フロントエンド

- javascript
- React

## 機能

- TODO 機能
- ユーザ認証
- データキャッシュ
- エラーハンドリング
- DB マイグレーション
- セキュリティ

## 動作手順

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
