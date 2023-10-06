from pyzbar.pyzbar import decode
from PIL import Image

#img = Image.open()

result = decode(img)
print(result)