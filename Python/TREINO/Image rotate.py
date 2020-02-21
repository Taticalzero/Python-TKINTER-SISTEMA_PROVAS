from PIL import Image
im = Image.open("estrutura.jpeg")
im.rotate(45).show()