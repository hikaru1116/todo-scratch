# 1. WSGIのアプリケーションは、2つの引数を持った呼び出し可能なオブジェクトである。

# 2. 第2引数として渡されたオブジェクトを呼び出し、HTTPステータスコードとヘッダ情報を渡す。

# 3. レスポンスボディとしてバイト文字列をyieldするiterableなオブジェクトを返す。

def app(env, start_response):
    start_response('200 OK', [('Content-type', 'text/plain; charset=utf-8')])
    print('Hello, World!!!')
    return [b'Hello World Hikaru']
