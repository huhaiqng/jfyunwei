#!/bin/bash
cd /jsb
export ENV_FILE=jsb/.prod

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple importlib-metadata==3.10.1
pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt

[ -f /var/run/celery/worker.pid ] && rm -f /var/run/celery/worker.pid
celery multi start -A jsb worker -c 2 -l info -f logs/worker.log
nohup celery -A jsb beat -l info -f logs/beat.log  >/dev/null 2>&1 &
# python manage.py runserver
gunicorn jsb.wsgi --bind=0.0.0.0:8000 --log-file logs/INFO.log --workers 2
