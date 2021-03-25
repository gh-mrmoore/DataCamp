# Calculate the search rate for both groups simultaneously
print(ri.groupby('driver_gender').search_conducted.mean())