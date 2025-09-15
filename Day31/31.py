def adjust_thermostat(temp, target):
    if temp < target:
        return "heat"
    elif temp>target:
        return "cool"
    else:
        return "hold"


print(adjust_thermostat(68, 72))
print(adjust_thermostat(75, 72))
print(adjust_thermostat(72, 72))
print(adjust_thermostat(-20.5, -10.1))
print(adjust_thermostat(100, 99.9))
print(adjust_thermostat(0.0, 0.0))