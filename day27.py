import pandas as pd

data = {
    "Name": ["Akshmith", "Roopesh", "Pranvi", "Karan", "Suraksha", "Sharvya", "Jagruthi"],
    "Department": ["AI", "AI", "ML", "Data Science", "AI", "ML","Data Science"],
    "Marks": [85, 78, 92, 74, 88, 70, 60]
}

df = pd.DataFrame(data)

print("\nStudent Dataset:\n")
print(df)

avg_marks = df.groupby("Department")["Marks"].mean()
print("\nAverage Marks by Department:\n")
print(avg_marks)
