while 1:
    next = input()
    if next == "0":
        break
    rev_next = ''.join(reversed(next))
    if next == rev_next:
        print("yes")
    else:
        print("no")
        