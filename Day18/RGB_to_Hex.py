def rgb_to_hex(rgb):
    color=rgb.replace("rgb(", "").replace(")", "")
    values = [int(x.strip()) for x in color.split(",")]
    hex_values = [f"{v:02x}" for v in values]
    hex_color = "#" + "".join(hex_values)
    

    return hex_color


rgb_to_hex("rgb(255, 255, 255)")
rgb_to_hex("rgb(1, 11, 111)")