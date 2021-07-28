def vowel_filter(func):
    def wrapper():
        res = func()
        return [let for let in res if let.lower() in 'aoeui']
    return wrapper
