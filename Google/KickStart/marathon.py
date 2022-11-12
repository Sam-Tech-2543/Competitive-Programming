t = int(input())

for i in range(t):
    l, n = map(int, input().split())

    lst1 = []
    dist = 0
    extras = 0

    for j in range(n):
        s = input().split()
        d = int(s[0])
        c = str(s[1])

        if lst1 == []:
            lst1.append(c)
            dist += d
            extras = dist % l
        else:
            if lst1[0] == c:
                dist += d
                extras = dist % l
            else:
                lst1[0] = c

                if dist - extras + d >= l:
                    extras = dist % l
                    dist -= extras
                    dist += d - extras
                else:
                    dist -= d
                    extras = dist % l

    print(f"Case #{i+1}:", dist // l)
