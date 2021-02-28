# Create a scatter plot of G1 vs. G3
sns.relplot(x="G1", y="G3", data=student_data, kind="scatter")

# Show plot
plt.show()