def xys(num, *args):
    print(num)
    print("....")
    print(args)

def xyz(num, **kwargs):
    print(num)
    print("....")
    print(kwargs)



xys(1, 2, 3, 4, 5)
xyz(1, 2, 3, 4, 5)