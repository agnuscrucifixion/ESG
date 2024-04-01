import requests
import docker

#client = docker.from_env()


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
    #image = client.images.pull('agnusdecrucifixion/pdf_converter:prefinal')
    #container = client.containers.run('agnusdecrucifixion/pdf_converter:prefinal', ports={'5000/tcp': 5000}, detach=True)
    #print(container.id)
    print("Введите аргумент: ")
    argument = input()
    print("\n")
    while not main("http://localhost:5000/upload-pdf", argument):
        print("\n")
        print("Пожалуйста, введите корректный аргумент: ")
        argument = input()
        print("\n")

