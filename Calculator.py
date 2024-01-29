def add(x,y):
    return x +y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation:")
print("a.Add")
print("b.Subtract")
print("c.multiply")
print("d.Division")

while True:
    option=input("Enter the option(a/b/c/d):")
    if option in ('a','b','c','d'):
        try:
            digit1=float(input("Enter the first digit:"))
            digit2=float(input("Enter the second digit:"))
        except ValueError:
            print("Invalid input.Please enter the number.")
            continue
            
        if option=='a':
            print(digit1,"+",digit2,"=",add(digit1,digit2))
            
        elif option=='b':
            print(digit1,"-",digit2,"=",subtract(digit1,digit2))
            
        elif option=='c':
            print(digit1,"*",digit2,"=",multiply(digit1,digit2))
            
        elif option=='d':
            print(digit1,"/",digit2,"=",divide(digit1,digit2))
            
        next_computation=input("Next try? (yes/no):")
        if next_computation=="no":
            break
        
    else: 
        print("Invalid Input")
        