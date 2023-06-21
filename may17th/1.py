# for i in range (10, 51, 10):
#     print(i, end = ' ')

# a=[10,20,30,40,50]
# for i in a:
#     print(i, end = ' ')

# a=[]
# for i in range(5):
#     item = int(input("정수입력 : "))
#     a.append(item)
# print(a)

# a=["안녕하세요","Hello","Hi","Bye"]
# for i in a:
#     print(i[0])

# a= (["바닐라","초코","딸기"],["과자","우유","아이스크림"])
# print(a)

# a=[10,20,30,40,50]
# print (a)
# print(min(a))
# print(max(a))
# print(sum(a))
# print(sum(a))
# print(sum(a)/len(a))

# students=int(input("학생 수 입력 : "))
# grade = []
# for i in range(5):
#     num= int(input(f"{i+1}번 정수 입력 : "))
#     grade.append(num)

# print(grade)
# print(max(grade))
# print(min(grade))
# print(sum(grade))
# print(sum(grade)/students)

from random import *
computerlotto = []
while len(computerlotto)<6: #자동 로또 번호
    x = randint(1, 45)
    if x not in computerlotto:
        computerlotto.append(x)

userlotto = []
a = 0
while(1): #사용자 로또 입력
    value = int(input("1~45까지 로또 번호를 입력 : "))
    if (value <= 0 or value >= 46):
        print("1부터 45 사이의 수를 입력하세요")
    else:
        userlotto.append(value)
        a = a + 1
        if(a >= 6):
            break

cnt = 0
for i in range(6):
    if(userlotto[i] == computerlotto[i]):
        cnt = cnt + 1
if(cnt == 6):
    print("6개 일치")
    print("")
    print(">> 1등 당첨")
elif(cnt == 5):
    print("5개 일치")
    print("")
    print(">> 2등 당첨")
elif(cnt == 4):
    print("4개 일치")
    print("")
    print(">> 3등 당첨")
elif(cnt == 3):
    print("3개 일치")
    print("")
    print(">> 4등 당첨")
else:
    print("다음 기회에")
print(computerlotto)
print(userlotto)