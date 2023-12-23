from PIL import Image

def grayscale(path : str):
    image = Image.open(path)
    bw = image.convert('L')
    bw.save('black_and_white.jpg')
