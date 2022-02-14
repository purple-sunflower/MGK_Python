#1번

a = int(input("첫 번째 과목의 점수를 입력하세요: "))
b = int(input("두 번째 과목의 점수를 입력하세요: "))
c = int(input("세 번째 과목의 점수를 입력하세요: "))

avg = (a+b+c)/3

if avg >= 50:
    print("평균 점수는 " ,avg ,"점으로 합격입니다.\n")
else:
    print("평균 점수는 " ,avg ,"점으로 불합격입니다.\n")


#2번

w = input("단어를 입력해주세요: ")
s = input("문장을 입력해주세요: ")

if w in s: 
    print("단어가 있습니다.")
else:
    print("단어가 없습니다.")

#위와 같은 코드
#if w not in s: 
    #print("단어가 없습니다.")
#else:
    #print("단어가 있습니다.")