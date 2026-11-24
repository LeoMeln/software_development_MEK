#!/bin/bash

for i in $(seq 1 10); do
    touch "test$i.txt"
    echo "Создан: test$i.txt"
done

i=10
while [ "$i" -ge 1 ]; do
    rm "test$i.txt"
    echo "Удален: test$i.txt"
    i=$((i - 1))
done
