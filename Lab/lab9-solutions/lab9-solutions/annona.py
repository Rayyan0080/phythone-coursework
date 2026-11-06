def annona(L):
    count=0
    for i in range(len(L)):
        flag=True
        for j in range(len(L)):
            if L[i] == L[j] and i!=j:
                flag = False

        if flag:
            count=count+1
    return count

lst=[1, 0, 2, 0, 3]
result = annona(lst)
print(result)

