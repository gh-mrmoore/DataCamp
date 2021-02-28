# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet", y="G3", data=student_data, hue="location", kind="box", sym="")

# Show plot
plt.show()