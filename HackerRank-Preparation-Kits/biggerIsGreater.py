import string

def biggerIsGreater(w):
    alpha = string.ascii_lowercase
    w = [i for i in w]

    for i in range(len(w)-1,0,-1):
        ##print(f"{i=}")
        for j in range(i-1,-1,-1):
            ##print(f"{j=}")
            if w[i]>w[j]:
                #print("Higer=",w[i],i)
                #print("Lower=",w[j],j)

                w[j],w[i]=w[i],w[j]

                
                #print(w)
                #print(w[:j+1])
                #print(sorted(w[j+1:]))
                
                return "".join(w[:j+1]+sorted(w[j+1:]))
            
    return "no answer"


#print(biggerIsGreater("hefg"))
#print(biggerIsGreater("dkhc"))
print(biggerIsGreater("ab"))
print(biggerIsGreater("bb"))
print(biggerIsGreater("hefg"))
print(biggerIsGreater("dhck"))
print(biggerIsGreater("dkhc"))

print("----------------------")

print(biggerIsGreater("lmno"))
print(biggerIsGreater("dcba"))
print(biggerIsGreater("dcbb"))
print(biggerIsGreater("abdc"))
print(biggerIsGreater("abcd"))
print(biggerIsGreater("fedcbabcd"))

print(biggerIsGreater("zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw"))