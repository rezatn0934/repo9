from dataclasses import dataclass


@dataclass
class FileReader:
    file_name: str

    def __enter__(self):
        self.file = open(self.file_name, "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileReader("text.txt") as file:
    a = file.read()
    print(a)
