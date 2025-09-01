# Учет движения денежных средств

Результат выполнения тестового задания

### Технологии
- Python, Django
- HTML, CSS (Bootstrap)
- SQLite

## Как запустить

1. Клонируйте репозиторий
```bash
git clone https://github.com/filimanistr/cash-flow-test-task
```

2. Перейдите в директорию
```bash
cd cash-flow-test-task
```

3. Настройте окружение
```bash
python -m venv .venv
```

4. Активируйте окружение
   - на linux:
    ```bash
    . .venv/bin/activate
    ```
   - на windows
    ```bash
    .\.venv\Scripts\activate
    ```

5. Установите необходимые зависимости
```bash
python -m pip install -r requirements.txt
```

6. Запустите миграции и заполните базу тестовыми данными
```bash
python src/manage.py migrate
python src/manage.py loaddata src/accounting/fixtures/*
```

7. Запустите тестовый сервер
```bash
python src/manage.py runserver
```

## Демонстрация работы

Результат — сайт из нулевых, с перезагрузкой страницы на каждое нажатие. Вариант реализации без необходимости использования js. Главный недостаток такого подхода — плохой UX

![Home](https://github.com/filimanistr/cash-flow-test-task/blob/master/img/demo.mp4)
