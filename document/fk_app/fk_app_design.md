# [ft_app] Todo-Scratch フロントエンドアプリケーション 仕様書

Todo-Scratch アプリのフロントエンドアプリケーション。  
招待したユーザで作成したグループでタスク管理を行うことができます。

## バージョン

- npm: v8.1.0 〜
- node: v16.13.0 〜

## 利用したライブラリ

- [react-router-dom](https://reactrouter.com/)
- [material ui](https://mui.com/)
- [axios](https://github.com/axios/axios)
- [swiper](https://swiperjs.com/)

## アプリケーション構成

React を利用したアプリケーション。
状態管理は ReactHooks を使用し、Flux アーキテクチャの設計思想をもとにした構成とした。

## 機能・画面設計一覧

| 機能・画面                                                    | 内容                                                 |
| ------------------------------------------------------------- | ---------------------------------------------------- |
| [共通機能]()                                                  | Todo-Scratch アプリの画面共通機能                    |
| [サインイン ](./screens/signin_design.md)                     | ユーザがログインする画面                             |
| [ユーザ登録 ](./screens/signup_design.md)                     | ユーザがアカウントを新規登録する画面                 |
| [タスク一覧](./screens/task_list_desgin.md)                   | タスクの一覧を表示をする画面                         |
| [タスク詳細・編集 ](./screens/task_detail_desgin.md)          | 指定したタスクの詳細情報の表示・内容の編集をする画面 |
| [アカウント編集 ](./screens/account_desgin.md)                | ユーザのアカウント情報の編集をする画面               |
| [グループ設定閲覧・編集 ](./screens/group_settings_desgin.md) | グループの設定情報の閲覧・編集をする画面             |
| [招待グループ一覧 ](./screens/grpup_approve_list_desgin.md)   | ユーザが招待されているグループを表示する画面         |
| [参加グループ一覧 ](./screens/group_joined_list_desgin.md)    | ユーザが参加しているグループの一覧を表示する画面     |
| [新規グループ作成 ](./screens/group_create_design.md)         | 新しいグループの作成画面                             |
