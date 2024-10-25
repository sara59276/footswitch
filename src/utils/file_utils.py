import os
import platform
from stat import S_IREAD


class FileUtil:

    @staticmethod
    def create_file(destination_folder: str, scan_id: str, animal_id: str, experimenter_initials: str, current_date: str) -> str:
        filename = f"{scan_id}_{animal_id}_{experimenter_initials}_{current_date}.csv"
        destination_folder = destination_folder
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
