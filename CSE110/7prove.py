from PIL import Image

image_original = Image.open("cat.jpg")

width, height = image_original.size
pixels_original = image_original.load()
r, g, b = pixels_original[100, 200]
pixels_original[100, 200] = (r, g, b)


image_original.show()

image_original2 = Image.open("desert.jpg")

image_original2.show()

pixels_cat = image_original.load()

comb_image = (image_original + image_original2) 

for y in range(100, 500):
    for x in range(0, 300):
        (r, g, b) = pixels_cat[x, y]

        comb_image[x, y] = (r, g, b)

comb_image.save("...")
comb_image.show()