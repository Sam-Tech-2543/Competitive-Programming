# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr):
    # Write your code here
    p,n,z=0,0,0
    for i in arr:
        if i>0:
            p+=1
        elif i==0:
            z+=1
        else:
            n+=1
    
    print(round(p/len(arr),6))
    print(round(n/len(arr),6))
    print(round(z/len(arr),6))
    