# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax.plot[0, 0](seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color = "b")
ax.plot[0, 0](seattle_weather["MONTH"], seattle_weather["MLY-PRCP-25PCTL"], color = "b", linestyle = "--")
ax.plot[0, 0](seattle_weather["MONTH"], seattle_weather["MLY-PRCP-75PCTL"], color = "b", linestyle = "--")

# Plot Austin precipitation data in the bottom axes
ax.plot[1, 0](austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color = "r")
ax.plot[1, 0](austin_weather["MONTH"], austin_weather["MLY-PRCP-25PCTL"], color = "r", linestyle = "--")
ax.plot[1, 0](austin_weather["MONTH"], austin_weather["MLY-PRCP-75PCTL"], color = "r", linestyle = "--")

plt.show()