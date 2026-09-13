def apply_discount(price, percent):
    return int(price * 1/percent)

def flat_discount(price):
    if price > 50:
        return price - 50
    else:
        return price