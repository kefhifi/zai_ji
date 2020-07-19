def aaa(func):
    def bbb(*args, **kwargs):
        print("...")
        return func(*args, **kwargs)
    return bbb


h = 3


@aaa
def test(i):
    print("hello", "--")
    return i


c = test(h) 

print("===", c)


