def extract_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Если utf-8 не работает, попробуйте другую кодировку
        with open(file_path, 'r', encoding='latin-1') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""
