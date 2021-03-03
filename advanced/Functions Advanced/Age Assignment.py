def age_assignment(*args, **kwargs):
    res = {name: val for key, val in kwargs.items() for name in args if key in name}
    return res

