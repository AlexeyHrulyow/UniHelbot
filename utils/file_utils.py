#file_utils.py

import os
import logging

logger = logging.getLogger(__name__)

def safe_remove_file(file_path: str) -> bool:
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logger.info(f'Removed {file_path}')
            return True
    except Exception as e:
        logger.error(f'Failed to remove {file_path}: {e}')
    return False