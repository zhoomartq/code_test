# Тестовое задание на вакансию Junior Backend Developer в Codify Lab
Задача: 
Спроектировать и разработать API для системы опросов пользователей

### _Документация API_ (автодокументирование на swagger (drf-yasg) доступно по адресу http://0.0.0.0:8000/docs/ )

Сроки выполнения тестового задания:
2 - 4 рабочих дня

## Функционал для администратора системы:

Авторизация в системе
- Добавление/Изменение/Удаление опросов. 
- Атрибуты опроса: название, дата старта, дата окончания, описание.
- Добавление/Изменение/Удаление вопросов в опросе. 
- Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов).
- Получение пройденных опросов с детализацией по пользователю и по его ответам (учесть все типы вопросов)

## Функционал для пользователей системы:

- Регистрация/Авторизация в системе
- Получение списка активных опросов
- Прохождение опроса (учесть все типы вопросов)
- Получение пройденных пользователем опросов с детализацией по ответам (учесть все типы вопросов)

## Использовать следующие технологии: 
* Django
 * Django REST Framework
  * PostgreSQL и другое на усмотрение разработчика.


## Результат выполнения задачи:

Оформленный код решения на GitHub/GitLab/Bitbucket с понятным Readme.md описанием и интсукцией по развертыванию приложения
Документация по API

## Склонируйте репозиторий с помощью git
    git@github.com:zhoomartq/code_test.git /SSH
    https://github.com/zhoomartq/code_test.git /HTTPS 

### В файле ``` runtime.txt ``` указана версия питона

### перед запуском проекта создайте ```.env``` file и настройте бд как в файле ```env.example```

### Чтобы запустить проект на докере введите команду ```docker-compose up -d --build```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

* Создание суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```
### Далее введите свои данные для администратора
```bash
Username (leave blank to use 'username'): #username
Email address: username@username.com
Password: ********
Password (again): ********
Superuser created successfully.
```

### Введите команду ```docker-compose logs -f web``` для отслеживания запросов в приложении

* Приложение будет доступно по адресу: http://0.0.0.0:8000/
* Администрирование приложения будет доступно по адресу: http://0.0.0.0:8000/admin/
* Документация API (автодокументирование на swagger (drf-yasg) доступно по адресу http://0.0.0.0:8000/docs/ )

## Чтобы создать пользователя:
* Request method: POST
* URL: http://0.0.0.0:8000/registration/register/
* Body: 
    * username: 
    * password: 
* Example:
```
curl --location --request POST 'http://0.0.0.0:8000/registration/register/' \
--form 'username=%username' \
--form 'password=%password'
```

## Чтобы получить токен пользователя: 
* Request method: POST
* URL: http://0.0.0.0:8000/registration/login/
* Body: 
    * username: 
    * password: 
* Example:
```
curl --location --request POST 'http://0.0.0.0:8000/registration/login/' \
--form 'username=%username' \
--form 'password=%password'
```

## Чтобы создать опрос:
* Request method: POST
* URL: http://0.0.0.0:8000/api/quizzes/
* Header:
   *  Authorization: Token userToken
* Body:
    * title: title
    * end: format: YYYY-MM-DD 
    * description: description 
* Example: 
```
curl --location --request POST 'http://0.0.0.0:8000/api/quizzes/' \
--header 'Authorization: Token userToken' \ # Токен должен быть суперадмина (Токен суперадмина можно создать также как и обычного пользователя)
--header 'Content-Type: 'application/json'
--form 'title=title' \
--form 'end=end \
--form 'description=description'
```
### Детальнее можно ознакомиться в ```swagger``` документации http://0.0.0.0:8000/docs/ 

...

