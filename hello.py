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
t1 = (1,2,'a', 'b')
#del t1[0] # 리스트의 경우에는 0번째 요소인 1이 삭제되어야 할 텐데, 튜플의 경우에는 오류 발생. 'tuple' object doesn't support item deletion -> 삭제하는 걸 지원하지 않는다. 
# 튜플은 리스트와는 다르게, 고정되어 있다.
print(t1[0]) # 인덱스 볼 수는 있음
print(t1[0:2]) # 슬라이싱도 가능. 그러나, t1 자체에는 변화 없음 




