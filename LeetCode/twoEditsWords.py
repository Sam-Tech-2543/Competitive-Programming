#https://leetcode.com/contest/biweekly-contest-90/problems/words-within-two-edits-of-dictionary/


class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        lst=[]
        for i in queries:
            for j in dictionary:
                edit=0
                c=0
                for k in j:
                    if k!=i[c]:
                        edit+=1
                    c+=1
                if edit<=2:
                    if queries.count(i)>lst.count(i):
                        lst.append(i)
                    break

        return lst

    


#queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
#["word","note","wood"].
print(Solution.twoEditWords(["word","note","ants","wood"], ["wood","joke","moat"]))

#["t","i","m","i","p","s"]
#["w","j","b","p","u","b","u","i","h","m"]

#["t","i","m","i","p","s"]
print(Solution.twoEditWords(["t","i","m","i","p","s"], ["w","j","b","p","u","b","u","i","h","m"]))