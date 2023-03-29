from PIL import Image


main_image = Image.open("pic.jpg")


watermark = Image.open("watermark.png")
watermark_width = int(main_image.width / 4)
watermark_height = int(watermark_width * watermark.height / watermark.width)
watermark = watermark.resize((watermark_width, watermark_height), Image.ANTIALIAS)


watermark_position = (main_image.width - watermark_width, main_image.height - watermark_height)


main_image.paste(watermark, watermark_position, watermark)


main_image.save("markedpic.jpg")
