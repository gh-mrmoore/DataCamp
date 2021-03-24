# Select educ
educ = gss['educ']

# Bachelor's degree
bach = (educ >= 16)

# Associate degree
assc = (16 > educ) & (educ >= 14)

# High school (12 or fewer years of education)
high = (12 >= educ)
print(high.mean())