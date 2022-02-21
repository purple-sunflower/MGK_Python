list = [] # 빈 리스트 생성

count = 0 # 반복 횟수
sum = 0 # 정수의 합

while (count < 7):
    a = int(input("정수를 입력해주세요: "))
    list.append(a)
    count+=1
    sum+=a

print("평균" , sum/7)
