import os
import easyOCR
import apryse
import util


def main(path):
    print("Начинается обработка")
    if not os.path.exists("temp"):
        os.mkdir("temp")
        os.mkdir("final")
        os.mkdir("temp/images")
        os.mkdir("temp/apryse_text")
        os.mkdir("temp/ocr_text")
    apryse.convert_to_text(path)
    easyOCR.to_png(path)
    easyOCR.process_images()
    util.final_coupling('final/ocr_text.txt', 'temp/apryse_text')
    util.clean_after()


if __name__ == '__main__':
    print("Введите аргумент: ")
    argument = input()
    print("\n")
    while not util.check_argument(argument):
        print("\n")
        print("Пожалуйста, введите корректный аргумент: ")
        argument = input()
        print("\n")

    print(f"Принятый аргумент: {argument}")
    print("\n")
    main(argument)
