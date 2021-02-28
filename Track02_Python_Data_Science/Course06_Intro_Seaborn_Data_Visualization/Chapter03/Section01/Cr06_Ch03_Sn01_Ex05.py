# Create bar plot of average final grade in each study category
order_categories = ["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"]
sns.catplot(x="study_time", y="G3", data=student_data, order=order_categories, kind="bar")

# Show plot
plt.show()