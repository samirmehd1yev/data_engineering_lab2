from pymongo import MongoClient
import re
from collections import defaultdict

# Connect to the MongoDB database
client = MongoClient('localhost', 27017)
db = client.my_db
tweets = db.tweets

# Define the aggregation pipeline
pipeline = [
    {"$match": {"retweeted_status": {"$exists": False}}},  # Exclude retweets
    {"$project": {"text": 1, "_id": 0}}  # Project only the 'text' field
]
tweets = list(tweets.aggregate(pipeline))

# Define pronouns to count
pronouns = ["han", "hon", "den", "det", "denna", "denne", "hen"]
pronoun_counts = defaultdict(int)

# Compile a regex pattern for matching pronouns case-insensitively
pronoun_pattern = re.compile(r'\b(han|hon|den|det|denna|denne|hen)\b', re.IGNORECASE)

# Count occurrences of each pronoun in tweets
for tweet in tweets:
    matches = set(pronoun_pattern.findall(tweet["text"]))
    for match in matches:
        pronoun_counts[match.lower()] += 1

# Print and write the pronoun counts to a text file
with open("pronouns_count.txt", "w") as file:
    for pronoun, count in pronoun_counts.items():
        print(f"{pronoun}\t{count}")
        file.write(f"{pronoun}\t{count}\n")

print("Pronoun counts have been successfully saved to pronouns_count.txt.")
