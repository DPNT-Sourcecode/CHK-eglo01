

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) == list: return -1
    if type(skus) != str: return -1
    skus = skus.lower()

    # define prices and offers
    prices = {"a": 50, "b": 30, "c": 20, "d": 15}
    x_for_y = {"a": {"units": 3, "price": 130}, "b": {"units": 2, "price": 45}}

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
    deals = {"a": 0, "b": 0}

    # deal with stream of skus
    for sku in skus:
        if sku not in prices.keys():
            return -1
        if sku in x_for_y.keys():
            deals[sku] += 1
        else:
            total += prices[sku]
    for sku in deals.keys():
        total += x_for_y_calculator(deals[sku], x_for_y[sku]["units"], x_for_y[sku]["price"], prices[sku])
    
    return total
