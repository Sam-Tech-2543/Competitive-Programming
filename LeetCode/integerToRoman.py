# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def __init__(self) -> None:
        self.hashMap={1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI",
                      7:"VII", 8:"VIII", 9:"IX", 10:"X", 50:"L", 100:"C",
                      500:"D", 1000:"M"}
        
        
    def getVal(self, num: int, digit: int) -> str:
        if num==0:
            return ""

        if num in self.hashMap:
            return self.hashMap[num]

        placeVal=10**(digit-1)

        if placeVal*9==num:
            return self.hashMap[placeVal]+self.hashMap[placeVal*10]
        if placeVal*4==num:
            return self.hashMap[placeVal]+self.hashMap[placeVal*5]
        
        if num>placeVal*5:
            ans=self.hashMap[placeVal*5]
            num-=placeVal*5
            for i in range(1,4):
                if i*placeVal==num:
                    ans+=self.hashMap[placeVal]*i
                    return ans
            return ans
        else:
            for i in range(1,4):
                if i*placeVal==num:
                    return self.hashMap[placeVal]*i


    def intToRoman(self, num: int) -> str:
        ans=""
        n=num
        lst=[]

        place=1
        digit=1
        while(n!=0):
            t1=(n%10)*place
            a=self.getVal(t1,digit)
            lst.append(a)

            n//=10
            place*=10
            digit+=1        
        
        return "".join(lst[::-1])
    
    


s=Solution()


# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones. 
print(s.intToRoman(3))

# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
print(s.intToRoman(58))

# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
print(s.intToRoman(1994))