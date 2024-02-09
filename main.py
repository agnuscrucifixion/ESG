import fitz
import cv2
import pytesseract
from PIL import Image
import numpy as np
import os


def process_all_pdfs(root_folder: str):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file).replace("\\","/")
                text_path = pdf_path.replace("pdfs", "txts").replace(".pdf", ".txt")
                reader = ImageReader(pdf_path)
                text = reader.process_pdf()
                with open(text_path, "w", encoding="utf-8") as text_file:
                    text_file.write(text)
                print(f"Text extracted from {pdf_path} and saved to {text_path}")


class ImageReader:
    def __init__(self, path_to_pdf: str):
        pytesseract.pytesseract.tesseract_cmd = r"V:/Tesseract-OCR/tesseract.exe"
        self.config = '--tessdata-dir "V:/Tesseract-OCRTesseract-OCR/tessdata" -l %s --oem %d --psm %d'
        self.path = path_to_pdf

    def correct_orientation(self, img: Image) -> np.ndarray:
        res = pytesseract.image_to_osd(img, output_type=pytesseract.Output.DICT)
        if res["orientation"] == 90:
            img = img.transpose(Image.ROTATE_90)
        elif res["orientation"] == 180:
            img = img.transpose(Image.ROTATE_180)
        elif res["orientation"] == 270:
            img = img.transpose(Image.ROTATE_270)
        return np.asarray(img)

    def preprocess(self, img: np.ndarray) -> np.ndarray:
        (height, width) = img.shape[:2]
        height, width = int(height * 5), int(width * 5)
        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.medianBlur(img, 3)
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        return img

    def noise_remove(self, img: np.ndarray) -> np.ndarray:
        img = cv2.bitwise_not(img)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        img = cv2.erode(img, kernel, iterations=1)
        img = cv2.dilate(img, kernel, iterations=1)
        return img

    def read_image(self, img: np.ndarray) -> str:
        return pytesseract.image_to_string(image=img, lang='rus+eng')

    def process_pdf(self):
        text = ""
        pdf_document = fitz.open(self.path)
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            try:
                img = self.correct_orientation(img)
            except:
                print("BLANK")

            img = self.preprocess(np.array(img))
            img = self.noise_remove(img)
            text += self.read_image(img)
            print(text)

        return text


if __name__ == '__main__':
    process_all_pdfs("V:/pdfs")
