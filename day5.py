#python의 input()은 기본적으로 모든 입력값을 문자열로 저장


#1번 : 20200101 입력 시 2020년 01월 01일로 출력
birthday = input("생일을 입력해주세요: ")

print(birthday[0:4] + "년")
print(birthday[4:6] + "월")
print(birthday[6:8] + "일" + "\n")

#2번: 20200101 입력 시 2020년 1월 1일로 출력
a = int(birthday)
b = a // 10000  #년도 출력
c = (a % 10000) // 100 #월 출력
d = c % 100

print(b , "년")
print(c , "월")
print(d , "일")
