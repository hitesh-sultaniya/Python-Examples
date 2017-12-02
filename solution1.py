def answer(data, n):
    return [x for x in data if x not in [y for y in set(data) if data.count(y) > n]]

