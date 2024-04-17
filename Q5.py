sub1 = int(input("Enter sub1 mark : "))
sub2 = int(input("Enter sub2 mark : "))
sub3 = int(input("Enter sub3 mark : "))

average = (sub1 + sub2 + sub3)/3

if average <= 100 and average >= 90:
    print("Grade : A")

if average <= 89 and average >= 80:
    print("Grade : B")

if average <= 79 and average >= 70:
    print("Grade : C")

if average <= 69 and average >= 60:
    print("Grade : D")

if average <= 59 and average >= 0:
    print("Grade : F")