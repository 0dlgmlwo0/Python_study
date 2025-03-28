# Hello World 출력
print("Hello, World!")

# 변수와 데이터 타입
name = "Alice"      # 문자열
age = 25            # 정수
height = 5.7        # 실수
is_student = True   # 불리언

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 조건문 예제
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

# 1부터 5까지 출력하는 반복문
for i in range(1, 6):
    print(i)

# 간단한 함수 예제
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 리스트 예제
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Orange")   # 리스트에 요소 추가

print(fruits)
print("First fruit:", fruits[0])
print("Total fruits:", len(fruits))

# 딕셔너리 예제
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person["name"])  # 키를 사용하여 값에 접근

# 파일 쓰기
with open("example.txt", "w") as file:
    file.write("Hello, this is a test.")

# 파일 읽기
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 리스트 컴프리헨션 예제
squares = [x**2 for x in range(1, 6)]
print(squares)

# 예외 처리 예제
try:
    num = int(input("Enter a number: "))
    print(f"Your number is {num}")
except ValueError:
    print("That's not a valid number!")
