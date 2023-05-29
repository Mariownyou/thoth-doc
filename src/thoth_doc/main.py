import os

from thoth_doc.parsers import code_reference_parser


class DocGenerator:
    parsers = []
    _default_parsers = [code_reference_parser]
    output_dirs = []

    def __init__(self, docs_folder, compiled_docs_folder):
        self.docs_folder = docs_folder
        self.compiled_docs_folder = compiled_docs_folder

    def write_file(self, lines, filepath):
        cwd = os.getcwd()
        base = filepath.replace(self.docs_folder, '')
        path = f'{cwd}/{self.compiled_docs_folder}{base}'

        with open(path, 'w') as f:
            f.write(lines)

    def parse_file(self, filepath):
        compiled_markdown = ''

        with open(filepath) as f:
            markdown = f.readlines()

        for line in markdown:
            for parser in self.parsers + self._default_parsers:
                parsed = parser(line)
                if parsed is not None:
                    compiled_markdown += parsed
                    break
        return compiled_markdown

    def create_folder_structure(self):
        cwd = os.getcwd()
        os.makedirs(f'{cwd}/{self.compiled_docs_folder}', exist_ok=True)

        for root, dirs, files in os.walk(self.docs_folder):
            for dir in dirs:
                path = f'{cwd}/{self.compiled_docs_folder}/{root.replace(self.docs_folder, "")}/{dir}'
                os.makedirs(path, exist_ok=True)

    def generate(self):
        self.create_folder_structure()

        for root, dirs, files in os.walk(self.docs_folder):
            for file in files:
                if file.endswith('.md'):
                    path = os.path.join(root, file)
                    compiled_lines = self.parse_file(path)
                    self.write_file(compiled_lines, path)
                else:
                    os.system(f'cp {os.path.join(root, file)} {self.compiled_docs_folder}/{root.replace(self.docs_folder, "")}')


if __name__ == '__main__':
    generator = DocGenerator('docs', 'docs_compiled')
    generator.generate()
