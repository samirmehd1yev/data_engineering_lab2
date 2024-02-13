#!/usr/bin/env python
import sys
import json
import re

# Regular expression to match the pronouns in a case-insensitive way
pronouns = re.compile(r'\b(han|hon|den|det|denna|denne|hen)\b', re.IGNORECASE)

# Process each line from stdin
for line in sys.stdin:
    try:
        # Parse the JSON tweet
        tweet = json.loads(line)
        
        # Skip retweets
        if 'retweeted_status' in tweet:
            continue

        # Find all pronouns in the text
        matches = set(pronouns.findall(tweet['text']))
        
        # Emit count for each pronoun found
        for match in matches:
            print(f"{match.lower()}\t1")
    except json.JSONDecodeError:
        continue


