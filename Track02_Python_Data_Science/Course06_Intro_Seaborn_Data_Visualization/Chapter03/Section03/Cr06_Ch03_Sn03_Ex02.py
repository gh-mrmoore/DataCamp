# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point", capsize=0.2)
        
# Show plot
plt.show()