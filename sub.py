from PIL import Image
import glob, os
import ImageChops
import math, operator
from PIL import ImageGrab

def pegaSub():
	im=ImageGrab.grab()
	im.save("../temp/temp.bmp", "bmp")
	im=ImageGrab.grab((520,315,760,450))
	im.save("../sub.bmp", "bmp")
	#im = im.crop((842,494,1073,626)) # Pega quadro de sub senha
	y = 14
	B = {}
	for i in range(3):
		x = 131
		for j in range(4):
			if j == 2:
				x -=1
			tmp = im.crop((x,y,x+19,y+19))
			tmp.save("../temp/"+str(i)+str(j)+".bmp", "bmp")
			B[str(i)+str(j)] = tmp
			x += 25
		y += 26
	return B 
	
def pegaNiv():
	im=ImageGrab.grab()
	im.save("../temp/temp.bmp", "bmp")
	im=ImageGrab.grab((12,42,57,55))
	im.save("../temp/temp2.bmp", "bmp")
	im = Image.open("../temp/temp2.bmp")
	return im

def verificaNivel():
	from time import sleep
	nivAtual =  pegaNiv()
	nivAtual.save("../temp/temp.bmp", "bmp")
	nivAtual = Image.open('../temp/temp.bmp')
	nivEspe = Image.open('../raw/lv6.bmp')
	print rmsdiff_2011(nivAtual,nivEspe)
	while not rmsdiff_2011(nivAtual,nivEspe) < 573:
		nivAtual =  pegaNiv()
		nivAtual.save("../temp/temp.bmp", "bmp")
		nivAtual = Image.open('../temp/temp.bmp')
		print 'ainda nao',rmsdiff_2011(nivAtual,nivEspe)
		sleep(1)
	
	
def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None
	

def rmsdiff_2011(im1, im2):
    "Calculate the root-mean-square difference between two images"
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value*(idx**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares/float(im1.size[0] * im1.size[1]))
    return rms
	

def demuxSub(A):
	B = {}
	C = {}
	for botao in A:
		A[botao].save("../temp/A" + botao+".bmp", "bmp")
	for infile in glob.glob("../raw/b*.bmp"):
		file, ext = os.path.splitext(infile)
		im = Image.open(infile)
		B[file[-1]] = im
	for infile in glob.glob("../temp/A*.bmp"):
		file, ext = os.path.splitext(infile)
		im = Image.open(infile)
		A[file[-2:]] = im
	for botao in A:
		i = 0
		if botao not in ('22','23'):
			print botao,i
			while not rmsdiff_2011(A[botao],B[str(i)]) < 577:
				print botao, i, rmsdiff_2011(A[botao],B[str(i)])
				i += 1 
			print botao, i, rmsdiff_2011(A[botao],B[str(i)])
			C[i] = botao
	
	return C

def verificaSub():
	im=ImageGrab.grab()
	im.save("../temp/print.bmp", "bmp")
	tmp=ImageGrab.grab((521,315,643,414))
	tmp.save("../temp/sub.bmp", "bmp")
	comSub = Image.open('../raw/sub.bmp')
	tmp =  rmsdiff_2011(tmp,comSub)
	print tmp
	if tmp < 577:
		print 'digita a sub'
		return 1
	