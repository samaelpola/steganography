# 🔒 Steganography: Hide Secrets in Images

## ✅ Compatibility

- **Python**: Version 3.8 or higher is required.

## 🚀 Usage

> **Note**: Ensure you are at the root of the project directory before executing any commands.

---

### 🔧 Prerequisites

#### 1️⃣ Create and Activate a Virtual Environment

To follow best practices, create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

- **On Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **On macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

#### 2️⃣ Install Dependencies

Ensure you have the following Python libraries installed:

- `Pillow`
- `Click`

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

---

## 🖼️ Hide a Secret Message

### Command:

```bash
python src/stegano.py hide <source_image_path> <destination_folder_path> <message>
```

### Parameters:

- `<source_image_path>`: Path to the source image.
- `<destination_folder_path>`: Path to the folder where the image with the hidden message will be saved.
- `<message>`: The message you want to hide in the image.

### Example:

```bash
python src/stegano.py hide src/input/ninho.jpeg src/output "My secret message"
```

---

## 🔍 Reveal a Hidden Message

### Command:

```bash
python src/stegano.py reveal <image_path>
```

### Parameter:

- `<image_path>`: Specify the path to the image containing the hidden message.

### Example:

```bash
python src/stegano.py reveal src/output/secret-ninho.png
```

---

## 📖 Additional Notes

- Ensure the source image format is compatible with the steganography script (e.g., `.jpeg`, `.png`).
- Use clear and descriptive folder paths to avoid confusion.

---
