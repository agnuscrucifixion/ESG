import os
from pdf2image import convert_from_path
import easyocr
import nltk
from nltk.tokenize import sent_tokenize


nltk.download('punkt')


def split_into_sentences(text, language='russian'):
    sentences = sent_tokenize(text, language=language)
    return sentences


def format_paragraph(paragraph):
    sentences = split_into_sentences(paragraph, language='russian')
    formatted_paragraph = ' '.join(sentences)
    return formatted_paragraph


def to_png(name):
    images = convert_from_path(name)

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
                    formatted_paragraph = format_paragraph(paragraph)
                    f.write(formatted_paragraph + '\n\n')

if __name__ == '__main__':
    to_png('C:/Users/TUF/Desktop/pdf/ПАО «ММК» - Этот отчет распознавали разными библиотеками.pdf')
    process_images()
