#
# Gunicorn config file
#
wsgi_app = 'wsgi:create_app()'

# Server Mechanics
# ========================================
# current directory
chdir = '/Users/user/repository/todo-scratch/src/'

# daemon mode
daemon = False

# enviroment variables
# raw_env = [
#     'ENV_TYPE=dev',
#     'HOGEHOGE_KEY=xxxxxxxxxxxxxxxxxxxxxxxxx'
# ]

# Server Socket
# ========================================
bind = '0.0.0.0:8000'

# Worker Processes
# ========================================
workers = 2

#  Logging
# ========================================
# access log
accesslog = '/Users/user/repository/todo-scratch/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# gunicorn log
errorlog = '-'
loglevel = 'info'
