# name = "홍길동"
# age = 17
# gender = "남"
# height = 170.521
# weight = 77.6758

# print("이름 :" + name)
# print("나이 :" + str(age))
# print("성별 :" + gender)
# print("키 :" + str(height))
# print("몸무게 :" +str(weight))

# print("이름 :%s" %name)
# print("나이 :%d"  %age)
# print("성별 :%c" %gender)
# print("키 :%.2f" %height)
# print("몸무게 :%.2f" %weight)

# print("키는 %.2f이고 몸무게는 %.2f 입니다" %(height, weight))

# print("이름 : {}" .format(name))
# print("나이: {}" .format(age))
# print("성별 : {}".format(gender))
# print("키 : {:.2f}" .format(height))
# print("몸무게 {:.2f}" .format(weight))
# print("키는 {:.2f}이고 몸무게는 {:.2f}입니다" .format(height, weight))

# print(f"이름 : {name}")
# print(f"나이 : {age}")
# print(f"성별 : {gender}")
# print(f"키 : {height:.2f}")
# print(f"몸무게 : {weight:.2f}")

# x = 10
# y = 20
# print("x ="+str(x))
# print("y ="+str(y))
# print("x+y={}" .format(x+y))

# year = 2005
# month = 1
# day = 1
# print("제 생일은 %d년 %d월 %d일입니다" %(year, month, day))
# print("제 나이는 %d살 입니다." %(2023-year))

# x = input()
# # print("출력결과 " +x )

# x = 10
# y = 3
# print("10 + 3 = " +str(x+y))
# print("10 - 3 = " +str(x-y))
# print("10 * 3 = " +str(x*y))

# 주민번호 = input("주민등록번호: ")
# if 주민번호[7] == "1" or 주민번호[7] == "3":
#     print("남자")
# else:
#     print("여자")

# i = 0
# while i < 5:
#  print(i)
#  i = i+1

# i = 0
# while i <=20:
#     if i % 2 == 0:
#         print(f"{i}", end = " ")
#     i = i + 1

# i = 0
# while i <= 20:
#     if i % 2 == 1:
#         print(f"{i}", end = " ")
#     i = i + 1    


# while True:
#     x = int(input("정수 입력 : "))
#     if(x == 0):
#         break
#     elif x%2==0:
#         print("짝수")
#     else:
#         print("홀수")
# print("\n종료")  

# print("--------------------------------------------")
# print("<< 비밀번호 맞추기>>")          
# print("--------------------------------------------")
# password = "19940115"
# cnt = 0
# while(1):
#         user=input("비밀번호 맞추기 : ")
#         if(user == password):
#                 cnt = cnt + 1
#                 break
#         else:
#                 print("잘못된 비밀번호입니다.")
#                 cnt = cnt +1

# print(f"{cnt}번 만에 성공!!")
# print("잠금해제")

# import random
# num = random.randrange(1,10)
# cnt = 0
# print("-----<<숫자 맞추기 프로그램>>-----")
# while(1):
#     user = int(input(">>1부터 10까지 숫자를 고르세요 : "))
#     if(user == num):
#         cnt = cnt +1
#         break
#     else:
#         if(user>num):
#                 print(f"{user} 보다 낮습니다")
#         else:
#              print(f"{user}보다 높습니다.")
#         cnt = cnt +1
# print("맞췄습니다!!")
# print(f"총 {cnt}번 만에 맞췄습니다.")


# print("메뉴판")
# print("---------------------")
# print()
# print("-비빔밥(7,500원)")
# print("- 제육볶음(8,500원)")
# print("-삼겹살(12,000)")
# print("-국밥(7,000)")
# print()
# while(1):
#     menu = input(">> 원하는 메뉴를 고르세요 : ")
#     if(menu == "비빔밥" or menu == "제육볶음" or menu == "삼겹살" or menu == "국밥"):
#         inbun = int(input("몇 인분 주문하시겠습니까? : "))
#         if(menu == "비빔밥"):
#                 print(f"선택한 메뉴는 비빔밥(으)로{7500*inbun}원입니다.")
#         elif(menu == "제육볶음"):
#                 print(f"선택한 메뉴는 제육볶음(으)로{8500*inbun}원입니다.")
#         elif(menu == "삼겹살"):
#                 print(f"선택한 메뉴는 삼겹살(으)로{12000*inbun}원입니다.")
#         elif(menu == "국밥"):
#                 print(f"선택한 메뉴는 국밥(으)로{7000*inbun}원입니다.")
#         else:
#                print("메뉴판에 없는 메뉴입니다.")
#                keep = input("계속 주문하시겠습니까?(yes/no):").lower()
#                if(keep != "yes"):
#                       print()
#                       print("---프로그램 종료---")
#                       break
ModelNumber1 = 0
ModelNumber2 = 0
ModelNumber3 = 0   

print("-------------------------------")
print("<<자동차 예약 프로그램>>")
print("-------------------------------")
while(1):
    user = input("자동차 모델을 선택하시겠습니까?(yes/no) : ").lower()
    if(user == "yes"):
        print("자동차 모델 번호 : 1        2       3")
        print(f"자동차 모델 현황 : {ModelNumber1}   {ModelNumber2}   {ModelNumber3} ")
        choose = input("자동차 모델 선택(1~3번 중 선택) : ")
        if(choose=="1"):
            if(ModelNumber1==1):
                print("이미 예약된 모델입니다.")
            else:
                ModelNumber1=ModelNumber1 + 1
        elif(choose=="2"):
            if(ModelNumber2==1):
                print("이미 예약된 모델입니다.")
            else:
               ModelNumber2=ModelNumber2 + 1
        elif(choose=="3"):
            if(ModelNumber3==1):
                print("이미 예약된 모델입니다.")
            else:
               ModelNumber3=ModelNumber3 + 1
        else:
            print("잘못 입력하셨습니다")
    elif(user == "no"):
        if(ModelNumber1 != 0 and ModelNumber2 == 0 and ModelNumber3 == 0):
            print("현재 예약된 모델 번호 : 1")
        elif(ModelNumber1 == 0 and ModelNumber2 != 0 and ModelNumber3 == 0):
            print("현재 예약된 모델 번호 : 2")
        elif(ModelNumber1 == 0 and ModelNumber2 == 0 and ModelNumber3 != 0):
            print("현재 예약된 모델 번호 : 3")
        elif(ModelNumber1 != 0 and ModelNumber2 != 0 and ModelNumber3 == 0):
            print("현재 예약된 모델 번호 : 1, 2")
        elif(ModelNumber1 != 0 and ModelNumber2 == 0 and ModelNumber3 != 0):
            print("현재 예약된 모델 번호 : 1, 3")
        elif(ModelNumber1 == 0 and ModelNumber2 != 0 and ModelNumber3 != 0):
            print("현재 예약된 모델 번호 : 2, 3")
        elif(ModelNumber1 != 0 and ModelNumber2 != 0 and ModelNumber3 != 0):
            print("현재 예약된 모델 번호 : 1, 2, 3")
        print("프로그램을 종료합니다...")
        break
    else:
        print("잘못된 입력입니다. yes나 no로만 답하세요.")
    