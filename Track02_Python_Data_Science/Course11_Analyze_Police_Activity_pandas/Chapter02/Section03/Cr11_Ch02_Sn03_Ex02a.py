# Calculate the search rate for male drivers
print(ri[ri.driver_gender == 'M'].search_conducted.mean())