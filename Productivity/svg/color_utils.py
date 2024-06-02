# color_utils.py
def interpolate_color(start_color, end_color, factor: float):
    """Interpolate between two RGB colors."""
    return tuple([
        int(start_color[i] + (end_color[i] - start_color[i]) * factor)
        for i in range(3)
    ])

def rgb_to_hex(rgb):
    """Convert an RGB color to HEX format."""
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'
