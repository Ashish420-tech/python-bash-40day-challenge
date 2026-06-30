from datetime import datetime
from file_manager import FileManager


class Logger(FileManager):

    def log_message(self, filename, message):
        """Append a timestamped log entry."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log = f"[{timestamp}] {message}\n"
        self.append_file(filename, log)
