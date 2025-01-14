name = input("Enter your name : ")
print("hiii")
print("Hello, " + name + "!")
num = int(input("Enter a number: "))
if(num%2 == 0):
    print("Even")
else:
    print("Odd")

def greet(n):
    return f"hiiii {n}"    
print(greet(name))

list = ["a", "b", "c"]

list.append("d")
print(list)