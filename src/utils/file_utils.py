import os
import platform
from datetime import datetime
from stat import S_IREAD


class FileUtil:

    ROOT_DIR = os.path.abspath(os.sep)
    DATA_DIR = os.path.join(ROOT_DIR, 'Footswitch', 'data')

    @staticmethod
    def create_file(scan_id: str, animal_id: str, experimenter_initials: str, current_date: str) -> str:
        filename = f"{scan_id}_{animal_id}_{experimenter_initials}_{current_date}.csv"
        destination_folder = FileUtil._get_destination_folder()
        filepath = os.path.join(destination_folder, filename)

        os.makedirs(destination_folder, exist_ok=True)
        if not os.path.isfile(filepath):
            with open(filepath, mode="w", newline=""):
                pass
            print(f"File created at: {filepath}")
        else:
            raise FileExistsError(f"File already exists: {filepath}")

        return filepath

    @staticmethod
    def set_readonly(filepath) -> None:
        if platform.system() == 'Windows':
            os.chmod(filepath, S_IREAD)
        else:  # macOS and Linux
            os.chmod(filepath, 0o444)

    @staticmethod
    def _get_destination_folder() -> str:
        today = datetime.now()
        year, month, day = today.strftime("%Y"), today.strftime("%m"), today.strftime("%d")
        return os.path.join(FileUtil.DATA_DIR, year, month, day)
