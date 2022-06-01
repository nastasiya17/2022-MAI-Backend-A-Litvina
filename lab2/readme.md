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

<p>
  <img src="https://github.com/nastasiya17/2022-MAI-Backend-A-Litvina/blob/main/lab2/ab/3.png">
</p>

### Backend

> ab -n 10 -c 2 -t 1 -v 2 http://127.0.0.1:8000/ 

<p>
  <img src="https://github.com/nastasiya17/2022-MAI-Backend-A-Litvina/blob/main/lab2/ab/2.png">
</p>

### Backend c помощью проксирования

> ab -n 10 -c 2 -t 1 -v 2 http://localhost/backend/

<p>
  <img src="https://github.com/nastasiya17/2022-MAI-Backend-A-Litvina/blob/main/lab2/ab/1.png">
</p>



