#리스트[안에 값이 다같지 않아도 됨]
#0:2= 0번부터 1번까지 출력됨 (2-1=1)
#시작이 0일 경우는 생략가능

#std = ["hello", "hi", "안녕",5]
#print(std[:2])#(0;2)

#index사용해서 값 가져오기

#std = ["hello", "hi", "안녕",5]
#print(std.index("안녕")

#len()= list길이 반환

#cafe = ["아메리카노","카페라떼","바닐라라떼","요거트"]
#print(len(cafe))

#데이터 추가
# 1. append() : list 맨 뒤에 값이 추가
# 2. insert() : 원하는 위치에 값이 추가

#cafe.append("프라푸치노")
#cafe.append("레몬에이드")
# print(cafe)

#cafe.insert(0,"에스프레소")
#cafe.insert(5,"블루베리요거트")
#print(cafe)


#데이터 할당(값 바꾸기)

#cafe[4] ="플레인요거트"
#print(cafe)

#데이터 삭제
# 1. del 명령 -> 인덱스로 제거
# 2.pop() -> 인덱스로 제거
# 3.remove() -> 값으로 제거

#del cafe[-1]
#print(cafe)

#cafe.pop(0)
#print(cafe)

#cafe.remove('바닐라라떼')
#print(cafe)

#리스트 안에 있는지 없는지 확인
#print("카페라떼"in cafe)#부정은 not in

# bakery=["스콘","케이크","샌드위치"]
# #print(len(bakery))

# bakery.insert(1,"약과")

# bakery.extend(["햄치즈 샌드위치, 에그샐러드 샌드위치, 닭가슴살 샌드위치"])

# bakery.remove("스콘")

# bakery[3]="불고기 샌드위치"
#print(bakery)

def add(a,b):
    result = a+b
    return result

add(10,3)
print (add)