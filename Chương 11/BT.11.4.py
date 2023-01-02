lists=[]
while True:
    a=float(input("Nhập phần tử trong list:"))
    lists.append(a)
    if a==0:
        break
print("Tổng các phần tử trong list là:")
print(sum(lists))
print("Các phần tử trong list là:")
print(lists)
b=[]
x=float(input("Nhập số x:"))
max1=max(lists)
if x>max1:
    print(x,"lớn hơn tất cả các số trong list")
else:
    print(x,"không lớn hơn tất cả các số trong list")
if x in lists:
    print(x,"xuất hiện trong lists")
    print(x,"xuất hiện",lists.count(x),"trong list")
else:
    print(x,"không xuất hiện trong lists")
print(lists.count)
# x có lớn hơn các phần tử trong list
        