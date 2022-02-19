def likes(names):
    amount = len(names)
    if amount == 0:
        return 'no one likes this'
    elif amount == 1:
        return names[0] + ' likes this'
    elif amount == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif amount == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        return names[0] + ', ' + names[1] + ' and ' + str(len(names)-2) + ' others like this'
