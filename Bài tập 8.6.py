a=int(input("Chọn xe 4 chỗ hoặc 7 chỗ:"))
b=float(input("Nhập số km:")) 
c=int(input("Nhập thời gian chờ:"))
if c<=5:
    c=0
if a==4:
    if b<=0.8:
        b*=11000
    if b<=20 and b>=0.8:
        b*=12100
    else:
        b=(b-20)*10000+242000
    if c>5:
        c=(c-5)*800
    print("Số tiền xe phải trả:", b+c, "VNĐ")
if a==7:
    if b<=0.8:
        b=13000
    if b<=30 and b>=0.8:
        b*=14100
    else:
        b=(b-30)*12000+423000
    if c>5:
        c=(c-5)*800
    print("Số tiền xe phả trả:",b+c, "VNĐ")
if a!=4 and a!=7:
    print("Không có xe nhé!")        
        