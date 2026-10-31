import os
import shutil
import argparse


def copy_file(file_path, dist):
    try:
        extension = os.path.splitext(file_path)[1]

        if not extension:
            extension = "no_extension"
        else:
            extension = extension[1:]

        target_dir = os.path.join(dist, extension)
        os.makedirs(target_dir, exist_ok=True)
        filename = os.path.basename(file_path)
        target_path = os.path.join(target_dir, filename)
        shutil.copy2(file_path, target_path)
        print(f"Скопійовано: {filename}")

    except OSError as e:
        print(f"Помилка копіювання файлу {file_path}: {e}")


def read_directory(source, dist):
    try:
        for item in os.listdir(source):
            item_path = os.path.join(source, item)

            if os.path.isdir(item_path):
                read_directory(item_path, dist)

            elif os.path.isfile(item_path):
                copy_file(item_path, dist)

    except OSError as e:
        print(f"Помилка читання папки {source}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Рекурсивне сортування файлів за розширеннями")

    parser.add_argument("source", help="Вихідна директорія")
    parser.add_argument(
        "dist",
        nargs="?",
        default="dist",
        help="Директорія призначення"
    )

    args = parser.parse_args()
    source = os.path.abspath(args.source)
    dist = os.path.abspath(args.dist)

    if not os.path.isdir(source):
        print("Вихідна директорія не існує!")
        return

    if os.path.commonpath([source, dist]) == source:
        print("Директорія призначення не повинна бути всередині вихідної!")
        return

    os.makedirs(dist, exist_ok=True)
    read_directory(source, dist)


if __name__ == "__main__":
    main()
