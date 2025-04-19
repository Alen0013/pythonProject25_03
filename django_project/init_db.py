import os
import subprocess


def init_db():
    # Применяем миграции
    subprocess.run(['python', 'manage.py', 'migrate'], check=True)

    # Создаем суперпользователя
    subprocess.run(['python', 'create_superuser.py'], check=True)

    print("Database initialization completed successfully!")


if __name__ == '__main__':
    init_db()