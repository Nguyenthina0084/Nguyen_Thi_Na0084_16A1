x=int(input( "số KWh ="))
y="Số tiền điện là :"
z="nghìn VNĐ"
if x <= 50:
    print(y,(x*1.678),z)
elif 51<=x<=100:
    print(y,(x*1.734),z)
elif 101<=x<=200:
    print(y,(x*2.014),z)
elif 201<=x<=300:
    print(y,(x*2.536),z)
elif 301<=x<=400:
    print(y,(x*2.834),z)
else:
    print(y,(x*2.927),z)