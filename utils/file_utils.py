import os
import shutil


def cleanup_temp_files(user_id: int, file_path: str = None):
    if file_path and os.path.exists(file_path):
        os.remove(file_path)

    receipts_dir = "data/receipts"
    if os.path.exists(receipts_dir):
        pass