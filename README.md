# Проект «API для Yatube»

## Описание проекта:

В данном проекте реализован функционал API социальной сети, где пользователи могут создавать публикации, комментировать их, а так же подписываться на других пользователей и сообщества.

## Основные возможности API:

- Публикации:
  - Получение списка публикаций: запрос возвращает список всех публикаций с поддержкой пагинации. 
  - Создание публикации: аутентифицированные пользователи могут добавлять новые публикации. 
  - Поучение, обновление, частичное обновление и удаление публикации по ID: доступно только автору публикации. 
- Комментарии:
  - Получение всех комментариев к публикации: запрос возвращает список комментариев для указанной публикации.
  - Добавление комментария: только аутентифицированные пользователи могут добавлять комментарии.
  - Получение, обновление, частичное обновление и удаление комментария по ID: доступно только автору комментария.
- Сообщества:
  - Получение списка сообществ: возвращает список доступных сообществ.
  - Получение информации о сообществе по ID.
- Подписки:
  - Получение списка подписок: возвращает все подписки текущего пользователя.
  - Добавление подписки: пользователь может подписаться на другого пользователя.
- Аутентификация:
  - Получение JWT-токена: для аутентификации пользователя.
  - Обновление и проверка JWT-токена: обновление истекшего токена и проверка валидности токена.

## Безопасность:

  - Анонимные запросы на создание, обновление и удаление публикаций и комментариев запрещены.
  - Все действия, связанные с изменением данных, доступны только авторизованным пользователям.

## Примеры запросов к API:

Создание пользователя:
```http request
POST http://127.0.0.1:8000/api/v1/users/
Content-Type: application/json

{
  "username": "New_user",
  "password": "Change_me",
  "email": "new_user@email.com"
}
```

Получение JWT-токена:
```http request
POST http://127.0.0.1:8000/api/v1/jwt/create/
Content-Type: application/json

{
  "username": "New_user",
  "password": "Change_me"
}
```

Создание новой публикации:
```http request
POST http://127.0.0.1:8000/api/v1/posts/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "New post",
  "group": 1
}
```

Получение информации о публикации по ID:
```http request
GET http://127.0.0.1:8000/api/v1/posts/1/
```

Обновление публикации по ID:
```http request
PUT http://127.0.0.1:8000/api/v1/posts/1/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "Updated post"
}
```

Удаление публикации по ID:
```http request
DELETE http://127.0.0.1:8000/api/v1/posts/1/
Content-Type: application/json
Authorization: Bearer <your_access_token>
```

Получение списка публикаций с пагинацией:
```http request
GET http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2
```

Добавление комментария к публикации:
```http request
POST http://127.0.0.1:8000/api/v1/posts/1/comments/
Content-Type: application/json
Authorization: Bearer <your_access_token>

{
  "text": "new comment"
}
```

Получение комментариев к публикации:
```http request
GET http://127.0.0.1:8000/api/v1/posts/1/comments/
```

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/clifforc/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv .venv
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```