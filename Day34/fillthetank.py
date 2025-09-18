def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    if fuel_level>tank_size:
        raise ValueError("fuel_level can't be greater than tank_size")
    elif fuel_level<0 or tank_size < 0 or price_per_gallon<0:
        raise ValueError("Inputs must be non-negative numbers")
    
    fuel_to_fill = tank_size-fuel_level
    total_cost = fuel_to_fill*price_per_gallon
    print(f"${total_cost:.2f}")
    return f"${total_cost:.2f}"

cost_to_fill(10, 15, 3.50)