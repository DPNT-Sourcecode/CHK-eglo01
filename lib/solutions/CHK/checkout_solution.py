

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) != str: return -1

    # define prices and offers
    prices = {"A": 50, "B": 30, "C": 20, "D": 15}
    x_for_y = {"A": {"units": 3, "price": 130}, "B": {"units": 2, "price": 45}}

    # handle offer logic
    def x_for_y_calculator(actual_units: int, offer_units: int, offer_price: int, regular_price: int):
        subtotal = 0
        while actual_units >= offer_units:
            actual_units -= offer_units
            subtotal += offer_price
        subtotal += (actual_units * regular_price)
        return subtotal

    # init result price
    total = 0
    deals = {"A": 0, "B": 0}

    # deal with stream of skus
    for sku in skus:
        if sku not in prices.keys():
            return -1
        if sku.islower():
            return -1
        if sku in x_for_y.keys():
            deals[sku] += 1
        else:
            total += prices[sku]
    for sku in deals.keys():
        total += x_for_y_calculator(deals[sku], x_for_y[sku]["units"], x_for_y[sku]["price"], prices[sku])
    
    return total