def sum(lst):
    total=0
    for x in range(0,len(lst)):
        total=total+lst[x]
    print(total)
lst=[]
lst=list(map(int,input("enter the numbers in list").split()))
sum(lst)





