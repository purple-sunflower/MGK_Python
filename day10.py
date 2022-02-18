num = int(input("정수를 입력하세요: "))

def getTotal(a):
    sum = 0
    for i in range (0,num+1):
        sum+=i
        i+=1
    return sum

answer = getTotal(num)
print(answer)