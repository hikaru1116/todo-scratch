# [bk_app] Todo-Scratchバックエンドアプリケーション 仕様書

Todo-Scratchアプリのバックエンドアプリケーション。  
バックエンドアプリの機能仕様については、[WebAPI仕様書](./api_design.md)を参照。  
またTodo-Scratchのアプリとしての仕様は、[こちら][.]を参照。

## pythonバージョン
- python: v3.9.0 ~ 

## 主な利用ライブラリ
- mysql-connector-python:8.0.22

## アプリケーション構成
[bk_base](.)を利用して実装したアプリケーションである。


## フォルダ構成

|  フォルダ  |  内容  |
| ---- | ---- |
|  controllers  |  |
|  handlers  | Contorollerのロジック処理を扱うファイルを格納 |
|  validators  | Controllerのリクエストパラメータ等のチェック処理を扱うファイルを格納 |
|  entities  |  アプリケーションのモデルオブジェクトを表現するEntityファイルを格納。  |
|  repositoreis  |  永続化処理を扱うファイルを格納  |
|  services  |  アプリケーションのモデルを操作する処理を扱うファイルを格納  |


## 依存関係

````mermaid
flowchart RL
    handlers --> controllers
    validators --> controllers
    services --> handlers
    repositoreis --> handlers
    repositoreis --> services
    entities
````
## WebAPI仕様

[こちら](./api_design.md)を参照