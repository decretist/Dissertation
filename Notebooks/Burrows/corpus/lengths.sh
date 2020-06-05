#!/bin/bash
while read -r line
do
    echo $line | wc -w
done < a/psAug.txt

