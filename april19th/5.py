sum = 0
for i in range(1,11):
    if(i%2!=0):
        sum = sum - i
    else:
        sum = sum + i
print(f"sum : {sum}") 