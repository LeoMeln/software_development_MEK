#!/bin/bash

printf "%-15s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do
    [ -e "$file" ] || continue

    if [ ! -s "$file" ]; then
        continue
    fi

    SEQ=$(grep -v "^>" "$file" | tr -d '\n')

    A=$(printf '%s' "$SEQ" | grep -o "A" | wc -l)
    T=$(printf '%s' "$SEQ" | grep -o "T" | wc -l)
    G=$(printf '%s' "$SEQ" | grep -o "G" | wc -l)
    C=$(printf '%s' "$SEQ" | grep -o "C" | wc -l)

    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$A" "$T" "$G" "$C"
done
