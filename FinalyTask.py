# Написать программу, которая находит и удаляет дубликаты файлов
# в указанной директории и всех ее поддиректориях.

import os
import hashlib


def calculate_hash(file_path):
    """Расчитывает хеш-сумму файла"""
    with open(file_path, 'rb') as file:
        content = file.read()
        hash_sum = hashlib.md5(content).hexdigest()  # Используем MD5 сумму
    return hash_sum


def remove_duplicates(directory):
    """Находит и удаляет дубликаты файлов в указанной директории и всех ее поддиректориях"""
    hash_set = set()  # Множество для хранения хеш-сумм файлов
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_hash = calculate_hash(file_path)
            if file_hash in hash_set:
                os.remove(file_path)  # Удаляем дубликат файла
            else:
                hash_set.add(file_hash)  # Добавляем хеш-сумму в множество


# Вызов функции для поиска и удаления дубликатов файлов в указанной директории
remove_duplicates('C:\TEST')
# Здесь 'C:\TEST' замените на путь к директории, в которой нужно удалить дубликаты файлов.
