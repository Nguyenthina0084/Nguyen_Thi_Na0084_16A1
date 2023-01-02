# Tìm thú trong vườn 
print("Danh sách động vật trong vườn thú:")
list_of_animals=["elephant","bear","cat","dog","fish","goat","parrot"]
# list
print(list_of_animals)
# Số lượng thú
print(len(list_of_animals))
# Tìm thú
find=list_of_animals
find=input("Nhập tên thú cần tìm:")
if find in list_of_animals:
    print(find,"có trong vườn thú")
else:
    print(find,"không có trong vườn thú")