#1번 예제
class person:
    def introduce(self, name, age):
        self.name = name
        self.age = age
        print(f"안녕하세요, 저는 {self.name}이고, {self.age}살입니다.")


p = person()
p.introduce("현석", 20)

#2번 예제
class Dog:
    def __init__(self, name, breed = "믹스"):
        self.name = name
        self.breed = breed

    def info(self):
        print(f"강아지 이름: {self.name}, 품종: {self.breed}")

d1 = Dog("삐뽀")
d2 = Dog("하루", "시츄")

d1.info()
d2.info()

#3번 예제
class Car:
    wheel_count = 4


print(Car.wheel_count)

#4번 예제 
class Shape:
    def get_area(self):
        print("도형의 넓이를 계산할 수 없습니다.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


s = Shape()
s.get_area()

r = Rectangle(100, 200)
print(r.get_area())

#5번 예제 
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"이름: {self.name}, 점수: {self.score}")

students = [Student("홍길동", 90), Student("배현석", 80), Student("공하은", 100)]

for student in students:
    student.introduce()
