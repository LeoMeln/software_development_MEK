#!/bin/bash

FILE_PATH="./system.log"
ERROR_CODE=1

# Тест файла
if [-f "$FILE_PATH" ]; then
    echo "Лог-файл найден."
else
    echo "Ошибка: файл не существует"
fi

# Числовое сравнение через CASE

case $ERROR_CODE in
    0)
        echo "Статус: ошибок нет." ;;
    1)
        echo "Статус: критическая ошибка!" ;;
    *)
        echo "Статус: неизвестный код" ;;
esac
