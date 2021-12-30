import os.path
from pdf2image import convert_from_path

def getNameFromPath(path):
    return os.path.splitext(os.path.basename(path))[0]


def pngify(inputPath, outputPath):
    pil_image_lst = convert_from_path(inputPath) # This returns a list even for a 1 page pdf
    pil_image = pil_image_lst[0]
    img1 = pil_image.convert("RGB")
    img1.save(outputPath + f"\{getNameFromPath(inputPath)}.png")