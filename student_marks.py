name = input("Student name: ")

maths =int(input("Maths marks: "))
science =int(input("Science marks: "))
english =int(input("English marks: "))

total =maths+science+english
percentage =total/3

print("/nStudent:", name)
print("Total marks=", total)
print("Percentage=", percentage)
if percentage>=75:
    print("Grade=A")
    print("Result= Pass")
elif percentage>=60:
    print("Grade=B")
    print("Result= Pass")
elif percentage>=40:
    print("Grade=C")
    print("Result= Pass")
else:
    print("Grade=F")
    print("Result= Fail") 
