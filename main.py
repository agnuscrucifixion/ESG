import os
import requests


def main(url, path):
    print("Начинается обработка")
    files = {'file': open(path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        with open('final.txt', 'wb') as f:
            f.write(response.content)
            print("Text file downloaded successfully.")
            return True
    else:
        print("Failed to download text file.")
        return False


if __name__ == '__main__':
    print("Введите аргумент: ")
    argument = input()
    print("\n")
    while not main("http://localhost:5000/upload-pdf", argument):
        print("\n")
        print("Пожалуйста, введите корректный аргумент: ")
        argument = input()
        print("\n")

