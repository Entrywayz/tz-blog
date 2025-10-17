## Как собрать и запустить проект локально

### Предварительные требования
- Установленные Docker и Docker Compose

### Запуск проекта

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Запустите проект с помощью Docker Compose:
```bash
docker-compose up --build
```

3. Приложение будет доступно по адресу: `http://localhost:8080`

4. Документация API доступна по адресу: `http://localhost:8080/docs`

### Остановка проекта
```bash
docker-compose down
```

Для полной очистки с удалением volumes:
```bash
docker-compose down -v
```

## Описание API

### Получить все посты

**Запрос:**
```http
GET /posts
```

**Ответ:**
```json
[
  {
    "id": 1,
    "title": "Мой первый пост",
    "content": "Содержание первого поста",
    "created_at": "2023-10-01T12:00:00"
  },
  {
    "id": 2,
    "title": "Второй пост",
    "content": "Содержание второго поста",
    "created_at": "2023-10-01T13:00:00"
  }
]
```

### Создать новый пост

**Запрос:**
```http
POST /posts
Content-Type: application/json

{
  "title": "Новый пост",
  "content": "Содержание нового поста"
}
```

**Ответ:**
```json
{
  "id": 3,
  "title": "Новый пост",
  "content": "Содержание нового поста",
  "created_at": "2023-10-01T14:00:00"
}
```

## Как проверить работоспособность (smoke-тест)

1. **Проверить доступность API:**
```bash
curl http://localhost:8080/posts
```

2. **Создать тестовый пост:**
```bash
curl -X POST "http://localhost:8080/posts" \
-H "Content-Type: application/json" \
-d '{"title": "Тестовый пост", "content": "Это тестовый пост для проверки работы API"}'
```

3. **Получить список всех постов:**
```bash
curl http://localhost:8080/posts
```

### Способ 3: Проверка логов

Проверьте логи приложения для диагностики:
```bash
docker-compose logs app
```

Проверьте логи базы данных:
```bash
docker-compose logs db
```

### Ожидаемый результат
- API должно возвращать корректные HTTP статусы (200, 201)
- Посты должны успешно создаваться и возвращаться в списке
- Отсутствие ошибок в логах приложения и базы данных

## Структура проекта

```
project/
├── docker-compose.yml
├── Dockerfile
└── app/
    ├── main.py
    ├── database.py
    ├── models.py
    └── schemas.py
```