def cakes(recipe, available):
    amount = []
    for i in recipe:
        if i in available:
            amount.append(available[i] // recipe[i])
        else:
            return 0
    return min(amount)
