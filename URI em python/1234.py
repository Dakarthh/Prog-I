while True:
    try:
        l2 = ""
        l1 = input()

        M = True

        for l in l1:
            if l == ' ':
                l2 += ' '
                continue
            if M:
                l2 += l.upper()
                M = False
            else:
                l2 += l.lower()
                M = True
        print(l2)
    except EOFError:
        break