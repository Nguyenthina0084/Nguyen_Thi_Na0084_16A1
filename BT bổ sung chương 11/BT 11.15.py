# Từ điển Anh-Việt
dic1={"Từ Anh":"Nghĩa Việt",
           "cat" : "con mèo",
           "dog" : "con chó",
           "ant" : "con kiến",
           "bear": "con gấu"}
# Hiển thị từ điển
for key in dic1:
    print(key,":",dic1[key])
# trong từ điển có bao nhiêu từ
print("Trong từ điển có:",len(dic1),"từ")

while True:
    print("Bạn muốn làm gì? 1: Xem từ điển, 2: Tra từ, 3: Thêm từ, 4: Xóa từ")
    a=int(input())
    if a==1:
        print("Dictionary:")
        for key in dic1:
            print(key,":",dic1[key])
# Tra từ tiếng anh trong từ điển
    if a==2:
        b=input("Nhập từ cần tra:")
        if b in dic1:
            print(b,"nghĩa là:",dic1[b])
            print("Dictionary:")
            for key in dic1:
                print(key,":",dic1[key])