def caesar_cipher(text, key):
    """
    This function implements the Caesar Cipher algorithm.

    :param text: The text to be encrypted.
    :param key: The cipher key to shift the alphabet.
    :return: The encrypted text.
    """
    cipher_text = ""

    for char in text:
        # If the character is a letter, shift it by the key.
        if char.isalpha():
            ascii_val = ord(char)
            shifted_ascii_val = (ascii_val + key - 65) % 26 + 65
            cipher_text += chr(shifted_ascii_val)
        else:
            # If the character is not a letter, leave it as is.
            cipher_text += char

    return cipher_text

# Example usage
text = input("Enter the text to encrypt: ")
key = int(input("Enter the cipher key: "))

cipher_text = caesar_cipher(text, key)
print(f"The encrypted text is: {cipher_text}")





  
