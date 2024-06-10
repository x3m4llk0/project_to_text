import os
import chardet

# Путь до корневой директории проекта
project_dir = 'path/to/your/project'  # замените на ваш путь
пше
# Извлечение имени проекта из пути
project_name = os.path.basename(os.path.normpath(project_dir))

# Имя выходного текстового файла
output_file = f'{project_name}_files.txt'

# Директории, которые необходимо игнорировать
ignored_dirs = ['venv', '.idea', '.git', '__pycache__']

def list_project_tree(directory, ignored_dirs):
    project_tree = []
    for root, dirs, files in os.walk(directory):
        # Удаляем игнорируемые директории из списка
        dirs[:] = [d for d in dirs if d not in ignored_dirs]

        level = root.replace(directory, '').count(os.sep)
        indent = '|' + ' ' * 4 * (level - 1) + '+-- ' if level > 0 else ''
        project_tree.append(f'{indent}{os.path.basename(root)}/')
        sub_indent = '|' + ' ' * 4 * level + '+-- '
        for file in files:
            project_tree.append(f'{sub_indent}{file}')
    return project_tree

def read_file_content(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        return raw_data.decode(encoding)

def list_files_and_contents(directory, ignored_dirs, output_file):
    project_tree = list_project_tree(directory, ignored_dirs)

    with open(output_file, 'w', encoding='utf-8') as f:
        # Записываем дерево проекта
        f.write('Project Structure:\n')
        f.write('\n'.join(project_tree))
        f.write('\n\n')

        # Записываем содержимое файлов
        for root, dirs, files in os.walk(directory):
            # Удаляем игнорируемые директории из списка
            dirs[:] = [d for d in dirs if d not in ignored_dirs]

            for file in files:
                file_path = os.path.join(root, file)
                f.write(f'File: {file_path}\n')
                try:
                    file_content = read_file_content(file_path)
                    f.write(file_content)
                except Exception as e:
                    f.write(f'Error reading file: {e}\n')
                f.write('\n' + '='*80 + '\n')  # Разделитель между файлами

if __name__ == "__main__":
    list_files_and_contents(project_dir, ignored_dirs, output_file)
