#========================================================2장 

# 되새김문제 1번 ( 평균 점수 구하기 )
# 풀이 1
a=80
b=75
c=55
resultAvg1 = (a+b+c)/3
print("되새김문제 1번-풀이 1 평균 : ",resultAvg1)

# 풀이 2
a = [80,75,55]
total = 0
for i in a:
    total+=i
resultAvg2 = total / len(a)
print("되새김문제 1번-풀이 2 평균 : ",resultAvg2)

# 되새김문제 2번 ( 홀수, 짝수 판별하기 )
a=13
remainder =  a % 2
if remainder == 1 :
    print("되새김문제 2번 : 홀수")
else :
    print("되새김문제 2번 : 짝수")

# 되새김문제 3번 ( 주민등록번호 나누기 )
pin = "881120-1068234"
yyyymmdd = pin[0:6] 
num = pin[7:14]
print("되새김문제 3번 - 년월일 : ",yyyymmdd)
print("되새김문제 3번 - 숫자 : ",num)

# 되새김문제 4번 ( 주민등록번호 인덱싱 )
sex = pin[7]
print("되새김문제 4번 - 성별 : ",sex)

# 되새김문제 5번 ( 문자열 바꾸기 )
strA = "a:b:c:d"
strB = strA.replace(":","#")
print("되새김문제 5번 : ",strB)

# 되새김문제 6번 ( 리스트 역순 정렬하기 )
listA = [1, 3, 5, 4, 2]
listA.sort()
listA.reverse()
print("되새김문제 6번 reverse : ", listA)

# 되새김문제 7번 ( 리스트를 문자열로 만들기 )
listAA = ['Life','is','too','short']
result = " ".join(listAA)
print("되새김문제 7번 : ",result)

# 되새김문제 8번 ( 튜플 더하기 )
tpA = (1,2,3)
print("변경전 id : ",id(tpA))
tpA = tpA + (4,)
print("되새김문제 8번 : ",tpA)
print("변경후 id : ",id(tpA))

# 되새김문제 9번 (딕셔너리의 키)
dictA = dict()
#dictA['name'] = 'python'
#dictA[('dictA',)] = 'python'
#dictA[[1]] = 'python'
#dictA[250] = 'python'
print("dictA['name']: ", type('name')) #<class 'str'>
print("dictA[('dictA',)] : ",type(('dictA',))) #<class 'tuple'>
print("dictA[[1]] : ",type([1])) #<class 'list'>
print("dictA[250] : ",type(250)) #<class 'int'>
print (" 되새김문제 9번 : 딕셔너리의 키로 변하는 값을 사용할 수 없다. 그런데키로 사용된 dictA[[1]] 는 리스트 이므로 변하는 값이다.")
print (" 키로 사용되었던 나머지는 문자열, 튜플, 숫자는 변하지 않는 값이므로 딕셔너리 키로 사용가능하다.")

#  되새김문제 10번 ( 딕셔너리 값 추출 )
dA = {'A':90, 'B':80, 'C':70}
#result = dA.get('B')
result =  dA.pop('B')
print(dA)
print(" 되새김문제 10번 - 추출된 값 : ",result)

# 되새김문제 11번 ( 리스트에서 중복 제거 )
listB = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(listB)
listC = list(aSet)
print(" 되새김문제 11번 : ",listC)

# 되새김문제 12번 ( 파이썬 변수 )
varA = varB = [1,2,3]
varA[1] = 4
print(" 되새김문제 12번 - varA: ",varA)
print(" 되새김문제 12번 - varB: ",varB) # 둘 다 같은 리스트 객체를 바라보고 있기때문이다.


#========================================================3장

# 되새김문제 1번 ( 조건문의 참과 거짓 ) 
stringA = "Life is too short, you need python"

if "wife" in stringA: 
    print("되새김문제2 1번 : wife")
elif "python" in stringA and "you" not in stringA: 
    print("되새김문제2 1번 : python")
elif "shirt" not in stringA: 
    print("되새김문제2 1번 : shirt")
elif "need" in stringA: 
    print("되새김문제2 1번 : need")
else: 
    print("되새김문제2 1번 : none")

# 되새김문제 2번 ( 3의 배수의 합 구하기 )
result = 0
i = 1
while i <= 1000:
    if (i % 3) == 0 :
        result += i
    i += 1
print("되새김문제2 2번 :",result)

# 되새김문제 3번 ( 별 표시하기 )
print("되새김문제2 3번")
i = 0
while True:
    i += 1
    if i > 5:
        break
    print("*" * i)

# 되새김문제 4번 ( 1부터 100까지 출력 )
print("되새김문제2 4번")
for i in range(1,101):
    print(i)

# 되새김문제 5번 ( 평균 점수 구하기 )
classA = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in classA:
    total += score
average = total/len(classA)
print("되새김문제2 5번 : ",average)

# 되새김문제 6번 ( 리스트컴프리헨션 )
# 홀수만 골라 2를 곱한 값은 result 리스트에 담는 예제
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print("되새김문제2 6번 -1 : ",result)        
#-----------

numbers2 = [1,2,3,4,5]
result2 =[num * 2 for num in numbers2 if num % 2 == 1]
print("되새김문제2 6번 -2 : ",result2)
