num = int(input("Enter number to check: ")) # user inpit
i = 2 #loop variable initialization
p = 0 # conitional variable
while i < num:
    if num%i == 0: #check
        p = p+1 # if condition become true then change the value of variable p
    i = i +1 #loop increament
if p == 0: # if value of p is not change then it is prime
    print("prime")
else:
    print("Not prime")
