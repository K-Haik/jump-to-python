# 1. 조건문 if 사용하기
# 다음 코드가 입력되었을 때 "성인입니다"가 출력되도록 조건문을 완성해보세요.
age = 20

if age >= 19:
    print("성인입니다.")
else:
    print("성인이 아닙니다.")


# 2. if / else
# 사용자의 나이를 입력받아 20세 이상이면 "성인입니다"
# 아니면 "청소년입니다"를 출력하는 프로그램을 만들어보세요.

age = int(input("사용자의 나이: "))

if age >= 20:
    print("성인입니다")
else: print("청소년입니다")


# 3. if / elif / else
# 점수를 입력받아 아래 기준에 따라 등급을 출력하세요:
# 90점 이상: A
# 80점 이상: B
# 70점 이상: C
# 그 외: F

score = int(input("점수: "))

if score >= 90: print("A")
elif score >= 80: print("B")
elif score >= 70: print("C")
else: print("F")


# 4. while문으로 1부터 5까지 출력하기
# 결과: 1 2 3 4 5

i = 1
while i in range(1, 6):
    print(i)
    i = i + 1


# 5. for문으로 리스트 순회
# 다음 리스트의 요소를 한 줄에 하나씩 출력하세요.

fruits = ["사과", "바나나", "포도", "수박"]
for fruit in fruits:
    print(fruit)
