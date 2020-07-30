
def open_file(filename):
    try:
        f = open(filename,"r",encoding="utf-8")
    except:
        print("您输入的文件路径错误！")
        return 0
    else:
        return f


def close_file(filename):
    filename.close()


def compare(filename1,filename2):
    line=0
    index=0
    while True:
        str1=filename1.readline()
        str2=filename2.readline()
        line+=1
        if str1!="" or str2!="":
            if str1!=str2:
                if len(str1)>len(str2):
                    for i in range(len(str2)):
                        index+=1
                        if str1[i]!=str2[i]:
                          raise Exception("两个文件第一次出现不同在：{}行{}列".format(line,index))
                            return 0
                        else:
                            continue
                else:
                    for i in range(len(str1)):
                        index+=1
                        if str1[i]!=str2[i]:
                            print("两个文件第一次出现不同在：{}行{}列".format(line,index))
                            return 0
                        else:
                            continue
        elif str1=="" and str2=="":
            print("两个文件相同")
            break


if __name__ == '__main__':

    f1 = open_file('newresult')
    if f1==0:
        exit(0)
    else:
        f2 = open_file('oldresult')
    if f2==0:
        f1.close_file()
        exit(0)
    compare(f1,f2)
