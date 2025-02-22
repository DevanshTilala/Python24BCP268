def add_modify_delete():
    names=set()
    names.update(["AAA","BBB","CCC","DDD","EEE"])

    print(names)
    names.discard("AAA")
    names.add("LLL")
    print(names)
    names.discard("DDD")
    names.discard("BBB")
    print(names)
    # names.add("AAA")
    # names.add("BBB")
    # names.add("CCC")
    # names.add("DDD")
    # names.add("EEE")

    # print(names)
    # for i in names:
    #     names.add(modify_string(i))
    #     names.discard(i)
    #     break

    # print(names)

    
    
    # print(names)

add_modify_delete()