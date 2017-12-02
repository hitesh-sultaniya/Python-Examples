def str_len(stringInput):
    if type(stringInput) == int:
        return "Sorry integers don't have length"
    elif type(stringInput) == float:
        return "Sorry float don't have length"
    else:
        return len(stringInput)

print(str_len(10.6))
