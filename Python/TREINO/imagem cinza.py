from PIL import Image
im = Image.open("estrutura.jpeg").convert('L')
im.show()
im.save('estrutura02','jpeg')