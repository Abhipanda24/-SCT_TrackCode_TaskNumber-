def caesar_cipher(text, shift, mode):
    result = ""
    
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift for encryption or decryption
            shift_direction = shift if mode == "encrypt" else -shift
            # Normalize within a-z or A-Z
            shifted = (ord(char) - base + shift_direction) % 26 + base
            result += chr(shifted)
        else:
            result += char  # Keep non-alphabet characters unchanged
            
    return result

# --- Main Program ---

print("Caesar Cipher Program")
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode! Choose 'encrypt' or 'decrypt'.")
else:
    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (e.g., 3): "))
        output = caesar_cipher(message, shift, mode)
        print(f"\nThe {mode}ed message is:\n{output}")
    except ValueError:
        print("Shift value must be an integer!")