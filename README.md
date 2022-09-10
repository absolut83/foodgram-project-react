# Продуктовый помощник

## Описание

«Продуктовый помощник»: это ресурс, на котором пользователи публикуют рецепты, добавляют чужие рецепты в избранное и подписываются на публикации других авторов.

### Запуск проекта в Docker compose

- Установите Docker.

Параметры запуска описаны в файлах `docker-compose.yml` и `nginx.conf` которые находятся в директории `infra/`

- Запуск docker compose:

```bash
docker-compose up -d --build
```  

- Сбор статики:

```bash
docker-compose exec backend python manage.py collectstatic --no-input
```  

- Миграции:

```bash
docker-compose exec backend python manage.py migrate
```

- Запустите процесс загрузки ингредиентов и тегов (папки дата внутри backend):

```bash
docker-compose exec backend python manage.py load_ingrs
```

```bash
docker-compose exec backend python manage.py load_tags
```

- Создайте суперпользователя:

```bash
docker-compose exec backend python manage.py createsuperuser
```

### Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env

```python
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres 
DB_HOST=db 
DB_PORT=5432 
```

Проект запущен на боевом сервере по адресу:

```bash
http://84.201.176.122/
```


Логин для доступа в админку:

```bash
absolut83
```

Пароль:

```bash
16051983
```
## Об авторе
### Виталий Яремчук

absolut83@mail.ru

Telegram - @kuvalda684