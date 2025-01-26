while True:
    n = input()
    if n == '0':
        break

    n_l = len(n)
    for i in range(n_l//2):
        if n[i] != n[-i-1]:
            print("no")
            break
    else:
        print("yes")