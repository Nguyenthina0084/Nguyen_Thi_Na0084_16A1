# Viết hàm trả về phần nguyên của phép chia hai số nguyên
def so_nguyen(x,y):
    a=x//y
    return a
x=int(input("Nhập số nguyên thứ nhất:"))
y=int(input("Nhập số nguyên thứ hai:"))
a=so_nguyen(x,y)
print("Số",x,"chia","Số",y,"trả về phần nguyên là:",a)