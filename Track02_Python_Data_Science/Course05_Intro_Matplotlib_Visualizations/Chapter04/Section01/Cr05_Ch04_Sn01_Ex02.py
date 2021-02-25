# Use the "Solarize_Light2" style and create new Figure/Axes
fig, ax = plt.subplots()
plt.style.use('Solarize_Light2')
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()