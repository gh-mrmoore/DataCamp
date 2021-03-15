# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['cuisine_type'], limit = len(restaurants['cuisine_type']))

# Inspect the first 5 matches
print(matches[0:5])