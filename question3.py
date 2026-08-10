num=int(input())
n=0
Even_count=0
odd_count=0
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    if (num*i)%2==0:
        Even_count+=1
    else:
        odd_count+=1
print("Even count:",Even_count)
print("Odd count:",odd_count)
