def get_laptop_cost(laptops, budget):
    prices = sorted(set(laptops), reverse=True)

    if len(prices) >= 2:
        second_best = prices[1]
        if second_best <= budget:
            return second_best

    affordable = [p for p in prices if p <= budget]
    return max(affordable) if affordable else 0
