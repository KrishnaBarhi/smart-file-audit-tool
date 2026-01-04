import argparse
from pathlib import Path

from config.constants import OUTPUT_DIR_NAME
from core.scanner import DirectoryScanner
from core.categorizer import FileCategorizer
from core.organizer import FileOrganizer



def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Smart File Automation & Audit Tool"
    )

    parser.add_argument(
        "--path",
        required=True,
        help="Path of the directory to scan and organize"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    input_path = Path(args.path).resolve()

    # 1️⃣ Validate input path
    if not input_path.exists():
        print(f"[ERROR] Path does not exist: {input_path}")
        return

    if not input_path.is_dir():
        print(f"[ERROR] Path is not a directory: {input_path}")
        return

    # 2️⃣ Prepare output directory
    output_path = input_path.parent / OUTPUT_DIR_NAME

    print("[INFO] Starting file scan...")
    print(f"[INFO] Input Directory : {input_path}")
    print(f"[INFO] Output Directory: {output_path}")

    # 3️⃣ Scan files
    scanner = DirectoryScanner(input_path)
    files = scanner.scan()

    categorizer = FileCategorizer()

    print(f"[INFO] Total files found: {len(files)}")
    print("[INFO] Categorizing files...\n")

    print("[INFO] Organizing files...\n")
    organizer = FileOrganizer(output_path)
    organizer.create_output_dir()

    for file in files:
        category = categorizer.get_category(file)
        organizer.organize_file(file, category)

    print("\n[INFO] File organization completed successfully.")



if __name__ == "__main__":
    main()
