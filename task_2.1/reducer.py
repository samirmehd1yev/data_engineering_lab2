#!/usr/bin/env python
import sys
from collections import defaultdict

# Dictionary to hold pronoun counts
pronoun_counts = defaultdict(int)

# Read each line from stdin
for line in sys.stdin:
    # Parse the pronoun and count
    pronoun, count = line.strip().split('\t')
    
    # Increment the count for the pronoun
    pronoun_counts[pronoun] += int(count)

# Emit the final counts
for pronoun, count in pronoun_counts.items():
    print(f"{pronoun}\t{count}")

