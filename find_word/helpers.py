import os

colors = {
    'red': "\033[91m",
    'base': "\033[0m",
}


def get_files_path(extension='.txt'):
    words_path = os.path.join(os.curdir, 'words')
    words_full_path = [os.path.join(words_path, file) for file in os.listdir(words_path) if file.endswith(extension)]

    return words_full_path


def find_word(query):
    all_files = get_files_path()

    for file in all_files:
        with open(file, 'r') as f:
            lines = f.readlines()

            for line in lines:
                if query in line:
                    matched_line = line.replace(query, f"{colors['red']}{query}{colors['base']}")
                    print(f"{file}:{matched_line}")
