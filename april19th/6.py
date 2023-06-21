user = int(input("정수입력 : "))
for i in range(2,user+1):
    if(user%i==0):
        break
    if(i==user):
        print(f"{user}는 소수")
    else:
        print(f"{user}는 소수가 아님")
