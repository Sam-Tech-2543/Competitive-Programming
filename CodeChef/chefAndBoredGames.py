def chefAndBoredGames(n):
    c = 0
    for i in range(1, n + 1, 2):
        a = n - i + 1
        c += a * a

    print(c)


chefAndBoredGames(3)
chefAndBoredGames(8)
chefAndBoredGames(5)
