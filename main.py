n = int(input("Enter the no. of row: "))

for i in range(n+1):
    for j in range(i):
        print("* ",end="")
    print("")