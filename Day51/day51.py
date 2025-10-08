def send_message(route):
    speed = 300_000
    total_distance = sum(route)
    travel_time = total_distance / speed
    delay = (len(route) - 1) * 0.5
    total_time = travel_time + delay
    # Round to 4 decimals and strip trailing zeros
    return float(f"{total_time:.4f}".rstrip("0").rstrip("."))