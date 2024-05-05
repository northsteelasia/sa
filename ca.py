def analysis():

    l = []

    # May
    l.append(731) 
    l.append(731) 
    l.append(733)
    l.append(735)


    r = []

    l.sort()

    for x in l:
        if x in r:
            continue
        else:
            r.append(x)
            print(x, l.count(x))

    print(l)
    print(r)

