#### 前端生产环境部署

提取管理端静态文件

```
python manage.py collectstatic
```

上传文件前端静态文件到 /data/yunwei/jfywf

添加 nginx vhost

```
server {
    listen       80;
    server_name  _;
    charset utf-8;
    client_max_body_size 200m;

    location / {
        root /data/yunwei/jfywf;
    }

    location ^~ /djstatic {
        root /data/yunwei/jsb;
    }

    location ^~ /api {
        proxy_pass    http://127.0.0.1:8000;
        keepalive_timeout  600;
        proxy_read_timeout 600;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location ^~ /admin {
        proxy_pass    http://127.0.0.1:8000;
        keepalive_timeout  600;
        proxy_read_timeout 600;
        proxy_redirect off;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

```



#### 后端生产环境部署

安装 gunicorn

```
pip install gunicorn
```

启动

```
nohup gunicorn jsb.wsgi --bind=0.0.0.0:8000 --log-file logs/INFO.log >/dev/null 2>&1 &
```

