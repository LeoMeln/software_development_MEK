#!/bin/bash

echo "=== Оценки выше 80 ==="
awk '$2>80' students.txt

echo "=== Оценки ниже 70 ==="
awk '$2<70' students.txt

echo "=== Первая строка ==="
awk 'NR==1' students.txt
