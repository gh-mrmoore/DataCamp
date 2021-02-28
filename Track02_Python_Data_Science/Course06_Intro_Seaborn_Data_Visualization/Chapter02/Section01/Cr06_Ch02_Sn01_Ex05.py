# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", col="schoolsup", col_order=["yes", "no"])

# Show plot
plt.show()