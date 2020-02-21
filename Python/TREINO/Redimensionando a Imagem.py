from PIL import Image
img = Image.open('estrutura.jpeg')
new_img = img.resize((256,256))
new_img.save('estrutura256x256.jpeg','jpeg')