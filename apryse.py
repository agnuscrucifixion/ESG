import os
import subprocess


def convert_to_text(path):
    apryse_text_dir = "temp/apryse_text"
    try:
        subprocess.run(["pdf2text", "-o", apryse_text_dir, path], check=True)
        print(f"Файл PDF успешно конвертирован в текст и сохранен в множество.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при конвертации файла PDF: {e}")
        return

    output_file_path = "final/apryse_text.txt"

    text_files = [f for f in os.listdir(apryse_text_dir) if os.path.isfile(os.path.join(apryse_text_dir, f))]
    print("Обрабатываем множество файлов и соединяем в один")
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for text_file in text_files:
            file_path = os.path.join(apryse_text_dir, text_file)
            with open(file_path, "r", encoding="utf-8") as input_file:
                output_file.write(input_file.read().strip() + "\n\n")

    print("Создан текстовый файл от Apryse")
