def type_check(param_type):
    def decorator(func):
        def wrapper(param):
            if isinstance(param, param_type):
                return func(param)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
