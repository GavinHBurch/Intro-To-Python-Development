from PIL import Image

image_cat = Image.open("cat.jpg")
image_desert = Image.open("desert.jpg")


pixels_desert = image_desert.load()
pixels_cat = image_cat.load()

print(image_desert.size)
print(image_cat.size)

comb_image = Image.new("RGB", image_desert.size)
(width, height) = image_desert.size
print(f"Width: {width}")
print(f"Height: {height}")
pixel_comb = comb_image.load()

print(pixels_desert[200, 100] )

for y in range(0, height):
    for x in range(0, width):
        (r,g,b) = pixels_cat[x, y]
        if g > 110 and r < 100 and b < 100:
            (r,g,b) = pixels_desert[x,y]
        pixel_comb[x,y] = (r,g,b)


comb_image.save("combimage.jpg")
comb_image.show()