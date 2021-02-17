def encode(text, key):
    return_string = ""
    text.lower()
    for letter in text:
        ancii_val = ord(letter)
        if ord('a') <= ancii_val <= ord('z'):
            ancii_val = ancii_val + key
            if ancii_val > ord('z'):
                ancii_val = ancii_val - 26
            elif ancii_val < ord('a'):
                ancii_val = ancii_val + 26
        return_string = return_string + (chr(ancii_val))
    return return_string


def main():
    text = input("Enter the text to encode : ")
    key = input("Enter the key to encode : ")
    key = int(key)
    print("Encoded string : ", encode(text, key))


if __name__ == '__main__':
    main()
