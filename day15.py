list = [5, 42, 16, 35, 70, 22, 59, 61]

def findMaxIndex(a):
    idx = 0
    for i in range (len(a)):
        if a[idx] < a[i]:
            idx = i
    return idx

print("최댓값:", list[findMaxIndex(list)])  
print("최댓값의 인덱스:", findMaxIndex(list))
