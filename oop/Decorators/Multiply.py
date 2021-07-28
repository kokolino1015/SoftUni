def multiply(times):
    def decorate(func):
        def wrapper(params):
            return func(params) * times

        return wrapper

    return decorate
