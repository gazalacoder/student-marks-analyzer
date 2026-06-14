import csv
import matplotlib.pyplot as plt

names = []
marks = []
with open("marks.csv","r")as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        names.append(row[0])
        marks.append(int(row[1]))

print("Average:", sum(marks)/len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))

plt.bar(names, marks)
plt.title("Student Marks Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
