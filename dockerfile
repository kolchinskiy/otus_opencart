# Используем базовый образ Python
FROM python:3.11

# Устанавливаем зависимости с помощью pip
RUN pip install allure-pytest
RUN pip install selenium
RUN pip install faker
RUN pip install requests

# Копируем все файлы из текущего каталога в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем тест
CMD ["python", "index.py"]