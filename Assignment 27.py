import matplotlib.pyplot as plt

# Data to plot
categories = ['Math', 'Science', 'History', 'English']
scores = [85, 90, 78, 88]

# Create a bar chart
plt.bar(categories, scores, color='skyblue')
plt.title('Student Scores')
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.ylim(0, 100)

# Display the chart
plt.show()
