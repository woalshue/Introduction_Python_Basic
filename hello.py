print("Hello, World!")

# 2-1 숫자형 
# 정수형
a = 1
print(a)
print(type(a))

# 실수형(. 포함된 것)
a = 1.24
print(a)
print(type(a))

# 컴퓨터식 지수 표현 방식
a = 4.24e10
print(a)
print(type(a))
a = 4.24e-10
print(a)
print(type(a))

# 사칙연산
a = 3
b = 4
print(a+b)
print(a*b)
print(a/b) # 나누기
print(type(a/b))
print(a//b) # 몫을 보여줌
print(a%b) # 나머지를 보여줌
print(a**b) # a의 b제곱 > 3의 4제곱 

# 문자열
a = "Hello World"
print(a)
print(type(a))
food = "Python's favorite food is perl"
print(food)
say = '"Python is very easy." he says.'
print(say)
a = 'Python\'s favorite food is perl'
print(a)
x = 'Life is too short\nYou need python' # 이스케이프 문자 \n 줄바꿈
print(x)
a = """Life is too short
You need python""" # """"""은 그냥 띄어도 인식함
print(x)

# 문자열 연산
a = "Python"
b = " is fun!"
print(a+b)
print(a * 100) # Python이란 글자를 100번 출력
print("=" * 50)

# 문자열 길이 구하기
a = "Life is too short"
print(len(a))
vlrn = 'You need python'
print(len(vlrn))

# 인덱싱
a = "Life is too short You need python"
print(a[0])
print(a[-1]) # n이 출력됨. -를 사용하면 역방향으로 셈 
print(a[-0]) # L이 출력됨. 0과 -0은 똑같은 것이기 때문에 똑같은 값을 보여줌

# 슬라이싱
a = "Life is too short, You need Python"
print(a[0:4])
a = "20010331Rainy"
print(a[:8])
print(a[8:])
a = "12345678"
print(a[::1]) # @이상부터 @미만까지 @간격으로
print(a[::2]) # 처음부터 끝까지 두 칸 간격으로
print(a[::3])
b = "12123425125"
print(b[::-2]) # 음수로 간격을 설정하면 거꾸로 간격 쳐서 출력함 
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b) # 이렇게 인덱싱으로 하나씩 뽑아서 출력해도 되지만 슬라이싱을 사용하자. 
print(a[:]) # 처음과 끝을 모두 생략하면 문자열의 처음부터 끝까지 모두 출력

# 20010331Rainy 를 연도/월일/날씨 세 부분으로 나눠라 !
a = "20010331Rainy"
Year = a[:4]
day = a[4:-5]
weather = a[-5:]
print(Year)
print(day)
print(weather)

# Pithon 를 Python 으로 수정하여라 ! 
a = "Pithon"
print(a[:1] + 'y' + a[-4:]) 

# 문자열 포매팅
a = "I eat %d apples." % 3
print(a) # I eat 3 apples. 가 출력됨. 따옴표를 여러 번 안 닫아줘도 돼서 사용하는 것. 
b = "I eat " + str(3) + " apples." 
print(b) # 마찬가지. 너무 작성하기 귀찮음. 
number = 10 
day = "three"
a = "I eat %d apples. so I was sick for %s days." % (number, day)
print(a)
number = 10 
day = "three"
a = "I eat %s apples. so I was sick for %s days." % (number, day) # %s 는 개사기템임. 정수든 실수든 문자열이든 다 쓸 수 있음. 
print(a)
a = "adafsd adfsfs fasdfdsafd {} afdfasfs".format("안녕") # {}로 안녕 이 들어감. 
print(a)
b = "asfdfs {age} afdsfsfsf {name} afsfdasd".format(name = "조설빈", age = 3)
print(b) 
name = "손재민"
a = f"나의 이름은 {name}입니다." # 뒤에 복잡하게 .format 할 것 없이 앞에 f 만 붙여주고 변수 설정해주면 더 편함. 
print(a)
a = "Error is %d%%." % 98 # %d와 %가 같은 문자열 안에 존재하는 경우, % 를 나타내려면 반드시 %%로 써야 한다. 
print(a)

# 정렬과 공백 
a = "%10s" % "hi"
print(a) # 8칸이 띄워진 후 hi가 출력됨. 
b = "%-10sjane." % "hi" 
print(b) # hi 좌측정렬 하고 8칸 띄고 jane 출력
c = "%-7smorning dude." % "Good"
print(c) # Good 좌측정렬 하고 3칸 띄고 morning dude. 출력

# 소수점 표현
a = "%f" % 3.421427472
print(a)
b = "%0.3f" % 3.42134567 # %간격.소수점 남기는 자리 수f ... %0.3f 는 소수점 세 번째까지 남긴다는 뜻 
print(b)
c = "%15.3f" % 3.42124567 # 전체 길이가 15인 문자열 공간에서 소수점 셋째자리까지만 남겨두고 우측정렬한다는 뜻
print(c)
q = "%-10.3f" % 3.09876543
print(q) # 반올림 적용 됨. 셋째자리까지 남기니 098을 7로 반올림해서 099가 됨. 
s = "%-13.5fWhat are you doing?" % 2.42134567
print(s) 

# format 함수를 사용한 포매팅
a = "I eat {0} apples".format(3)
print(a)
b = "I eat {0} apples".format("five")
print(b)
number = 3
a = "I eat {0} apples".format(number)
print(a)
number = 10 
day = "three"
x = "I ate {0} apples. So I was sick for {1} days.".format(number, day)
print(x)
y = "I ate {number} apples. So I was sick for {day} days.".format(number = 3, day = "five")
print(y)
a = "I ate {0} apples. So I was sick for {day} days.".format(3, day = 5)
print(a)
a = "{0:<10}".format("Hi") # 왼쪽 정렬
print(a)
b = "{0:>10}".format("hi") # 오른쪽 정렬
print(b)
c = "{0:^10}".format("hi") # 가운데 정렬
print(c)
d = "{0:=^10}".format("hi") # 공백 채우기. 가운데 정렬을 하되, hi 제외 나머지 8칸을 = 으로 채우기.(채워넣을 문자값은 정렬 문자 <,>,^ 바로 앞에 넣어야 함)
print(d)
e = "{0:!<10}".format("hi") # 왼쪽 정렬을 하되, hi 제외 나머지 8칸을 ! 으로 채우기. 
print(e) 
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{and}}".format()) # 문자열 포매팅 할 때 {}와 같은 중괄호 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우 {{}} 2개 연속 사용

# f 문자열 포매팅
name = '김나현'
age = 21
print(f"내가 좋아하는 사람의 이름은 {name}이고요, 그녀의 나이는 {age}살 입니다.")

year = 2022
age = 21
print(f"조설빈은 {year + 1}년에 {age + 1}살이 되었습니다.") # f 문자열 포매팅은 표현식을 지원 (표현식이란 문자열 안에서 변수와 +,-와 가타은 수식을 함께 사용하는 것.)

d = {'name':'손재민', 'age':21}
print(f"나의 이름은 {d['name']}입니다. 나의 나이는 {d['age']}살입니다.") # 딕셔너리 사용할 수 있음

d = {'language':"Python", 'language_2':"Java"}
print(f'제가 가장 좋아하는 언어는 {d["language"]}이고요, 앞으로 배우고자 하는 언어는 {d["language_2"]}입니다.') 

print(f'{"hi":<10}') # 10칸 중 좌측정렬
print(f'{"hi":>10}') # 10칸 중 우측정렬
print(f"{'hi':^10}") # 10칸 중 가운데 정렬
print(f'{"hi":=^10}') # 공백 채우기
print(f'{"hi":!<10}')

y = 3.42134234
print(f'{y:0.4f}') # 소수점 4자리까지 
print(f'{y:10.4f}') # 소수점 4자리까지 표현하고 10칸 중 우측정렬

print(f'{{and}}') # f 문자열에서 {}문자를 표시하려면 {{}} 두 개 동시에 사용

a = "%0.4f" % 3.42134234
print(a)
a = "%s" % ("good")
print(a)
a = "%10.3f" % 3.424738257
print(a)

# 문자열 관련 함수
a = "hobby"
print(a.count('b')) # a 변수에서 b의 개수를 돌려줌

a = "Python is the best choice"
print(a.find('b')) # 문자열에서 b 가 가장 먼저 나온 인덱스를 알려줌
print(a.find('x')) # x 는 문자열 속에 없기 때문에 -1이 출력됨. (없으면 -1 출력)

a = "Life is too short"
print(a.index('t')) # index 도 find 와 마찬가지로 문자열 중 찾는 문자가 처음 나온 위치를 반환한다. 
#print(a.index('k')) # index 는 find 함수와 다르게 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생한다. 

print(",".join('abcd')) # 문자열의 각각의 문자 사이에 ',' 를 삽입한다. 

print(",".join(["a", "b", "c", "d"]))
print("!".join(["a", "b", "c", "d"])) # join 함수의 입력으로 리스트를 사용하는 예

a = "hi"
print(a.upper()) # 소문자를 대문자로 바꾸어 주는 함수 

a = "HI"
print(a.lower()) # 대문자를 소문자로 바꾸어 주는 함수

a = "   hi     "
print(a.lstrip()) # 왼쪽 공백 지우기. 문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다. lstrip 에서 l은 left를 의미
print(a.rstrip()) # 오른쪽 공백 지우기. 
print(a.strip()) # 양쪽 공백 지우기.  

a = "Life is too short"
print(a.replace("Life", "Your leg")) # Life 를 Your leg 로 교체한다. 
print(a.split()) # 문자열 자료형이 있으면 띄어쓰기를 기준으로 잘라서 리스트를 만듬. 

a = "a:b:c:d"
print(a.split(":")) # ':' 표시 기준으로 쉼표가 찍히고 리스트가 만들어짐. 특정 문자를 split 함수에 넣으면 해당 문자를 기준으로 잘라서 리스트를 만들어 줌. 
my_str = "조선대학교/IT융합대학/컴퓨터공학과/딥러닝전공"
print(my_str.split("/"))

# 리스트 (=변수 여러 개를 묶는 역할)
a = ["이서영", "문재성", "int", "김정현"]
print(a)
print(a[1]) # 문재성 출력

a = [1,2,"int", "김정현", ["김재원", "Manse samdori"]] # 리스트 안에 숫자, 문자, 그리고 또 다른 리스트를 넣을 수 있음 
print(a[4])
print(a[4][1]) # 리스트 안의 값의 4번째에 위치한 또 다른 리스트 안에서의 1번째 값을 출력

a = [1,2,3] 
print(a[0] + a[2]) # 리스트 인덱싱
print(a[-1])

a = [1,2,3,4,5]
print(a[0:3]) # 리스트 슬라이싱

a = [1,2,3]
b = [4,5,6]
print(a + b) # 리스트 더하기 
print(a * 3) # 리스트 곱하기

a = ["박주하", "잠수", "문재성"]
a[0] = "한재성" # 리스트에서 하나의 값 수정하기 
print(a)
a[0:2] = ["김정현", "Stopmotion Man"] # 리스트에서 연속된 범위의 값 수정하기 
print(a)

a = ["박주하", "잠수", "문재성"]
a[0:2] = [] # 0부터 2 전까지 리스트 값을 빈 리스트로 수정 (문재성 만 남음)(삭제)
print(a)

a = ["박주하", "잠수", "문재성"]
del a[0] # del 을 사용하여 삭제도 가능
print(a)

a = list() # 비어있는 리스트는 이렇게 생성할 수도 있다
print(a)

a = [1,2,3]
#print(a[2] + "hi") 
# # 3hi 가 출력될 것 같지만, TypeError(형 오류) 발생. 3은 정수이고, "hi"는 문자열. 정수와 문자열은 당연히 서로 더할 수 없기 때문에 형 오류 발생
# 숫자와 문자열을 더해서 3hi 처럼 만들고 싶다면, 숫자 3을 문자 '3'으로 바꾸어 주어야 한다. 
print(str(a[2]) + "hi") # str함수는 정수나 실수를 문자열의 형태로 바꾸어 주는 파이썬의 내장함수이다. 

# 리스트 함수
a = ["박주하", "잠수", "문재성"]
a.append("시우버") # append 함수를 통해 마지막에 "시우버" 를 리스트에 추가
print(a)

a = ["박주하", "잠수", "문재성"]
a.sort() # 정렬 함수. 가나다,알파벳 순으로 정렬
print(a)

a = [1,5,3]
a.sort() # 숫자는 크기 순으로 정렬
print(a)

a = [1,5,3]
a.reverse() # 뒤집기 함수. 거꾸로 뒤집음
print(a)

a = [1,5,3]
print(a.index(5)) # 리스트 안에 5 가 있나 ? 있으니 5의 위치인 1을 출력

a = [1,5,3]
a.insert(0,4) # insert 함수는 append 함수와 다르게 구체적인 위치에 추가 가능. 0번째 인덱스에 4를 추가해라. 
print(a)

a = [1,5,3]
a.remove(1) # 리스트 안에 있는 1을 없애라. (remove 함수는 지우고자 하는 값을 입력해야 함. 인덱스를 입력하는 것이 아님.)
print(a)

a = [5,3,1,1,1,1,1]
a.remove(1) # 리스트 안에 지우고자 하는 값이 한 개가 아니라 여러개라면, 가장 앞에 있는 숫자 하나만 지워짐
print(a)

a = [1,5,3]
print(a.pop()) # 리스트 안의 값 중 가장 마지막에 있는 값을 꺼내버림
print(a) # pop 함수를 통해 마지막 값인 3을 꺼내버렸으니, a 리스트 안에는 1,5만 남아있음

a = [1,5,3,1,1]
print(a.count(1)) # 리스트 안에 있는 x의 개수를 세어줌

a = [1,5,3,1,1]
a.extend([2,3]) # 리스트를 넣을 수 있음(마지막에 들어감)
print(a)

a = [1,2,3]
a.append([5,6]) # 리스트에 다시 리스트를 추가
print(a)

'''a = [1,2,3]
print(a.index(0))''' # 값 오류 발생. 리스트 안에 0이 존재하지 않기 때문에 

a = [1,2,3]
print(a.pop(2)) # pop(x)는 리스트의 x번째 요소를 꺼내버림(3 꺼냄)
print(a) # 2번째 요소인 3을 꺼내서 a 리스트에서 지워버렸으니, a를 출력하면 [1,2]만 남게 됨

# 문제 1번 
국어 = 80
영어 = 75
수학 = 55
print(국어 + 영어 + 수학) # 210 
print(210/3) # 나눗셈 기호 / 를 사용해서 과목 수인 3으로 나누기. 평균점수 = 70

# 문제 1번 책 풀이
a = 80
b = 75
c = 55
print((a + b + c)/3)

# 문제 2번 책 풀이 (어려워서 혼자 못 풀음)
#자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해서 말해 보자.
print(1 % 2) # 1 출력. % 는 나눗셈 후 나머지를 반환하는 나머지 연산자
print(2 % 2) # 0 출력
print(3 % 2) # 1 출력
print(4 % 2) # 0 출력
# 아하 ! 자연수가 홀수일 때는 2로 나누면 1을 반환하고, 짝수일 때는 0을 반환
print(13 % 2) # 1 출력
# 자연수 13은 홀수이구나. 

# 문제 3번
pin = "881120-1068234"
yyyymmdd = "19" + pin[:2] + pin[2:6] # 문자열 슬라이싱 사용
num = pin[-7:]
print(yyyymmdd)
print(num)

# 문제 4번
pin = "881120-1068234"
print(pin[-7]) # 문자열 인덱싱 사용

# 문제 5번
a = "a:b:c:d"
b = a.replace(':', '#') # replace 함수 사용
print(b)

# 문제 6번
a = [1,3,5,4,2]
a.sort() # 리스트 내장함수 정렬함수 사용
print(a)
a.reverse() # 리스트 내장함수 순서뒤집기 함수 사용
print(a)

# 문제 7번 
a = ['Life', 'is', 'too', 'short']
result = " ".join(a) # a 리스트의 각 단어들을 한 문장으로 조립할 때 단어들 사이마다 공백을 넣어주어야 함. 1개의 공백문자 " " 를 사용하여 join
print(result)


# 튜플

# 리스트는 변경 가능 but 튜플은 변경 불가능
# t1 = (1, 2, 'a', 'b')
# del t1[0] -> 불가능. 리스트는 삭제할 수 있었는데, 튜플은 삭제도 불가능

# 인덱싱 하기 
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# 슬라이싱 하기
print(t1[1:]) # 1번째부터 끝까지

# 튜플 더하기
t2 = (3, 4)
print(t1 + t2)

# 튜플 곱하기
print(t2 * 3) # 튜플에서 곱하기는 곧 '반복'이다. 3을 곱하면 t2가 세 번 반복된다. 

# 튜플 길이 구하기
print(len(t1)) # t1의 길이를 구해서 출력

# 값 추가하기 ~ 
t3 = (1, 2, 'a', 'b')
print(t3 + (3,)) # t3 튜플에 3을 추가함 

# 튜플은 요솟값을 변경할 수 없기 때문에 sort, insert, remove, pop 과 같은 내장함수가 없다. 


# 딕셔너리 자료형
dic = {'name' : 'jaemin', 'phone' : '010-6449-1625', 'birth' : '0219'}

a = {1 : 'hi'} # key 로 정숫값 1, value 로 문자열 hi 를 사용함

b = {'a' : [1, 2, 3]} # value 에 리스트도 넣을 수 있다

# 딕셔너리 쌍 추가하기 
a = {1 : 'a'}
a[2] = 'b' # a 딕셔너리에 key가 2이고 value가 b인 딕셔너리 쌍을 추가
print(a)

a['name'] = 'pey'
print(a)

a[3] = [1, 2, 3] # 3인 key에 value로 리스트를 넣음
print(a)

# 딕셔너리 요소 삭제하기
del a[1]
print(a) # del a[key] 를 입력하면 key 에 해당하는 {key: value} 쌍이 삭제된다

a = {"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}
print(a)


# 딕셔너리에서 key를 사용해 value 얻기
grade = {'pey': 10, 'julliet': 90}
print(grade['pey']) # 'pey'라는 key의 value를 얻기 위해. 어떤 key 의 value 를 얻기 위해서는 딕셔너리변수이름[key] 를 사용해야 함. 

a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])
# 딕셔너리 변수에서 [] 안의 숫자 1은 두 번째 요소를 나타내는 것이 아니라 key에 해당하는 1을 나타낸다. 
# 딕셔너리는 리스트나 튜플에 있는 인덱싱 방법을 적용할 수 없다. 

my_dic = {'name': 'Jaemin', 'phone_number': '010-6449-1625', 'birth': '030219'}
print(my_dic['name'])
print(my_dic['phone_number'])
print(my_dic['birth'])

# 딕셔너리 만들 때 주의할 사항
a = {1 : 'a', 1: 'b'}
print(a)
# >>> {1: 'b} 가 출력된다.
# 딕셔너리에서 key는 고유한 값이므로 중복되는 key값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다는 점을 주의
# 동일한 key가 2개 존재할 경우, 1: 'a' 쌍이 무시된다.
# 즉, 딕셔너리에서는 동일한 key가 중복으로 존재할 수 없다.

# 또 한 가지 주의해야 할 점 : key에 리스트는 쓸 수 없다는 것. (하지만 튜플은 key로 쓸 수 있다.)
# 딕셔너리의 key로 쓸 수 있느냐, 없느냐는 key가 변하는 값인지, 변하지 않는 값인지에 달려 있다. 
# 리스트는 그 값이 변할 수 있기 때문에 key로 쓸 수 없다. 
# a = {[1,2]: 'hi'} # 리스트를 key로 설정하면 오류 발생.
# 단, value에는 변하는 값이든, 변하지 않는 값이든 아무 값이나 넣을 수 있다. 


# 딕셔너리 관련 함수 

# key 리스트 만들기 - keys
a = {'name': 'Jaemin', 'phone_number': '010-6449-1625', 'birth': '030219'}
print(a.keys()) # a.keys()는 딕셔너리 a의 key만을 모아 dict_keys 객체를 리턴한다.
# 만약 리턴값으로 리스트가 필요하다면, list(a.keys())를 사용하면 된다. (dict_keys 객체를 리스트로 변환)
print(list(a.keys()))

# dict_keys 객체 사용 (리스트를 사용하는 것과 별 차이는 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.)
for k in a.keys():
    print(k)

# value 리스트 만들기 - values
a = {'name': 'Jaemin', 'phone_number': '010-6449-1625', 'birth': '030219'}
print(a.values()) # value만 얻고 싶다면 values 함수 사용. 호출 시 dict_values 객체를 리턴

# key, value 쌍 얻기 - items
a = {'name': 'Jaemin', 'phone_number': '010-6449-1625', 'birth': '030219'}
print(a.items()) # items 함수는 key 와 value 의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴

# key: value 쌍 모두 지우기 - clear
a = {'name': 'Jaemin', 'phone_number': '010-6449-1625', 'birth': '030219'}
a.clear() 
print(a) # clear 함수는 딕셔너리 안의 모든 요소를 삭제. 빈 리스트를 [], 빈 튜플을 ()로 표현하는 것과 마찬가지로 빈 딕셔너리도 {}로 표현

# key 로 value 얻기 - get
a = {'name': 'Jaemin', 'phone_number': '010-6449-1625', 'birth': '030219'}
print(a.get('name'))
print(a.get('phone_number'))
# get(x) 함수는 x라는 key에 대응되는 value를 리턴. 
# a.get('name') 는 a['name'] 을 사용했을 때와 동일한 결과값을 리턴. 

a = {'name': 'Jaemin', 'phone_number': '010-6449-1625', 'birth': '030219'}
# print(a['nokey']) # a['nokey'] 방식을 사용하여 딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우 에러를 발생시킴
print(a.get('nokey')) # get 함수를 사용하여 딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우 None 을 리턴 (None 은 '거짓' 이라는 뜻이라고만 알아 두기.)
# 어떤 것을 사용할 것인지는 사용자의 선택. 

# 딕셔너리 안에 찾으려는 키가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는 get(x, '디폴트 값') 을 사용하면 편리.
print(a.get('nokey', 'Hello, Jaemin!')) # 딕셔너리 a 안에는 nokey 에 해당하는 키가 없으므로 설정해 둔 디폴트 값 Hello, Jaemin! 을 리턴

# 해당 key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name': 'Jaemin', 'phone_number': '010-6449-1625', 'birth': '030219'}
print('name' in a) # True 를 리턴
print('email' in a) # False 를 리턴 


# 집합 자료형 
s1 = set([1, 2, 3]) # 집합 자료형(set 자료형)
print(s1)
print(type(s1)) # <class 'set'>
 
s2 = {1, 2, 3} # 딕셔너리에서는 key가 꼭 있어야 했다면, 집합에서는 괄호 안에 키 - 밸류 없이 값들만 쭉 쓰면 그게 집합이 됨
print(s2)
print(type(s2))

s1 = set("Hello")
print(s1)
# 집합에는 순서가 딱히 없기 때문에 랜덤하게 출력됨.
# 집합에서 원소는 고유한 값이기 때문에 중복된 값들은 하나만 남고 제거됨
# print(s1[0]) # 순서가 없기 때문에 인덱스로 접근하는 것 불가능

s1 = set([1, 2, 3])
l1 = list(s1) # 굳이 값을 가져오고 싶다면 list로 형 변환을 해 주어야 함
print(l1[0])

s1 = set([1, 2, 3])
l1 = tuple(s1) # 튜플로도 형 변환 가능 
print(l1)

# 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2) # 교집합 {4, 5, 6} 이 출력됨
print(s1.intersection(s2)) # intersection 함수 사용 -> 집합1.intersection(집합2)를 사용히여 교집합 구하는 것도 가능

# 합집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 | s2) # 합집합 {1, 2, 3, 4, 5, 6, 7, 8, 9} 이 출력됨
print(s1.union(s2)) # union 함수 사용 -> 합집합 구할 수 있음

# 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 - s2) # 차집합 {1, 2, 3} 이 출력됨
# s1에서 s2를 빼는 것이므로, s1에서 s2와 중복된 것들을 뺴내고, s1에만 고유하게 존재하는 원소들을 뽑아내는 것
print(s2 - s1) # {8, 9, 7} 가 출력됨
print(s2.difference(s1)) # difference 함수 사용 -> 차집합 구할 수 있음

# 집합 자료형 관련 함수
# 값 1개 추가하기 - add (리스트에서는 append 였음)
s1 = set([1, 2, 3])
s1.add(4) # s1 집합에 4가 추가됨 (값을 한 개 추가)
print(s1) 

# s1.add([4, 5, 6]) -> 에러 발생. add는 원소 하나만 추가할 수 있는데, 리스트를 사용하여 여러 개를 추가하려고 하였기 때문


# 값 여러 개 추가하기 - update
s1 = set([1, 2, 3])
s1.update([4, 5, 6]) # s1 집합에 4, 5, 6이 추가됨 (값을 여러개 추가)
print(s1)

s2 = set([1, 2, 3])
s2.update([4, 4, 5, 6]) # 같은 원소를 중복하여 추가하려고 하면 중복은 제거되고 추가 됨 (리스트에서는 중복 모두 추가됨)
print(s2)

# 특정 값 제거하기 - remove
s1 = set([1, 2, 3])
s1.remove(2) # s1 집합 내에서 2 라는 원소를 제거
# 여기서 2가 인덱스가 아니라, 실제 제거하고자 하는 값임. 집합에는 인덱스가 없음
print(s1)

# 언제 집합을 많이 활용하느냐? 
l1 = [1, 2, 2, 3, 3, 3, 3, 4]
# l1 리스트를 계속 리스트로 활용하고 싶은데, 고유한 값 하나씩만 남기고 싶을 떄
s1 = list(set(l1)) # set 으로 l1을 감싸서 집합으로 형 변환을 시켜서 s1에 저장 -> 중복이 전부 제거됨 -> 다시 list로 감싸서 형 변환 
print(s1) # 리스트 [1, 2, 3, 4] 출력됨 


# 불 자료형
a = True # a = "True" 와 같이 string 으로 적은 것과는 다름 
print(a) # True 가 출력됨. 이것은 string "True" 와 다름
print(type(a)) # type 을 찍어 보면 bool 자료형이라 알려줌 (불리언)

a = False # False 도 마찬가지. 대신, 맨 앞이 대문자여야 함 (소문자 사용 시 에러 발생)
print(a)

a = 1 == 1 # 1과 1이 같니? -> True 
print(a) # True가 출력됨

a = 1 == 2
print(a) # False 출력됨
 
a = 1 < 2 
print(a) # True

# 자료형의 참과 거짓
a = [1, 2, 3, 4]
while a: # a 에 값이 있으므로 True -> 하나씩 날리다가 결국 a가 []이 되면 False 가 됨 ([]처럼 빈 상태는 False)
    print(a)
    a.pop() # pop 함수를 사용하여 끝 값을 하나씩 날림

if []:
    print("참")
else:
    print("거짓")
# 위 조건문을 실행시켜 보면 "거짓" 이 출력됨. [] 리스트 안이 비어있기 때문에 False 이므로

if [1, 2, 3]:
    print("참")
else:
    print("거짓")
# 위 조건문을 실행시키면 "참" 이 출력됨.

# 불 연산
a = bool([1, 2, 3]) # 값이 존재하는 리스트를 bool로 감싸주면 True 가 저장됨
print(a)


# 변수
a = [1, 2, 3]
print(id(a)) # id 함수는 주소를 보여줌

a = [1, 2, 3] # a 변수 = '1, 2, 3이 담겨있는 리스트'(객체) -> a 변수에는 해당 객체의 '주소'가 할당되는 것임
b = a # b 에 a 가 갖고 있는 주소를 동일하게 저당
print(id(a))
print(id(b))
# a와 b의 주소를 출력해 보았을 때 값은 동일하게 출력될 수 밖에 없음
print(a is b) # is 는 두 개의 주소가 같은지 판별하는 것 -> True 가 출력됨


