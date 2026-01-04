from pathlib import Path


class DirectoryScanner:
    """
    Scans a directory recursively and returns a list of files.
    """

    def __init__(self, base_path: Path):
        self.base_path = base_path

    def scan(self):
        """
        Recursively scan the base directory and return file paths.
        """
        files = []

        for item in self.base_path.rglob("*"):
            if item.is_file():
                files.append(item)

        return files
