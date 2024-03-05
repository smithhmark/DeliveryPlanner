#!/usr/bin/env bash
#
date > results.out
for file in example_data/*.txt
do
  echo "" >> results.out
  echo "$file" >> results.out
  python3 planner.py -v "$file" >> results.out
  echo "" >> results.out
  date >> results.out
done

