import os
import shutil
import sys

def normalize(text):
    char_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'д': 'd', 'е': 'e', 'є': 'ye', 'ж': 'zh',
        'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'yi', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'yu', 'я': 'ya'
    }

    text = text.lower()  # Converting text to lowercase before transliteration
    result = []

    for char in text:
        if char in char_map:
            result.append(char_map[char])
        elif char.isalnum():
            result.append(char)
        else:
            result.append('_')

    return ''.join(result)


# Function for sorting files
def sort_files(folder_path):
    extensions = {
        'images': ('JPEG', 'PNG', 'JPG', 'SVG'),
        'videos': ('AVI', 'MP4', 'MOV', 'MKV'),
        'documents': ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
        'audio': ('MP3', 'OGG', 'WAV', 'AMR'),
        'archives': ('ZIP', 'GZ', 'TAR')
    }

    known_extensions = set()
    unknown_extensions = set()

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_extension = file.split('.')[-1].upper()
            known = False

            for category, exts in extensions.items():
                if file_extension in exts:
                    known = True
                    known_extensions.add(file_extension)

                    target_folder = os.path.join(folder_path, category)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    source_file = os.path.join(root, file)
                    target_file = os.path.join(target_folder, normalize(file))
                    shutil.move(source_file, target_file)

            if not known:
                unknown_extensions.add(file_extension)

    return known_extensions, unknown_extensions

def start(folder):

    known_extensions, unknown_extensions = sort_files(folder)

    print("Known extensions:")
    for ext in known_extensions:
        print(ext)

    print("\nUnknown extensions:")
    for ext in unknown_extensions:
        print(ext)

if __name__ == '__main__':
    start()  