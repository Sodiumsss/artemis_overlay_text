import os
def getname(dir):
    for a, b, c in os.walk(dir):
        return c
Ntext = getname("./text")
Nreplace = getname("./replace")
if Ntext == Nreplace:
    print("将要对以下文件进行替换：")
    print(Ntext)
    print()
    if input("输入0结束，除此以外继续。") == "0":
        exit()
    for it in range(len(Ntext)):
        f1 = open("./text/"+Ntext[it], mode="r+", encoding="UTF-8")
        f2 = open("./replace/"+Ntext[it], mode="r+", encoding="UTF-8")
        mylist1 = []
        mylist2 = []
        tofind = "\t\t\t\t\t"
        for x in range(10000):
            buf1 = f1.readline()
            buf2 = f2.readline()
            if buf1.find(tofind) != -1:
                if buf1 != '\t\t\t\t\t{"rt2"},\n':
                    mylist1.append((buf1))
            if buf2.find(tofind) != -1:
                if buf2 != '\t\t\t\t\t{"rt2"},\n':
                    mylist2.append((buf2))
        # print(mylist1)#待替换文本
        # print(mylist2)#将要替换文本
        f3 = open("./new/"+Ntext[it], mode="w", encoding="UTF-8")
        f1.seek(0, 0)
        mainbuf = f1.read()
        for x in range(len(mylist2)):
            mainbuf = mainbuf.replace(mylist1[x], mylist2[x])
        f3.write(mainbuf)
        print("OK!")
        f1.close()
        f2.close()
        f3.close()

"""
print(mylist1)
print(mylist2)
f1.seek(pointer1[0]-len(mylist1[0].encode("utf-8")),0)
print(f1.read(len(mylist1[0])))
print("xxxx")
if len(pointer1)==len(pointer2):
    f1.seek(pointer1[0],0)
    f1.write(mylist2[0])
    print("change.")
"""
