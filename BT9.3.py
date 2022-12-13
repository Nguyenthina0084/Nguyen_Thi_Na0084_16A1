#Tính BMI
h=float(input("Nhập chiều cao của bạn:"))
w=float(input('Nhập cân nặng của bạn:'))
BMI=(w/(h*h))
print(BMI)
if BMI<18.5:
    print("Bạn gầy ")
elif BMI>18.5 and BMI<24.99:
    print("Bạn bình thuường")
else:
    print("Bạn thừa cân")