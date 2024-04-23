

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) != str: return -1

    # define prices and offers
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}
    offers = [
        {"type": "x_for_y", "quantity": 5, "sku": "A", "offer_price": 200},
        {"type": "x_for_y", "quantity": 3, "sku": "A", "offer_price": 130},
        {"type": "buy_get_free", "quantity": 2, "buy_sku":"E", "get_sku":"B", "get_quantity": 1},
        {"type": "x_for_y", "quantity": 2, "sku": "B", "offer_price": 45},
        # we consider this new rule essentially a 3 for 2 rule, as all same type
        {"type": "x_for_y", "quantity": 3, "sku": "F", "offer_price": 20},
]
    
    def handle_offers(quants, offers):
        # handle offers in order of priority (init order)
        offer_total = 0
        for offer in offers:
            # deal with x for y offer
            if offer["type"] == "x_for_y":
                while quants[offer["sku"]] >= offer["quantity"]:
                    offer_total += offer["offer_price"]
                    quants[offer["sku"]] -= offer["quantity"]
            # deal with buy x get y free offer
            elif offer["type"] == "buy_get_free":
                max_free = (quants[offer["buy_sku"]] // offer["quantity"]) * offer["get_quantity"]
                if max_free > quants[offer["get_sku"]]:
                    quants[offer["get_sku"]] = 0
                else:
                    quants[offer["get_sku"]] -= max_free
        return offer_total, quants

    # init result price
    total = 0
    quants = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

    # deal with stream of skus
    for sku in skus:
        if sku not in prices.keys():
            return -1
        if sku.islower():
            return -1
        quants[sku] += 1
    offer_total, remaining = handle_offers(quants, offers)
    total += offer_total
    for sku in remaining:
        total += remaining[sku] * prices[sku]

    return total
