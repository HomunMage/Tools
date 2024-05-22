import svgwrite
from color_utils import interpolate_color, rgb_to_hex

def create_labeled_triangle(filename, image_size, num_layers, labels, start_color, end_color):
    dwg = svgwrite.Drawing(filename, size=(image_size, image_size), profile='tiny')

    # Calculate colors for each layer
    colors = [
        rgb_to_hex(interpolate_color(start_color, end_color, i / (num_layers - 1)))
        for i in range(num_layers)
    ]

    # Calculate the height of each layer
    layer_height = image_size / num_layers

    # Draw the layers from the bottom to the top with interpolated colors
    for i in range(num_layers):
        y1 = i * layer_height
        y2 = (i + 1) * layer_height
        layer_width_y1 = image_size * y1 / image_size
        layer_width_y2 = image_size * y2 / image_size

        points = [
            (image_size / 2 - layer_width_y1 / 2, y1),  # Left point y1
            (image_size / 2 + layer_width_y1 / 2, y1),  # Right point y1
            (image_size / 2 + layer_width_y2 / 2, y2),  # Right point y2
            (image_size / 2 - layer_width_y2 / 2, y2)   # Left point y2
        ]

        dwg.add(dwg.polygon(points=points, fill=colors[num_layers - i - 1], stroke='black'))

    # Draw the labels starting from the top downwards
    for i in range(num_layers):
        y1 = i * layer_height
        y2 = (i + 1) * layer_height
        text_position_y = (y1 + y2) / 2
        dwg.add(dwg.text(labels[i], insert=(image_size / 2, text_position_y), text_anchor="middle", font_size="15px", fill="black"))

    # Save the drawing
    dwg.save()

# Example usage:
image_size = 300
labels = ["$", "Definition", "Vision", "Design Pillars", "Systems", "Details"]
bottom_color = (0, 128, 255)
top_color = (255, 255, 0)
num_layers = len(labels)

create_labeled_triangle('labeled_triangle.svg', image_size, num_layers, labels, bottom_color, top_color)
