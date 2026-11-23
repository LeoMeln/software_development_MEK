#!/bin/bash

# Сбор данных у пользователя

read -p "Ваш вес (кг): " WEIGHT
read -p "Ваш рост (м): " HEIGHT

# Округление в целые
HEIGHT=${HEIGHT/,/.}

# Вычисляем ИМТ
BMI=$(awk -v w="$WEIGHT" -v h="$HEIGHT" 'BEGIN {printf "%.0f", w/(h*h)}')
echo "Ваш ИМТ: $BMI"
