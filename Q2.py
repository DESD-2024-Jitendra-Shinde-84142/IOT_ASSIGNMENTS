num = int(input("Enter the no : "))

i = 1
rev = 0 
while i <= 4:
    rem =  int(num % 10)
    num = num / 10
    i = i + 1
    rev = rev*10 + rem
    
temp = rev   
print(f"{temp}")

j = 1
while j <= 4:
    rem =  rev % 10
    rev = rev / 10
    j = j + 1
    print(f"{int(rem)}",end=" ")

print("")

k = 1
val = 0
place = 1000
while k <= 4:
    rem =  int(temp % 10)
    temp = temp / 10
    k = k + 1
    val = rem*place
    place = place /10
    print(f"{int(val)}",end="+")

print("")
