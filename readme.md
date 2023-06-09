# Обрезка ссылок с помощью Битли

Данная программа использует Bitly Api для сокращения ссылок, либо подсчитывет число переходов по сокращенной ссылке формата битли.

## Как установить
Требуется интерпретатор Python3 и установленные библиотеки:

- `requests`
- `python-dotenv`

Версии библиотек указаны в файле `requirements.txt`. Для установки зависимостей использовать команду:

```
pip install -r requirements.txt
```

## Переменные среды
Для работы с программой требуется наличие Битли токена. Получить токен можно на сайте [документации api](https://dev.bitly.com/)

Токен требуется сохранить в скрытую(.env) переменную: 
- `BITLY_TOKEN`

## Запуск программы 
__Для сокращенния ссылок введите команду в консоле:__
```
python main.py ВАША_ССЫЛКА
```
В результате должны получить ответ в виде:
```
Короткая ссылка: ВАША_ССЫЛКА_В_ФОРМАТЕ_БИТЛИ 
```
__Для получения статистики переходов по ссылкам:__
```
python main.py ВАША_ССЫЛКА_В_ФОРМАТЕ_БИТЛИ 
```
В результате должны получить ответ в виде:
```
Кол-во переходов по ссылке битли: N
```
