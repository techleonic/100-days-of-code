import colorgram

colors = colorgram.extract('image.jpg',6)
list_colors = []
for color in colors :
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    list_colors.append(new_color)

print(list_colors)

