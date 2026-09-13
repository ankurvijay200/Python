def calculate_total(prices):
    total = 0;
    for item in prices:
        total = total + item;
    return total

def apply_tax(amount):
    return amount + amount*0.05