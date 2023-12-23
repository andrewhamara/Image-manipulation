def yellow_to_blue(image):
    image = image.convert('RGBA')
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            r, g, b, a = pixels[x, y]
            if r > 100 and g > 100 and b < 100:
                yellow_intensity = (r + g) // 2
                pixels[x, y] = (0, 0, yellow_intensity, a)
    image = image.convert('RGB')
    return image
