import os
import qrcode

data=input("Enter the data to be encoded in the QR code: ")
qr=qrcode.make(data)

download_folder=os.path.join(os.getcwd(), "Downloads")
if not os.path.exists(download_folder):
    os.makedirs(download_folder)
file_path=os.path.join(download_folder, "qr_code.png")
qr.save(file_path)
print("QR code generated and saved as qr_code.png")