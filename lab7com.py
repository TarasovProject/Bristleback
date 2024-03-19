import sys

def head(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()[:10]  # Читаем первые 10 строк из файла
            for line in lines:
                print(line, end='')  # Выводим строки на экран
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
    except IOError:
        print("Ошибка при чтении файла.")

def main():
    if len(sys.argv) != 2:
        print("Пожалуйста, укажите путь к файлу в качестве аргумента командной строки.")
    else:
        file_path = sys.argv[1]
        head(file_path)

if __name__ == "__main__":
    main()

print('kanan')
