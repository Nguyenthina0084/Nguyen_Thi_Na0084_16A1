from random import choice
print("Thực đơn món ăn hôm thứ nhất:")
meals_1=["Redneck Ribs", "Prawn Star","San Quentin Squid","First Full of Pizza","Honky Tonk Chicken"]
print(meals_1)
print("Thực đơn món ăn hôm thứ hai:")
meals_2=["Redneck Ribs","Prawn Star","Running Bear Salmon","Running Bear Salmon","Honky Tonk Chicken"]
print(meals_2)
choice_1=choice(meals_1)
choice_2=choice(meals_2)
print("Món ăn hôm đầu tiên:",choice_1)
print("Món ăn hôm thứ hai:",choice_2)
if choice_1 is choice_2:
    print("Bữa ăn nhàm chán :((")
else:
    print("Bữa ăn không nhàm chán :))")