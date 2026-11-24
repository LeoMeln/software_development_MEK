#!/bin/bash

echo "=== Сумма оценок ==="
awk '{s+=$2} END{print s}' students.txt

echo "=== Средняя оценка ==="
awk '{s+=$2; c++} END{print s/c}' students.txt

echo "=== Максимальная оценка ==="
awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt
