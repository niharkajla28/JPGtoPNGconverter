from PIL import Image, ImageFilter

# img = Image.open('pokedox/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("blur.png", 'png')
#
# filtered_img = img.filter(ImageFilter.CONTOUR)
# filtered_img.save("smooth.png", 'png')
#
# filtered_img = img.convert('L')
# rotated = filtered_img.rotate(90)
# resize = filtered_img.resize((50,50))
# box = (100, 100, 400, 400)
# cropped = img.crop(box)
# cropped.save("grey.png", 'png')

# filtered_img.show()
# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))

img = Image.open('pokedox/astro.jpg')
img.thumbnail((200,200))
img.save('thumbnail4.jpg')
print('done')