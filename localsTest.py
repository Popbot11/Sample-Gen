def func(a, b, c, d):
    print(a+b+c+d)
args = [1, 2]
kwargs = {"c": 3, "d": 4}
func(*args, **kwargs)
