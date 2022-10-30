def bonAppetit(bill, k, b):
    # Write your code here
    a1=0
    for i in range(len(bill)):
        if i!=k:
            a1+=bill[i]
            
    if int(abs((a1/2)-b))==0:
        print("Bon Appetit")
    else:
        print(int(abs((a1/2)-b)))