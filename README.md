# Iris Classification API (Windows)

Микросервис для классификации видов ирисов на FastAPI и Docker.  
*Работает на Windows 10/11*

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0-green.svg)](https://fastapi.tiangolo.com/)

## Оглавление
- [Особенности](#особенности)
- [Требования](#требования)
- [Установка](#установка)
- [Запуск](#запуск)
- [Документация API](#документация-api)
- [Примеры запросов](#примеры-запросов)
- [Развертывание в Docker](#развертывание-в-docker)
- [Скриншоты](#скриншоты)

## Особенности
- REST API с эндпоинтами `/predict` и `/health`
- Валидация данных через Pydantic
- Автоматическая документация Swagger
- Готовый Docker-образ
- Логирование операций

## Требования
- Windows 10/11
- Python 3.9+
- Docker Desktop (для запуска в контейнере)

## Установка

1. Клонируйте репозиторий:
```powershell
git clone https://github.com/szhn1/iris-api.git
cd iris-api

2. Установите зависимости:
```powershell
pip install -r requirements.txt
```

## Запуск
### Локальный запуск
```powershell
uvicorn app.main:app --reload
```

### Docker-контейнер
```powershell
docker build -t iris-api .
docker run -p 8000:8000 iris-api
```

## Документация API
Доступна после запуска по адресу:  
`http://localhost:8000/docs`

![Swagger UI]

## Примеры запросов (PowerShell)
### Проверка работоспособности
```powershell
Invoke-WebRequest -Uri "http://localhost:8000/health" -Method GET
```

### Предсказание класса
```powershell
$Body = @{
    sepal_length = 5.1
    sepal_width = 3.5
    petal_length = 1.4
    petal_width = 0.2
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:8000/predict" `
-Method POST `
-Headers @{"Content-Type" = "application/json"} `
-Body $Body
```

## Развертывание в Docker
1. Соберите образ:
```powershell
docker build -t iris-api .
```

2. Запустите контейнер:
```powershell
docker run -p 8000:8000 iris-api
```

3. Проверьте логи:
```powershell
docker logs <ID_контейнера>
```

