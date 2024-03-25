import os
import easyOCR
import apryse

def clean_after():


def final_coupling(pathTextEasyOcr, pathText):






if __name__ == '__main__':
    apryse.convert_to_text("C:/Users/TUF/Desktop/pdf/ПАО «ММК» - Этот отчет распознавали разными библиотеками.pdf'")
    easyOCR.to_png('C:/Users/TUF/Desktop/pdf/ПАО «ММК» - Этот отчет распознавали разными библиотеками.pdf')
    easyOCR.process_images()
    final_coupling()
    clean_after()
