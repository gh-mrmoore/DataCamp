# Use the "ggplot" style and create new Figure/Axes
fig, ax = plt.subplots()
plt.style.use('ggplot')
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()