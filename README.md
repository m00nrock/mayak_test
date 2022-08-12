# Тестовое задание для компании Mayak Travel
Стек технологий: Python 3, Aiogram, SQLite

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
### Описание проекта:  
  Данный телеграм бот выступает в записывает данные в БД из файла xlxs.
 
### Как запустить проект:  

#### 1. для разработки:  
Клонировать репозиторий и перейти в него в командной строке:  
  
```shell
git clone https://github.com/m00nrock/mayak_test.git
```


Создать и активировать виртуальное окружение:  
  
```shell
python -m venv venv  
```
  
```shell
source venv/bin/activate  
```
  
```shell
python -m pip install -U pip  
```
  
Установить зависимости из файла requirements.txt:  
  
```shell
pip install -r requirements.txt  
```

Создать файл .env и указать в нём токен телеграм бот.
Пример заполнения в файле .env.example


Запустить проект:  
  
```shell
python3 main.py  
```

#### Ссылки проекта
https://t.me/mayak_moonrock_test_bot


#### TODO
Реализовать ci/cd
Рефактор основной логики
Реализовать парсинг сайтов из БД
Реализовать валидацию (на формат файла, на заполнение файла)
Упаковать БД и бота в докер-контейнеры, реализовать запуск через docker-compose