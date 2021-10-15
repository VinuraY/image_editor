# Created by Vinura Yashohara(AnonyMSAV) 
# 2021 - 10 - 14 18:29 p.m.
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import shutil
import platform

def rotate(value,image,copy):
	
	rotate_image = image.rotate(value)
	rotate_image.show()
	rotate_image.save(f'{copy}')

def crop(value,image,copy):
	
	crop_image = image.crop(value)
	crop_image.show()
	crop_image.save(f'{copy}')


def text(input_text,image,font,size,colour,copy):
	
	type_text = ImageDraw.Draw(image)
	type_text.text((0,0), input_text, font = font, fill = colour)
	image.show()
	image.save(f'{copy}')

def filters(value,image,copy):

	if(value == 1):
		print('''
			OPTIONS:

			1. Normal Blur
			2. MiniFilter
						''')
		
		select = int(input('Select : '))
		
		if(select == 1):
			effect = image.filter(ImageFilter.BLUR)
			effect.show()
			effect.save(f'{copy}')

		elif(select == 2):
			effect = image.filter(ImageFilter.MinFilter)
			effect.show()
			effect.save(f'{copy}')

		else:
			print('Error, Try Again')
			exit()

	elif(value == 2):
		
		effect = image.filter(ImageFilter.CONTOUR)
		effect.show()
		effect.save(f'{copy}')

	elif(value == 3):
		
		effect = image.filter(ImageFilter.DETAIL)
		effect.show()
		effect.save(f'{copy}')

	elif(value == 4):
		
		print('''
			OPTIONS:

			1. Edge Enhance (Normal)
			2. Edge Enhance (More)
						''')
		
		select = int(input('Select'))
		
		if(select == 1):
			
			effect = image.filter(ImageFilter.EDGE_ENHANCE)
			effect.show()
			effect.save(f'{copy}')

		elif(select == 2):
			
			effect = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
			effect.show()
			effect.save(f'{copy}')

		else:
			
			print('Error, Try Again')
			exit()

	elif(value == 5):
		
		effect = image.filter(ImageFilter.EMBOSS)
		effect.show()
		effect.save(f'{copy}')

	elif(value == 6):
		
		effect = image.filter(ImageFilter.FIND_EDGES)
		effect.show()
		effect.save(f'{copy}')

	elif(value == 7):

		print('''
			OPTIONS:

			1. Smoothing (Normal)
			2. Smoothing (More)
						''')
		
		select = int(input('Select'))
		
		if(select == 1):
			
			effect = image.filter(ImageFilter.SMOOTH)
			effect.show()
			effect.save(f'{copy}')

		elif(select == 2):
			
			effect = image.filter(ImageFilter.SMOOTH_MORE)
			effect.show()
			effect.save(f'{copy}')

		else:
			
			print('Error, Try Again')
			exit()

	elif(value == 8):
		
		effect = image.filter(ImageFilter.SHARPEN)
		effect.show()
		effect.save(f'{copy}')


def asci(image):

	width, height = image.size
	aspect_ratio = height / width
	new_width = 80
	new_height = aspect_ratio * new_width * 0.55
	image = image.resize((new_width, int(new_height)))
	image = image.convert('L')
	pixels = image.getdata()
	chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
	new_pixels = [chars[pixel // 25] for pixel in pixels]
	new_pixels = ''.join(new_pixels)
	new_pixels_count = len(new_pixels)
	ascii_image = [new_pixels[index:index + new_width]
	for index in range(0, new_pixels_count, new_width)]
	ascii_image = "\n".join(ascii_image)

	print(ascii_image)


def main(image,copy):

	
	print('''
		OPTIONS :

			1. Rotate Image
			2. Crop Image
			3. Type Text 
			4. Filters
			5. ASCII Art Generator 
			0. Exit ''')

	select = int(input('Select Option : '))

	
	if(select == 1):
		
		value = int(input('Degrees : '))
		rotate(value, image, copy)

	
	elif(select == 2):
		
		Left = int(input('Left : '))
		Right = int(input('Right : '))
		Upper = int(input('Upper : '))
		Lower = int(input('Lower : '))
		values = Left, Right, Upper, Lower
		crop(values, image, copy)

	
	elif(select == 3):
		
		input_text = input('Type here : ')
		font = input('Location of the font : ') # Location C:\Windows\Fonts\Font name folder\Font.tff
		size = int(input('Size of the text : '))
		colour = [1,2,3]

		for i in range(0,3):
			colour[i] = int(input(f'Colour (RGB value {i + 1}) : '))
		
		colour = tuple(colour)
		text(input_text, image, font, size, colour, copy)

	
	elif(select == 4):
		
		print('''
			OPTIONS : 

			1. Blur Filter
			2. Contour Filter
			3. Detail Filter
			4. Edge Enhancer (Normal, More)
			5. Find Edges
			6. Emboss Filter
			7. Smooth Filter (Normal, More)
			8. Sharpner
					  ''')

		select = int(input('Select Option : '))
		filters(select, image, copy)

	elif(select == 5):
		asci(image)

	elif(select == 0):
		print('Have a nice day!')
		exit()

	else:
		print('Error, Try again')
		exit()



print('''
		██████╗ ██╗ ██████╗██╗  ██╗ █████╗ 
		██╔══██╗██║██╔════╝╚██╗██╔╝██╔══██╗
		██████╔╝██║██║      ╚███╔╝ ███████║
		██╔═══╝ ██║██║      ██╔██╗ ██╔══██║
		██║     ██║╚██████╗██╔╝ ██╗██║  ██║
		╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                   
        Welcome To The CLI Image-Editor..

        Created by Vinura Yahohara (AnonyMSAV)

        ''')

os = platform.system() # To check OS type

if(os == 'Linux'):
	
	path = input('Path of the location image store : ') # Path of the image located eg: C:/User/Anony/Downloads
	name = input('Name of the image file : ') # Image name with extension eg: marple.jpg
	copy = f'{path}/copy.jpg' # Duplicate the real image to apply options.
	path = f'{path}/{name}'
	shutil.copyfile(path,copy)
	image = Image.open(copy)

	main(image,copy)

elif(os == 'Windows'):
	
	path = input('Path of the location image store : ') # Path of the image located eg: C:/User/Anony/Downloads
	name = input('Name of the image file : ') # Image name with extension eg: marple.jpg
	copy = f'{path}\\copy.jpg' # Duplicate the real image to apply options.
	path = f'{path}\\{name}'
	shutil.copyfile(path,copy)
	image = Image.open(copy)

	main(image,copy)
