import svgwrite

def interpolate_color(start_color, end_color, factor: float):
    """Interpolate between two RGB colors."""
    return tuple([
        int(start_color[i] + (end_color[i] - start_color[i]) * factor)
        for i in range(3)
    ])

def rgb_to_hex(rgb):
    """Convert an RGB color to HEX format."""
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

def create_concentric_circles(filename, image_size, num_circles, labels, start_color, end_color):
    dwg = svgwrite.Drawing(filename, size=(image_size, image_size), profile='tiny')

    # Calculate the center of the circles
    center = (image_size / 2, image_size / 2)

    # Calculate the radius step based on the number of circles
    radius_step = image_size / (2 * num_circles)

    # Calculate colors for each circle
    colors = [
        rgb_to_hex(interpolate_color(start_color, end_color, i / (num_circles - 1)))
        for i in range(num_circles)
    ]

    # Draw the circles from the outside to the inside with interpolated colors
    for i in range(num_circles, 0, -1):
        radius = radius_step * i
        dwg.add(dwg.circle(center=center, r=radius, fill=colors[i-1], stroke='none'))

    # Draw the labels starting from the center downwards
    for i in range(num_circles):
        radius = radius_step * i
        text_position_y = center[1] + radius_step * (i + 0.5)
        dwg.add(dwg.text(labels[i], insert=(center[0], text_position_y), text_anchor="middle", font_size="15px", fill="black"))

    # Save the drawing
    dwg.save()

# Example usage:
image_size = 400
labels = ["$", "Definition", "Vision", "Design Pillars", "Systems", "Implementation"]
start_color = (255, 255, 0)  
end_color = (0, 128, 255)
num_circles = len(labels)

create_concentric_circles('concentric_circles.svg', image_size, num_circles, labels, start_color, end_color)
