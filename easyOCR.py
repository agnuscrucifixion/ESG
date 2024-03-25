import os
from pdf2image import convert_from_path
import easyocr


def to_png(path):
    images = convert_from_path(path)

    for i, image in enumerate(images):
        image_path = f'C:/Users/TUF/Desktop/jpg/page{i}.jpg'
        image.save(image_path, 'JPEG')
        print(f'Saved image: {image_path}')


def process_images():
    reader = easyocr.Reader(['ru', 'en'], gpu=True)
    with open('output.txt', 'w', encoding='utf-8') as f:
        sorted_list = sorted(os.listdir('C:/Users/TUF/Desktop/jpg'), key=lambda x: int(x.split('.')[0][4:]))
        for filename in sorted_list:
            if filename.endswith('.jpg'):
                image_path = os.path.join('C:/Users/TUF/Desktop/jpg', filename)
                result = reader.readtext(image_path, detail=0, paragraph=True)
                print(image_path)
                for paragraph in result:
                    f.write(paragraph + '\n\n')
