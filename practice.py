print(5) 
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*3+1)
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)
#참/거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

#애완동물을 소개해 주세요 ~
animal = "철부지인간" #문자형 자료는 따옴표 사용
name = "잼민이"
age = 20 #age는 정수형 자료니까 따옴표 없이 그냥 작성
hobby = "농구" 
is_adult = age >= 20 

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "산책" #위에서는 농구라고 hobby라는 변수를 선언했지만, 여기서는 산책을 선언했기 때문에 해당 문장으로부터 밑에 문장에서부터는 hobby가 농구가 아닌 산책으로 들어가게 될 것 
#print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요") #정수형은 +를 포함한 print문에서 쓰이기 위해서는 str로 감싸주어 정수형을 문자형으로 바꿔줌
print(name,  "는 " , age , "살이며, " , hobby , "를 아주 좋아해요") #+ 대신에 , 사용가능 -> str 없이 정수형 작성 가능 그 대신 , 사용하면 띄어쓰기 포함됨 (위 주석 문장과 비교)
print(name + "는 어른일까요? " + str(is_adult)) 
'''여러 문장들 주석 처리
해당 방식 잊지 말기
또한 여러문장을 커서로 잡고 command + / 하면 일괄 주석처리 가능''' 

station = "사당" 
print(station + "행 열차가 들어오고 있습니다")

station = "동인천"
print(station + "행 열차가 들어오고 있습니다") 

print(1+1)
print(3-1)
print(3*2)
print(6/3)
print(2**3) # 2^3 = 8 
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 나누었을때의 몫 = 1
print(10//3) # 3
print(10 > 3)
print(4>= 7)
print(10 < 3)
print(5 <= 5) # 같다 조건이 있기 때문에 True로 출력할 것

print(3 == 3) # 앞의 값과 뒤의 값이 똑같다라는 의미
print(4 == 2)
print(3 + 4 == 7)
print(1 != 3) # 1= 은 같지 않다 라는 의미
print(not(1 != 3)) # False \
print((3 > 0) and (3 < 5)) # and 조건문 -> 모두 만족해야 Ture로 출력됨
print((3 > 0) & (3 < 5)) # &은 and와 동일 
print((3 > 0) or (3 > 5)) # 앞은 참 그러나 뒤는 거짓. or 조건이면 둘 중 하나만 참이여도 True로 출력됨
print((3 > 0) | (3 > 5)) # or은 |로도 기능 가능
print(5 > 4 > 3) # 연속된 값도 출력 가능
print(5 > 4 > 7)

print(2 + 3 * 4)
print((2 + 3) * 4) 

number = 2 + 3 * 4 # 14
print(number) # 위에서 number를 연산을 통해 14로 할당시킴
number = number + 2 # 16
print(number) # 위에서 할당시킨 number를 또 다시 연산을 통해 새로 할당시켜서 출력시키면 16
number += 2 # 18
print(number) # 위 방식은 더 쉽게 하는 방식으로, number += x 로 코드를 입력하고 number를 출력하면 할당된 number에 x 란 값이 저장되서 출력됨
number *= 2 # 36
print(number) 
number /= 2 # 18
print(number) 
number -= 2
print(number) # 16 
number %= 5 # 1 
print(number) # 할당된 number값을 2로 나누었을때의 나머지를 구하는 것이므로 

# 파이썬에서 제공하는 숫자 처리 함수
print(abs(-5)) # abs함수(absolute)는 절댓값을 나타내주는 함수 
print(max(5, 12)) # 12 최댓값을 나타내는 함수
print(min(5, 12)) # 5 최솟값을 나타내는 함수
print(round(3.14)) # 3 반올림해주는 함수
print(round(4.99)) # 5 

#Python에서 제공하는 math library를 이용
from math import *
from re import M, X # math library 안에 있는 모든 것들을 이용하겠다는 말
print(floor(4.99)) # floor = 내림. 4
print(ceil(3.14)) # ceil = 올림. 4
print(sqrt(16)) #sqrt = 제곱근 구하기. 16은 4의 제곱근. 4

#랜덤함수 -> 랜덤, 즉 난수. 무작위로 숫자를 뽑아주는 것. Python에서 제공하는 random library를 사용할 수 있음. 
from random import *
print(random()) # 0.0이상 ~ 1.0미만의 임의의 값 생성
print(random() * 10) # 0.0이상 ~ 10.0미만의 임의의 값 생성 
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성. 소수점 뒤는 보고 싶지 않을떄 int 사용
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성. 

#로또값 출력해보기(1 ~ 45)
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성 
print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 값 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성. randint는 양 끝 수를 포함하여 랜덤출력

#퀴즈2
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+ str(date) +"일로 선정되었습니다")

#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2) 
sentence3 = """
나는 소년이고, 
파이썬은 쉬워요
"""
print(sentence3)

#슬라이싱
jumin = "030219-3623110"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #03은 두 자리임 -> 콜론을 이용하여 0번쨰 자리부터 2번째자리 직전까지 라고 해서 0:2. 
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지. 위와 동일.
print("뒤 7자리 : " + jumin[7:14])
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지. 위와 동일.
print("뒤 7자리 : " + jumin[-7:]) #맨 뒤 시작인 0이 -1이고, 맨 뒤에서 7번째인 3인 -7부터 끝까지

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 다 소문자로 출력해줌
print(python.upper())
print(python[0].isupper()) # python 의 첫 번째 문자가 대문자인가? True
print(len(python)) # python 의 문자열 길이를 세 줌
print(python.replace("Python" , "Java")) # 원하는 글자를 바꿈. Python을 Java로 바꿔줌

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 두 번쨰 n을 찾는 것
print(index)

print(python.find("n"))
print(python.find("Java")) # 원하는 단어가 변수 안에 포함되어있지 않을 경우 -1이 출력됨
#print(python.index("Java")) # index 를 이용하면 에러가 뜸. python 이라는 변수 안에는 Java라는 단어가 포함되지 x
print("hi") # 위에 index 를 사용해서 hi도 출력이 안 됨. 그러나 위 index 문장을 주석 처리 하면 hi 출력 됨.

print(python.count("n")) # n이 몇 번 등장하는지 세 줌

#문자열 포맷
print("a" + "b") # a 와 b 를 연속적으로 나열해 줌
print("a" , "b") # a 와 b 를 띄어쓰기와 함께 나열해 줌

#방법1
print("나는 %d살입니다." % 20) #d는 정수를 의미. % 뒤에 원하는 수를 넣으면 문장을 출력해 줌. d에는 정수값만 넣을 수 있음
print("나는 %s을 좋아해요." % "파이썬") # s는 string(문자열) 값을 넣겠다는 것. 
print("Appe 은 %c로 시작해요." % "A") # %c 는 character라서 한 글자만 받겠다는 것.
# %s를 사용하면 정수든 문자열이든 캐릭터든 다 사용할 수 있음
print("나는 %s살입니다." % 20)
print("Appe 은 %s로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란" , "빨간"))

#방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란" , "빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란" , "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란" , "빨간")) 

#방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))

#방법4 (v3.6 이상)
age = 20
color = "빨간색"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출문자
#print("백문이 불여일견 
#백견이 불여일타") # 오류가 남

# \n : 줄바꿈
#print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다 
#print("저는 "나도코딩"입니다.") # 큰따옴표 때문에 에러 발생
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.') 
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \ (하나의 역슬래쉬)
#print("C:\Users\Jaemin\MacbookAir\PythonWorkSpace>") # 역슬래쉬때문에 에러 남
print("C:\\Users\\Jaemin\\MacbookAir\\PythonWorkSpace>") # 역슬래쉬 2개 넣어주면 문장 내에서는 하나로 출력됨


# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple 출력됨

print("백문이 불여일견\n백견이 불여일타")
print("저는 '나도코딩'입니다")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")
# \" \' : 문장 내에서 따옴표

#\\ : 문장 내에서 \
print("C:\\Users\\Jaemin\\MacbookAir\\PythonWorkSpace>") 

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # PineApple 출력됨

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") # RedApple 출력됨

# \t : 탭
print("Red\tApple")

'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 +> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
# 예) 생성된 비밀번호 : nav51!
'''

url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
print(my_str)
my_str = my_str[:my_str.index(".")] # 규칙2
# my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # 정수이기 때문에 str로 감싸주어야 함
print("{0}의 비밀번호는 {1}입니다.".format(url, password)) 

# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # append를 하면 늘 맨 뒤에 붙도록 되어 있음
print(subway)

# 정형돈씨를 유재석씨와 조세호씨 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

'''print(subway.pop())
print(subway)

print(subway.pop())
print(subway)'''

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort() # 정렬한다는 뜻
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list) 

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = ["조세호" , 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

#사전
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) #cabinet에 5라는 키는 없음 (밑에 실습을 위해 주석 처리 해 둠)
print("hi") #프로그램이 꺼지는지 안 꺼지는지 보기 위해 hi 출력문을 작성해 봄 
#cabinet에 5라는 키가 없기 떄문에 프로그램이 꺼져버리고, 그 밑에 hi출력문을 작성하였기 때문에 당연히 hi도 출력되지 않음

print(cabinet.get(5))
print("hi") #get을 사용하면 none을 출력하고 프로그램도 꺼지지 않고 계속 출력 됨
# 결론 : 값에 없는 키를 대괄호를 통해 출력하면 오류를 출력하고 프로그램이 꺼져버리고 그 하단에 작성한 코드도 출력이 되지 않음. 그러나 get을 이용하면 값에 없는 키더라도 none을 출력하고 프로그램도 꺼지지 않고 계속 출력 됨

print(cabinet.get(5, "사용가능")) # 값에 없는 키를 출력하려고 시도했을때 none을 출력하지 않고 본인이 원하는 값을 출력할 수 있음(값에 있는 키라면 그냥 그대로 옳은 값이 출력이 됨)
print("hi")
# 위에서는 그냥 none으로 출력되는데, 여기서는 사용가능으로 출력됨 -> 5라는 키는 쓸 수 있다는 의미가 됨.

print(3 in cabinet) # True # 사전 자료형 안에 어떤 값이 있는지를 확인하는 방법
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"} # 위에서는 정수형을 통해서 키를 선언했는데,정수가 아닌 스트링으로도 가능
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet)
cabinet["A-3"] = "김종국" # 같은 키에 새로운 값을 업데이트 시킴
print(cabinet) 

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet) # 다 지워져서 빈 중괄호가 출력됨 

# 튜플
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") # 메뉴를 추가하고 실행시키면 오류 발생(값 추가, 변경 불가능. 정해진 값만 사용 가능)

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩") # 위의 것을 튜플을 이용하여
print(name, age, hobby)

# 세트 (set)(집합)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # 중복 허용 않기 때문에 1,2,3이라 출력됨

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 이렇게도 설정할 수 있음

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python)) # 둘 다 유재석 출력됨

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # |는 or 이라는 뜻 
print(java.union(python)) # uninon은 합집합을 의미함 (순서는 보장되지 않음)

# 차집합 (java 할 수 있지만 python 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java 를 잊었어요
java.remove("김태호")
print(java)

