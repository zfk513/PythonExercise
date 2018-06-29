from PIL import Image

def process(im, y1):
	copyBox1 = (205, y1-6, 545, y1)
	pasteBox1 = (205, y1-1, 545, y1+5)
	region1 = im.crop(copyBox1)
	im.paste(region1, pasteBox1)

if __name__ == '__main__':

	im = Image.open("screenshot.png")
	y = 648
	for i in range(0, 8):
		y = 648 + i * 12
		process(im, y)
	for i in range(8, 16):
		y = 649 + i * 12
		process(im, y)
	for i in range(16, 24):
		y = 650 + i * 12
		process(im, y)
	for i in range(24, 27):
		y = 651 + i * 12
		process(im, y)
	region = im.crop((205, 638, 545, 978))
	region.show()