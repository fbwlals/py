sum = 0
sum1 = 0
for i in range(0,101):
    if(i%2==0):
        sum = sum + i
    elif(i%2!=0):
        sum1 = sum1 + i
print(f"짝수합 : {sum}")
print(f"홀수합 : {sum1}")
    