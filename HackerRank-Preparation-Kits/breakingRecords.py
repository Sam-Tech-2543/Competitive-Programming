def breakingRecords(scores):
    # Write your code here
    s1,s2=0,0
    j1=scores[0]
    j2=scores[0]
    for i in scores:
        if i>j1:
            s1+=1
            j1=i
        elif i<j2:
            s2+=1
            j2=i
    
    return [s1,s2]