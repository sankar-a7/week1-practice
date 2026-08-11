values = [10, 10, 20, 20, 20, 30, 10, 10, 40]
result=[]
for i in values:
    if not result or i!=result[-1]:
        result.append(i)
print(result)