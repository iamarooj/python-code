# Caesar Cipher Implementation
# Lab Assignment 1 - Information Security

def caesar_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        # Check if character is uppercase letter
        if char.isupper():
            # Shift within range A-Z
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char

        # Check if character is lowercase letter
        elif char.islower():
            # Shift within range a-z
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += encrypted_char

        else:
            # Keep spaces and special characters unchanged
            encrypted_text += char

    return encrypted_text


def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        # Check if character is uppercase letter
        if char.isupper():
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char

        # Check if character is lowercase letter
        elif char.islower():
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decrypted_text += decrypted_char

        else:
            # Keep spaces and special characters unchanged
            decrypted_text += char

    return decrypted_text


# Main Program
message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift_value)
print("Encrypted Message:", encrypted)

decrypted = caesar_decrypt(encrypted, shift_value)
print("Decrypted Message:", decrypted)