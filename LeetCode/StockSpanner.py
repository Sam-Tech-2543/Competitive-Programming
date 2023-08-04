# 901. Online Stock Span
# https://leetcode.com/problems/online-stock-span/?envType=study-plan-v2&envId=leetcode-75

class StockSpanner:
    # def solution(self,price):
    #     ans=[0]*(len(price))
    #     stack=[0]
    #     for i in range(1,len(price)):
    #         while stack:
    #             n=stack.pop()
    #             if price[n]>price[i]:
    #                 ans[i]=i-n
    #                 stack.append(n)
    #                 break
    #         stack.append(i)

    #     ans[0]=None
    #     return ans
    def __init__(self):
        self.stack=[(0,0)]
        self.i=1

    def next(self, price: int) -> int:
        ans=0

        while self.stack:
            n=self.stack.pop()
            if n[1]>price:
                ans=self.i-n[0]
                self.stack.append(n)
                break

        self.stack.append((self.i,price))
        self.i+=1
        print(self.stack,ans)

        return ans



# s=StockSpanner()
# print(s.solution([100,80,60,70,60,75,85]))

# stockSpanner = StockSpanner()
# stockSpanner.next(100)
# stockSpanner.next(80)
# stockSpanner.next(60)
# stockSpanner.next(70)
# stockSpanner.next(60)
# stockSpanner.next(75)
# stockSpanner.next(85)

# [[],[31],[41],[48],[59],[79]]
stockSpanner = StockSpanner()
stockSpanner.next(31)
stockSpanner.next(41)
stockSpanner.next(48)
stockSpanner.next(59)
stockSpanner.next(79)
