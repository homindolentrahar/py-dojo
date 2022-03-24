import PIL.Image
import pilgram

image = PIL.Image.open("images/snk.jpg")

pilgram.css.saturate(image, 0.5).save('saturated.jpg')
pilgram.css.hue_rotate(image, 20).save("hue_rotated.jpg")
