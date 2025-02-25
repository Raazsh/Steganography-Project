import cv2

img = cv2.imread("encryptedImage.jpg") # Replace with the correct image path

message = ""
n = 0
m = 0
z = 0

c = {}
for i in range(255):
    c[i] = chr(i)

pas = input("Enter passcode for Decryption: ")
if pas == input("Enter the same passcode used for encryption: "): # Ensuring correct passcode
    for i in range(len(msg)): # Uses the length of the message
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
