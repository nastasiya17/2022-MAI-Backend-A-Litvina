## Запуск ##

> gunicorn --workers 4 main:app

default - файл конфигурации nginx (/etc/nginx/sites-available) - отдача статических файлов и проксирование запросов 

## Backend-сервер

> http://localhost:8000/ 

или 

> http://localhost/backend/

## Статические файлы 

> http://localhost/public/index.html

## Производительность 

### Статические файлы

> ab -n 10 -c 2 -t 1 -v 2 http://localhost/public/index.html

<p align="center">
  <img src="">
</p>

### Backend

> ab -n 10 -c 2 -t 1 -v 2 http://127.0.0.1:8000/ 

<p align="center">
  <img src="">
</p>

### Backend c помощью проксирования

> ab -n 10 -c 2 -t 1 -v 2 http://localhost/backend/

<p align="center">
  <img src="">
</p>



