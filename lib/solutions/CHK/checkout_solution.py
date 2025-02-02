

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if type(skus) != str: return -1

    # define prices and offers
    prices = {
        "A": 50, 
        "B": 30, 
        "C": 20, 
        "D": 15, 
        "E": 40, 
        "F": 10, 
        "G": 20, 
        "H": 10, 
        "I": 35, 
        "J": 60, 
        "K": 70, 
        "L": 90,
        "M": 15, 
        "N": 40, 
        "O": 10, 
        "P": 50, 
        "Q": 30, 
        "R": 50, 
        "S": 20, 
        "T": 20, 
        "U": 40, 
        "V": 50, 
        "W": 20, 
        "X": 17, 
        "Y": 20, 
        "Z": 21
        }
    quants = {
                "A": 0, 
        "B": 0, 
        "C": 0, 
        "D": 0, 
        "E": 0, 
        "F": 0, 
        "G": 0, 
        "H": 0, 
        "I": 0, 
        "J": 0, 
        "K": 0, 
        "L": 0,
        "M": 0, 
        "N": 0, 
        "O": 0, 
        "P": 0, 
        "Q": 0, 
        "R": 0, 
        "S": 0, 
        "T": 0, 
        "U": 0, 
        "V": 0, 
        "W": 0, 
        "X": 0, 
        "Y": 0, 
        "Z": 0
    }
    offers = [
        {"type": "x_for_y", "quantity": 5, "sku": "A", "offer_price": 200},
        {"type": "x_for_y", "quantity": 3, "sku": "A", "offer_price": 130},
        {"type": "buy_get_free", "quantity": 2, "buy_sku":"E", "get_sku":"B", "get_quantity": 1},
        {"type": "x_for_y", "quantity": 2, "sku": "B", "offer_price": 45},
        {"type": "x_for_y", "quantity": 3, "sku": "F", "offer_price": 20},
        {"type": "x_for_y", "quantity": 10, "sku": "H", "offer_price": 80},
        {"type": "x_for_y", "quantity": 5, "sku": "H", "offer_price": 45},
        {"type": "x_for_y", "quantity": 2, "sku": "K", "offer_price": 120},
        {"type": "buy_get_free", "quantity": 3, "buy_sku":"N", "get_sku":"M", "get_quantity": 1},
        {"type": "x_for_y", "quantity": 5, "sku": "P", "offer_price": 200},
        {"type": "buy_get_free", "quantity": 3, "buy_sku":"R", "get_sku":"Q", "get_quantity": 1},
        {"type": "x_for_y", "quantity": 3, "sku": "Q", "offer_price": 80},
        {"type": "x_for_y", "quantity": 4, "sku": "U", "offer_price": 120},
        {"type": "x_for_y", "quantity": 3, "sku": "V", "offer_price": 130},
        {"type": "x_for_y", "quantity": 2, "sku": "V", "offer_price": 90},
        {"type": "group_discount", "group": ["S", "T", "X", "Y", "Z"], "units": 3, "price": 45}
]
    
    def can_take_group_discount(quants, group_members, units):
        group_units = 0
        for member in group_members:
            group_units += quants[member]
            if group_units >= units:
                return True
        return group_units >= units

    def get_group_quants(quants, group_members):
        group_quants = {}
        for group_member in group_members:
            group_quants[group_member] = quants[group_member]
        return group_quants
    
    def get_group_prices(prices, group_members):
        group_prices = {}
        for group_member in group_members:
            group_prices[group_member] = prices[group_member]
        return group_prices

    def take_most_expensive_from_group(quants, units, group_quants, group_prices):
        sorted_prices = dict(sorted(group_prices.items(), key=lambda key_val: key_val[1]))
        while units > 0:
            for member in sorted_prices.keys().__reversed__():                
                if group_quants[member] > 0:
                    if group_quants[member] > units:
                        group_quants[member] -= units
                        quants[member] -= units
                        units = 0                        
                    else:
                        units -= group_quants[member]
                        group_quants[member] = 0
                        quants[member] = 0
        return quants

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
            elif offer["type"] == "group_discount":
                while can_take_group_discount(quants, offer["group"], offer["units"]):
                    group_quants = get_group_quants(quants, offer["group"])
                    group_prices = get_group_prices(prices, offer["group"])
                    quants = take_most_expensive_from_group(quants, offer["units"], group_quants, group_prices)
                    offer_total += offer["price"]

        return offer_total, quants

    # init result price
    total = 0

    # deal with stream of skus
    for sku in skus:
        if sku not in prices.keys():
            return -1
        if sku.islower():
            return -1
        if sku not in quants.keys():
            quants[sku] = 0
        quants[sku] += 1
    offer_total, remaining = handle_offers(quants, offers)
    total += offer_total
    for sku in remaining:
        total += remaining[sku] * prices[sku]

    return total

