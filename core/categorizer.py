from pathlib import Path
from config.constants import CATEGORY_MAP, DEFAULT_CATEGORY


class FileCategorizer:
    """
    Determines the category of a file based on its extension.
    """

    def __init__(self, category_map=None):
        self.category_map = category_map or CATEGORY_MAP

    def get_category(self, file_path: Path) -> str:
        """
        Return category name for given file.
        """
        extension = file_path.suffix.lower()

        for category, extensions in self.category_map.items():
            if extension in extensions:
                return category

        return DEFAULT_CATEGORY
