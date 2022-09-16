from wand.image import Image
import sys
fin = input("Enter image file: ")
with open(fin,"rb") as f:
    image_blob=f.read()
    print("BLOB stored as: ",type(image_blob))
    print("Length of BLOB: ",len(image_blob))
    with Image(blob=image_blob) as img:
        print("Image size: ", img.height,"x",img.width)

f.close()
