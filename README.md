# Steganography-Project
Secure Data Hiding in Images Using Steganography

Introduction

This project demonstrates image-based steganography, a technique to hide secret messages inside an image while keeping it visually unchanged. The hidden message can be securely retrieved using a passcode.

Features

✅ Hides messages inside an image without noticeable changes
✅ Password-protected decryption
✅ Uses OpenCV for image processing
✅ Lightweight and simple implementation

Requirements

Make sure you have the following installed:

Python 3.x

OpenCV (pip install opencv-python)


How to Use

1. Encryption (Hiding the Message)

Run the script and follow the prompts:

python steganography.py

Enter the secret message you want to hide.

Enter a passcode for security.

The script modifies the image and saves it as encryptedImage.jpg.


2. Decryption (Retrieving the Message)

Run the script again and enter the correct passcode:

python steganography.py

If the password matches, the hidden message is revealed.

If the password is incorrect, access is denied.


Project Structure

/Steganography-Project
│── steganography.py  # Main script for encryption & decryption
│── Sample.jpg        # Sample image for testing
│── encryptedImage.jpg # Output image with hidden data
│── README.md         # This file
