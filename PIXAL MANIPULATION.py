from PIL import Image
import numpy as np
import random

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB format
    pixels = np.array(img)
    
    # Get image dimensions
    height, width, _ = pixels.shape

    # Create a random permutation of pixel indices
    indices = list(range(height * width))
    random.seed(key)
    random.shuffle(indices)

    # Create a new image by rearranging pixels
    encrypted_pixels = np.zeros_like(pixels)
    for i in range(height):
        for j in range(width):
            original_index = i * width + j
            new_index = indices[original_index]
            new_i, new_j = divmod(new_index, width)
            encrypted_pixels[i, j] = pixels[new_i, new_j]

    # Save the encrypted image
    encrypted_img = Image.fromarray(encrypted_pixels)
    encrypted_img.save(output_image_path)

    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image
    img = Image.open(input_image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB format
    pixels = np.array(img)
    
    # Get image dimensions
    height, width, _ = pixels.shape

    # Recreate the original indices using the key
    indices = list(range(height * width))
    random.seed(key)
    random.shuffle(indices)

    # Reverse the pixel rearrangement
    decrypted_pixels = np.zeros_like(pixels)
    for i in range(height):
        for j in range(width):
            original_index = i * width + j
            new_index = indices.index(original_index)
            new_i, new_j = divmod(new_index, width)
            decrypted_pixels[i, j] = pixels[new_i, new_j]

    # Save the decrypted image
    decrypted_img = Image.fromarray(decrypted_pixels)
    decrypted_img.save(output_image_path)

    print(f"Image decrypted and saved to {output_image_path}")

def main():
    print("Welcome to the Image Encryption Tool!")

    # Get user input for encryption or decryption
    operation = input("Would you like to Encrypt or Decrypt an image? (E/D): ").lower()
    input_image_path = input("Enter the path of the image: ")
    output_image_path = input("Enter the output path: ")
    key = int(input("Enter a key (integer) for encryption: "))

    if operation == 'e':
        encrypt_image(input_image_path, output_image_path, key)
    elif operation == 'd':
        decrypt_image(input_image_path, output_image_path, key)
    else:
        print("Invalid operation! Please enter 'E' for encrypt or 'D' for decrypt.")

    print("\nProDigy Infotech - Created by Rohan Patel")

if __name__ == "__main__":
    main()
