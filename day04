# 1. 간단한 함수 정의
# 이름과 나이를 받아서 인사하는 함수를 만들어보세요.
# 예: greet("현석", 33) → "안녕하세요, 현석님! 33살이시군요."
import numbers


def greet(name, age):
    # 여기에 코드 작성
    return f"안녕하세요, {name}님! {age}살이시군요."

# 2. 기본값 인자 사용
# 취미를 묻는 함수인데, 취미를 입력하지 않으면 기본값으로 "독서"가 출력되게 해보세요.
# 예: hobby() → "당신의 취미는 독서입니다."

def hobby(name="사용자", interest="독서"):
# 여기에 코드 작성
    return f"{name}의 취미는 {interest}입니다."

a = hobby("현석", "운동")
print(a)

# 3. return vs print
# 두 수를 받아서 합을 return하는 함수와 print하는 함수를 각각 만들어보세요.
# 그 차이를 직접 출력해서 비교해보세요.

def add_return(a, b):
    # 여기에 코드 작성
    return a + b
print(add_return(3, 4))

def add_print(a, b):
    # 여기에 코드 작성
    print(a + b)

add_print(3, 4)

# 4. *args 사용하기
# 여러 개의 숫자를 받아서 총합을 구해주는 함수를 만들어보세요.
# 예: total(1, 2, 3, 4) → 10

def total(*numbers):
    # 여기에 코드 작성
    result = 0
    for i in numbers:
        result = result + i

    return result

a = total(3, 5, 6)
print(a)

# 5. 조건과 함수 결합
# 두 수 중 더 큰 수를 찾아 반환하는 함수를 작성하세요.
# 예: max_num(5, 3) → 5

def max_num(a, b):
    # 여기에 코드 작성
    if a > b:
        return a
    else:
        return b

print(max_num(21, 4))
