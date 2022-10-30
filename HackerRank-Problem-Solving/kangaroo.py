def kangaroo(x1, v1, x2, v2):
    if v1>v2:
        a1,a2=x1,x2
        while (a1<=a2):
            a1+=v1
            a2+=v2
            if a1==a2:
                return "YES"
        if a1==a2:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"