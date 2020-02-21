from PIL import Image
img = Image.open('estrutura.jpeg')
r,g,b = img.split()
len(r.histogram())
r.histogram()
img.show()
