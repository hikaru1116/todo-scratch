import multiprocessing

# ポート設定
bind = "0.0.0.0:8000"
# デーモン化
daemon = True
# ワーカ数の設定（システムコア数に応じて設定）
workers = multiprocessing.cpu_count() * 2 + 1
