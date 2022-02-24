class Calculator():
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class PerfectCal(Calculator):
    def module(self):
        result = self.first % self.second
        return result

numberOne = float(input("첫번째 숫자를 입력해주세요: "))
numberTwo = float(input("두번째 숫자를 입력해주세요: "))

numberResult = PerfectCal(numberOne, numberTwo)

way = int(input("계산 방법을 고르세요.\n(1.덧셈 2.뺄셈 3.곱셈 4.나눗셈(몫) 5.나눗셈(나머지)): "))

if way == 1:
    print(numberResult.add())
elif way == 2:
    print(numberResult.sub())
elif way == 3:
    print(numberResult.mul())
elif way == 4:
    print(numberResult.div())
elif way == 5:
    print(numberResult.module())    
else:
    print("숫자를 잘못 입력하셨습니다.")
