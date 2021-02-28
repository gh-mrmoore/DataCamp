# Create a point plot with subgroups
sns.catplot(x="romantic", y="absences", data=student_data, hue="school", kind="point")

# Show plot
plt.show()