import shutil
from pathlib import Path

from config.constants import OUTPUT_DIR_NAME, DEFAULT_CATEGORY
from utils.logger import AuditLogger



class FileOrganizer:
    """
    Organizes files into category-based folders
    inside a single output directory.
    """

    def __init__(self, output_base_path: Path):
        self.output_base_path = output_base_path
        self.logger = AuditLogger(output_base_path / "audit.log")

    def create_output_dir(self):
        """
        Create base output directory if not exists.
        """
        self.output_base_path.mkdir(exist_ok=True)

    def organize_file(self, file_path: Path, category: str):
        category = category or DEFAULT_CATEGORY

        category_dir = self.output_base_path / category
        category_dir.mkdir(parents=True, exist_ok=True)

        destination = category_dir / file_path.name

        if destination.exists():
            self.logger.log(
                action="SKIPPED",
                source=file_path,
                destination=destination,
                message="File already exists"
            )
            print(f"[SKIP] {file_path.name}")
            return

        try:
            shutil.copy2(file_path, destination)

            self.logger.log(
                action="COPIED",
                source=file_path,
                destination=destination
            )
            print(f"[COPIED] {file_path.name} → {category}/")

        except Exception as e:
            self.logger.log(
                action="ERROR",
                source=file_path,
                destination=destination,
                message=str(e)
            )
            print(f"[ERROR] Failed to copy {file_path.name}")

