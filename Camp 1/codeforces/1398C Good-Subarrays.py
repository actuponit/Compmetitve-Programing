for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    for i in range(len(a)):
        a[i] -= 1
    mp = {
        0: 1
    }
    count, s = 0, 0
    for i in range(len(a)):
        s += a[i]
        if s in mp:
            count += mp[s]
        mp[s] = mp.get(s, 0) + 1 
    print(count)