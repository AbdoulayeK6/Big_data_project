#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
    fields = line.strip().split(",")

    # Remove punctuation and convert to lowercase
    words = re.findall(r'\b\w+\b', line.lower())
    for word in words:
        print(f"{word}\t1")
