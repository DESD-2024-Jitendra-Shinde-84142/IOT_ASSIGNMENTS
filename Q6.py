num = int(input("Enter the no : "))

def fact(num):
    i = 1
    fact = 1
    while i <= num:
        fact = fact * i
        i = i + 1
    print(f"Factorial of Number is : {fact}")


fact(num)