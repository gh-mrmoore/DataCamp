# Calculate the search rate for female drivers
print(ri[ri.driver_gender == 'F'].search_conducted.mean())