
mapNum = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

def recursiveLoop(number,res):

    currentNumber = number%10
    
    if number == 0:
        return res
    else:
        number = number//10
        StrTaken = mapNum[currentNumber]
        newRes = []
        for i in StrTaken:

            if len(res) == 0:
                newRes.append(i)
            else:
                for j in res:
                    k = i+j
                    print(k)
                    if k in newRes:
                        k = k[::-1]
                    print(k)
                    newRes.append(k)
        return recursiveLoop(number,newRes)

print(recursiveLoop(22,[]))
        


        