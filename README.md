# 📱 QR Code Generator using Python

A simple and beginner-friendly **QR Code Generator** built using Python.  
This project allows users to enter any text or URL and generates a QR code image saved as a `.png` file.

---

## 🚀 Features

- 🔹 Takes user input (text, link, etc.)
- 🔹 Generates QR code instantly
- 🔹 Saves QR code as `qr_code.png`
- 🔹 Automatically creates a `Downloads` folder (if not present)
- 🔹 Clean and minimal implementation

---

## 🛠️ Built With

- Python 3
- `qrcode` package
- `os` module (for file handling)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/midhunmanesh01-code/QRCode
cd QRCode
```

### 2️⃣ Install Dependency

This project requires the `qrcode` package.

```bash
pip install qrcode[pil]
```

---

## ▶️ How to Run

Run the script using:

```bash
python qradv.py
```

or

```bash
python qrbasic.py
```

Then enter the data when prompted.

### Example

```
Enter the data to be encoded in the QR code: https://github.com
```

---

## 📂 Output

The generated QR code will be saved as:

```
Downloads/qr_code.png
```

(If using the basic version, it will be saved directly in the project folder.)

---

## 🧠 How It Works

1. Takes input from user
2. Uses `qrcode.make(data)` to generate QR image
3. Creates a Downloads folder if it doesn't exist
4. Saves the QR image as a PNG file

---

## 📸 Example Use Cases

- Website links
- Contact information
- WiFi credentials
- Payment links
- Portfolio links

---

## 📈 Future Improvements

- Add custom QR colors
- Add logo in center
- Create GUI version using Tkinter
- Convert into a web app using Flask

---

## 👨‍💻 Author

**Midhun Manesh**  
B.Tech CSE (AI & ML) Student  
Aspiring AI/ML Engineer 🚀
