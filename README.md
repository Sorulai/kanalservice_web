# kanalservice_web

## Запуск с помощью докера
1. Для запуска скрипта через докер, необходимо находится в директории __*kanalservice_web*__ 

2. Нужно дать скриптам права доступа для испольнения с помощью комманд
``` 
chmod +x kanalservice_back/entrypoint.sh
chmod +x kanalservice_back/entrypoint_celery.sh
chmod +x kanalservice_back/entrypoint_celery_beat.sh 
chmod +x kanalservice_front/entrypoint-front.sh 
```
3. Запустить Докер

``` sudo docker-compose up --build``` 

***

## Запуск без докера

### Дополнительные утилиты
>Python
>
>PostgreSQL
>
>Redis
>
>Node
>
>npm

### Подготовка для запуска

1. Для начала необходимо заменить константы в файле .env
- Для этого нужно перейти в __*kanalservice_web/kanalservice_back/*__ и в файле *.env* заменить данные от PostgreSQL и Redis 
``` 
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=kanalservice-web
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

REDIS_HOST=localhost
REDIS_PORT=6379
...
```

2. Возвращаемся в директорию __*kanalservice_web*__ , создаем вирутальное окружение и активируем его.
- `python3 -m venv env `
- `source env/bin/activate `

4. Далее устанавливаем все зависимости из *requirements.txt*
- `pip install -r kanalservice_back/requirements.txt `

5. Создаем БД *kanalservice-web* в PostgreSQL(проверьте что бы название в .env файле совпадало с названием вашей БД)

6.Переходим в директорию __*kanalservice_back*__

7. Применяем миграции и запускаем сервер
- `python3 manage.py migrate`
- `python3 manage.py runserver`

9. Открываем новый терминал,запускаем виртуальное окружение,переходим в __*kanalservice_back*__ и запускаем воркер celery 
- `celery -A kanalservice_back worker -l info`

10. Открываем новый терминал,запускаем виртуальное окружение,переходим в __*kanalservice_back*__ и запускаем celery beat
- `celery -A kanalservice_back beat -l info`

11.Возвращаемся в начальную директорию и переходим в директорию __*kanalservice_front*__

12.Переходим в файл *App.js* , который находится в  __*kanalservice_front/src*__, в 12 строке нужно поменять порт с *1337* на порт django сервера(по умолчанию *8000*)

13.Находясь в директории __*kanalservice_front*__ устанавливаем React
- `npm install react-script`
- 
14.После установки запускаем react сервер
- `npm start`

Переходим в приложение по ссылке [http://localhost:3000/]([lifehacker.ru](http://localhost:3000/))
