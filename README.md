# Приложение

Веб-приложение с использованием Django, которое предоставляет пользователям интерфейс для управления данными, загруженными с внешнего ресурса, и реализует функции поиска и сортировки.

## Как запустить проект

1. Чтобы установить проект, выполните следующие шаги:

   1. Склонируйте репозиторий:

        git clone https://github.com/sergey-brovko/FinalCertification.git
        cd FinalCertification

   2. Установите необходимые зависимости:

        pip install -r requirements.txt

2. Чтобы запустить проект, выполните следующую команду:

    python manage.py runserver

## Как использовать команду для парсинга данных

Для парсинга данных с ресурса "" необходимо выполнить команду: python manage.py parse_data

## Как протестировать сортировку и поиск

1. Для выполнения сортировки: на главной странице приложения нажмите на кнопку "Сортировка по" и из выпадающего списка выберите по какому параметру нужна сортировка.

2. Для выполнения поиска по заголовку сообщения: на главной странице приложения введите ключевую фразу в поле "Поиск".

3. Для выполнения бинарного-поиска по ID сообщения: на главной странице приложения в поле "Поиск" введите "id::X", где X - номер ID сообщения.

