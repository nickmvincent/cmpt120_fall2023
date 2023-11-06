import cmpt120image as img_module

img = img_module.getImage('./kid-green.jpg')
print(img[0][0])
print(img[0])

print(len(img))
print(len(img[0]))

# img_module.showImage(img, 'kid')

# img_module.showImage(img[0:250], 'top half')


img_module.showImage(img[250:], 'bottom half')
input("Press enter to quit")