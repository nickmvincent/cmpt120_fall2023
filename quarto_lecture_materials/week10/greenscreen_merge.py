import cmpt120image

def is_green(pixel, window=30):
    r, g, b = pixel
    return r < 0+window and g > 255-window and b < 0+window

img = cmpt120image.getImage('kid-green.jpg')
beach = cmpt120image.getImage('beach.jpg')

height = len(img)
width = len(img[0])


for window in [30, 50, 70, 90, 110, 130, 150]:
    for row in range(height):
        for col in range(width):
            pixel = img[row][col]
            if is_green(pixel, window):
                img[row][col] = beach[row][col]

    cmpt120image.showImage(img, 'Merged!')
    input('Press any key to continue')