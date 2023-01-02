# Viết chương trình thực hiện xử lý 10 chiều cao
print("10 chiều cao đơn vị inch")
list3=[74,74,72,72,73,69,69,71,76,71]
print(list3)
print("Đổi inch sang m")
for i in list3:
    m=i*0.0254
    print(i," inch = ",m, "m")
print(list3)
# In ra 3 chiều cao đầu trong list
print("3 chiều cao đầu trong list là:",list3[0:3])
# In ra 3 chiều cao cuối trong list
print("3 chiều cao cuối trong list là:",list3[7:10])
# Tính chiều cao trung bình 
print("Chiều cao trung bình là:",sum(list3))
# tính chiều cao lớn, nhỏ nhất
print("Chiều cao lớn nhất là:",max(list3))
print("Chiều cao nhỏ nhất là:",min(list3))
# Sắp xếp list theo giá trị tăng dần
list3.sort()
print("Thứ tự tăng dần:",list3)
# Sắp xếp list theo giá trị tăng dần
list3.reverse()
print("Thứ tự giảm dần:",list3)
