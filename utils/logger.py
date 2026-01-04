from datetime import datetime
from pathlib import Path


class AuditLogger:
    """
    Handles audit logging for file operations.
    """

    def __init__(self, log_file: Path):
        self.log_file = log_file
        self.log_file.parent.mkdir(exist_ok=True)

    def log(self, action: str, source: Path, destination: Path = None, message: str = ""):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entry = f"{timestamp} | {action} | {source}"
        if destination:
            entry += f" -> {destination}"
        if message:
            entry += f" | {message}"

        entry += "\n"

        with self.log_file.open("a", encoding="utf-8") as f:
            f.write(entry)
