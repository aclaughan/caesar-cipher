import string
from art import logo


def caesar_cipher( text, shift, direction ):
    alphabet = list(string.printable)
    length = len(alphabet) - 1
    code = ""

    for char in text:
        x = alphabet.index(char)

        if direction == 'd':
            offset = x - shift
            if offset > length:
                offset += length + 1
        elif direction == 'e':
            offset = x + shift
            if offset > length:
                offset -= length + 1
        else:
            print("invalid direction")
            break

        new_char = alphabet[offset]
        code += new_char

    return (code)


def main():
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    direction = direction.lower()[:1]

    print(caesar_cipher(text, shift, direction))


if __name__ == '__main__':
    main()
