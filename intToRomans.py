
# def 



# def ListingNums(num,NumList:list,divisor)->list[int]:
#     if num == 0:
#         return NumList
#     else:

#         reminder = num%divisor
#         num = (num//divisor)*divisor
#         divisor = divisor*10
#         NumList.append(reminder)
#         return ListingNums(num,NumList,divisor)

# emptyList = []
# print(ListingNums(3984,emptyList,10))

dictNum = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}

def romanPharsing(tup):

    num1 = tup[0]
    num2 = tup[1]

    if dictNum.get(num1*num2,None):
        return dictNum[num1*num2]
    elif num1 != 4 and num1 != 9:
        if num1>5:
            return dictNum[5*num2] + (num1-5)*dictNum[num2]
        return num1*dictNum[num2]
    elif (num1 == 4 or num1 == 9) and num2 == 100:
        return dictNum[num2] + dictNum[(num1*num2)+100]
    elif (num1 == 4 or num1 == 9) and num2 == 10:
        return dictNum[num2] + dictNum[(num1*num2)+10]
    elif (num1 == 4 or num1 == 9) and num2 == 1:
        return dictNum[num2] + dictNum[(num1*num2)+1]
    else:
        return ""
    




def ListingNums(num,divisor,res)->str:

    if divisor ==1:
        res = res + romanPharsing((int(num),int(divisor)))
        return res
    elif num//divisor == 0:
        divisor = divisor/10
        return ListingNums(num,divisor,res)
    else:
        q = int(num//divisor)
        resTup = (q,int(divisor))        
        res = res + romanPharsing(resTup)
        num = num%divisor
        if num == 0:
            return res
        return ListingNums(num,divisor/10,res)



for i in range(1,3999):
    print(ListingNums(i,1000,""))

# print(2000%1000)