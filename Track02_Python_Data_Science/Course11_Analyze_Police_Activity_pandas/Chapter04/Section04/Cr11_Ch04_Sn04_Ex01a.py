# Calculate the arrest rate for each 'rating'
print(ri_weather.groupby('rating').is_arrested.mean())