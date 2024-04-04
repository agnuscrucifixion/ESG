import requests
import docker
import os


# client = docker.from_env()

def before():
    if not os.path.exists("final"):
        os.mkdir("final")


def main(url, path):
    before()
    print("Начинается обработка")
    files = {'file': open(path, 'rb')}
    name_pdf = os.path.splitext(os.path.basename(path))[0]
    response = requests.post(url, files=files)
    if response.status_code == 200:
        with open(f'final/{name_pdf}.txt', 'wb') as f:
            f.write(response.content)
            print("Text file downloaded successfully.")
            requests.get("http://localhost:5000/clean")
            return False
    else:
        print("Failed to download text file.")
        return False


if __name__ == '__main__':
    # image = client.images.pull('agnusdecrucifixion/pdf_converter:prefinal')
    # container = client.containers.run('agnusdecrucifixion/pdf_converter:prefinal', ports={'5000/tcp': 5000}, detach=True)
    # print(container.id)
    print("Введите аргумент: ")
    argument = input()
    print("\n")
    while not main("http://localhost:5000/upload-pdf", argument):
        print("\n")
        print("Пожалуйста, введите ешё: ")
        argument = input()
        print("\n")
