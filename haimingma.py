def islegal(string):    #判断输入的字符是否合法
    return string.count('1') + string.count('0') == len(string)


def change(n):  # 十进制转二进制
    result = '0'
    if n == 0:  # 输入为0的情况
        return result
    else:
        result = change(n // 2)  # 调用自身
        return result + str(n % 2)


def smallest_check_number(k):     #计算需要的海明检验码的位数
    r = 1
    while 2 ** r - r - 1 < k:
        r += 1  # 得到最小检测位数
    return r


hammingList=input("请输入原码：")
if(islegal(hammingList)):

    hList = []
    for i in str(hammingList):
        hList.append(int(i))  # 将输入的海明码字符串转换为列表

    # print(smallest_check_number(len(hList)))
    for j in range(smallest_check_number(len(hList))):  # 插入海明检验码的位置
        hList.insert(2 ** j - 1, "a" + str(2 ** j - 1))
    # print("hList:", hList)

    List = []
    for a in range(len(hList)):
        b = change(a + 1).zfill(int(len(hList)))  # 位数不足补零
        blist = []
        for i in str(b):
            blist.append(int(i))      #将blist转换为列表
        List.append(blist)
        # print("blist" + str(a), blist)

    xorList = []          #定义异或列表
    for i in range(len(hList)-1):
      for index, binaryBitItem in enumerate(List):  # 同时访问数组下标 index
          if binaryBitItem[len(blist)-1-i] == 1:
            if isinstance(hList[index], int):
                xorList.append(hList[index])
            # print(binaryBitItem, hList[index])
      # print("xorList"+str(i)+":", xorList)
      result = 0
      for c in xorList:
        result = result ^ c      #blist里元素异或的值
        # print(result)
      if((hList[i]!=0)&(hList[i]!=1)):
        hList[i]=result
      xorList = []
    # print("List::::", List)
    # print(hList)
    ham=""
    for item in hList:     #列表转为字符串
        ham+=str(item)
    print(ham)
else:
    print("字符不合法！")



