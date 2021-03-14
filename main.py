data = open("data.txt", "wt", encoding='UTF8')
while True:
    txt = input("입력: ")
    if txt == "":
        data.close()
        break
    data.write( txt )
    data.write("\n")