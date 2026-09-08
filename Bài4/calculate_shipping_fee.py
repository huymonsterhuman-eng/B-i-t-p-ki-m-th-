def calculate_shipping_fee(total_amount, is_vip):
    if total_amount >= 1000000:
        if is_vip:
            return 0
        else:
            return 20000
    else:
        if is_vip:
            return 30000
        else:
            return 50000