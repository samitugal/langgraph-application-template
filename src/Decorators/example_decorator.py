def print_foo(func):
    def wrapper(*args, **kwargs):
        print("foo")
        return func(*args, **kwargs)
    return wrapper

