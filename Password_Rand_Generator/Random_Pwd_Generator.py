def main():
    min_len, max_len = min_max()
    password_init(min_len, max_len)


def min_max():
    min_len = int(input("Enter minimum password length: "))
    max_len = int(input("Enter maximum password length: "))
    return min_len, max_len


def password_init(min_len, max_len):
    majuscule = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]
    minuscule = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
    nombre = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    speciaux = ["€", "£", "¥", "$", "%", "@", "/", "'", "\"", "!", "#", "&", "(", ")", "*", "+", ",", "-",
                ".", ":", ";", "<", "=", ">", "?", "[", "]", "^", "_", "`", "{", "|", "}", "~", "¡", "¢", "£",
                "¤", "¥", "¦", "§", "¨", "©", "ª", "«", "¬", "®", "¯", "°", "±", "²", "³", "´", "µ", "¶",
                "·", "¸", "¹", "º", "»", "¼", "½", "¾", "¿", "×", "÷"]

    charsets = [majuscule, minuscule, nombre, speciaux]

    print("Generating password list")

    with open("dict.csv", "a") as fichier:
        for length in range(min_len, max_len + 1):
            generate_passwords(fichier, length, charsets, min_len)


def generate_passwords(file, length, charsets, min_len):
    if length == 0:
        return

    generate_passwords_recursive(file, length, "", charsets, min_len)


def generate_passwords_recursive(file, length, current, charsets, min_len):
    if length == 0 and len(current) >= min_len:
        file.write(current + "\n")
        return

    for charset in charsets:
        for char in charset:
            generate_passwords_recursive(file, length - 1, current + char, charsets, min_len)


if __name__ == "__main__":
    main()
