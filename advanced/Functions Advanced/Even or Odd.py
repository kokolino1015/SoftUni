def even_odd(*args):
    searching = args[-1]
    res = []
    for i in range(len(args) - 1):
        if searching == "even" and args[i] % 2 == 0:
            res.append(args[i])
        elif searching == "odd" and args[i] % 2 != 0:
            res.append(args[i])
    return res
