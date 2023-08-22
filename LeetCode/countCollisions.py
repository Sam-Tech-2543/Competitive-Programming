class Solution:
    def countCollisions(self, directions: str) -> int:
        lst=[]
        ans=0

        for i in range(len(directions)):
            if directions[i]=="L":
                flag=1
                if lst:
                    t=lst[-1]
                    if t=="R":
                        ans+=2
                        flag=0
                    if t=="S":
                        ans+=1
                        flag=0
                if flag:
                    lst.append("L")
                else:
                    lst[-1]="S"
            elif directions[i]=="S":
                lst.append("S")
            else:
                flag=1
                if lst:
                    t=lst[-1]
                    if t=="S":
                        ans+=1
                        flag=0
                if flag:
                    lst.append("R")
                else:
                    lst[-1]="S"

        currCollisions=ans

        while currCollisions!=0:
            currCollisions=0
            directions=lst[::-1]
            lst=[]

            for i in range(len(directions)):
                if directions[i]=="L":
                    flag=1
                    if lst:
                        t=lst[-1]
                        if t=="R":
                            ans+=2
                            currCollisions+=2
                            flag=0
                        if t=="S":
                            ans+=1
                            currCollisions+=1
                            flag=0
                    if flag:
                        lst.append("L")
                    else:
                        lst[-1]="S"
                elif directions[i]=="S":
                    lst.append("S")
                else:
                    flag=1
                    if lst:
                        t=lst[-1]
                        if t=="S":
                            ans+=1
                            currCollisions+=1
                            flag=0
                    if flag:
                        lst.append("R")
                    else:
                        lst[-1]="S"

        return ans

s=Solution()

print(s.countCollisions("RSLLRSSL"))