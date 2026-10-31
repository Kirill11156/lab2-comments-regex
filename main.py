"""Лаба 2, вариант 29 - поиск коментариев в программном коде."""

import re

# однострочные коментарии (# или //)
ANY_COMMENT = re.compile(r"#.*|//.*")


def is_comment(line):
    """Проверяет что строка целиком - коментарий."""
    s = line.strip()
    if not s:
        return False
    return bool(re.fullmatch(ANY_COMMENT, s))


def find_comments(text):
    """Ищет все коментарии, возвращает список (текст, номер строки)."""
    result = []
    for m in ANY_COMMENT.finditer(text):
        line_no = text.count("\n", 0, m.start()) + 1
        result.append((m.group(), line_no))
    return result


def read_file(path):
    """Читает файл, если не открылся - пустая строка."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def main():
    print("Лаба 2, вариант 29 - поиск коментариев в коде")
    print("1 - проверить строку (коментарий или нет)")
    print("2 - ввести код вручную")
    print("3 - загрузить код из файла")
    print("0 - выход")
    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        line = input("Введите строку: ")
        if is_comment(line):
            print("Да, это коментарий")
        else:
            print("Нет, это не коментарий")
    elif choice in ("2", "3"):
        if choice == "2":
            print("Вводите код, пустая строка - конец ввода:")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            text = "\n".join(lines)
            source = "ручной ввод"
        else:
            path = input("Путь к файлу: ").strip()
            text = read_file(path)
            source = path
            if not text:
                print("Файл не открылся или он пустой")
                return

        comments = find_comments(text)
        print(f"\nИсточник: {source}")
        if not comments:
            print("Коментарии не найдены")
        else:
            print(f"Найдено коментариев: {len(comments)}\n")
            for i, (t, line_no) in enumerate(comments, 1):
                t = t.replace("\n", "\\n")  # чтоб вывод не разъезжался
                print(f"{i}. [строка {line_no}] {t}")
    elif choice == "0":
        return
    else:
        print("Нет такого пункта")


if __name__ == "__main__":
    main()
