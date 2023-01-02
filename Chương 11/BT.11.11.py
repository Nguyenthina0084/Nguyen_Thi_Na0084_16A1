# Tạo 1 tuple có 10 phần tử chuỗi bất kỳ
color=("red","green","yellow","blue","white","orange","pink","red","blue","violet")
# Nhập index dương và index âm
id1=int(input("Nhập số từ 1 đến 9:"))
id2=int(input("Nhập số từ -1 đến -9:"))
# Nhập chuỗi cần tìm s_find
s_find="blue"
# In tuple
print("Tuple có 10 chuỗi bất kì:"
      ,color)
# In giá trị của phần tử trong tuple có index dương và âm
print("Phần tử có trong index dương là:" ,color[id1])
print("Phần tử có trong index âm là:",color[id2])
# Tìm và đếm số lần xuất hiện của s_find
print("'blue' xuất hiện trong tuple",color.count(s_find),"lần")