#!/bin/bash
# Detects music files with duplicate metadata and outputs a list.
# Uses muprint from https://github.com/ajeddeloh/musicPrinter and standard Linux CLI tools.
find . -type f -exec muprint -s 'A%ua' -s't%uf' -r _ $'%uA\t%ub\t%ut\t{}\n' {} \; 2>/dev/null | sort | tee list.txt |  cut -f 1-3 | uniq -d > dups.txt
grep -Fwf dups.txt list.txt > dup-files.txt
