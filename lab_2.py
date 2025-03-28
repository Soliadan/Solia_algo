def find_min_k(baskets, hours):
    if not (1 <= len(baskets) <= 10**4):
        raise ValueError("К-сть кошиків виходить за межі.")
    if not (1 <= hours <= 10**9):
        raise ValueError("К-сть годин виходить за межі.")
    if not all(1 <= bananas <= 10**9 for bananas in baskets):
        raise ValueError("К-сть бананів у кошику виходить за межі.")
    
    
    if len(baskets) > hours:
        raise ValueError("Недостатньо часу ")

    def required_hours(k):
        total_time = 0
        for bananas in baskets:
            total_time += (bananas + k - 1) // k  
        return total_time

    low, high = 1, max(baskets)

    while low < high:
        mid = (low + high) // 2
        if required_hours(mid) <= hours:
            high = mid
        else:
            low = mid + 1

    return low

print(find_min_k([3, 6, 7, 11], 8))   
print(find_min_k([30, 11, 23, 4, 20], 5))  
print(find_min_k([30, 11, 23, 4, 20], 6))  

print(find_min_k([3, 6, 7, 11], 8))  