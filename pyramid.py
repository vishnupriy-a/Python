def pyramid(n):
    print(" pyramid is:")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i*j, end=" ")
        print("\n")
n=int(input("enter the number of lines:"))
pyramid(n)
 





















