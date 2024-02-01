import os

CUR_FILE_PATH = os.path.abspath(__file__)
CUR_DIR_PATH = os.path.dirname(__file__)
FILES_PATH = os.path.join(CUR_DIR_PATH, 'files')
FILES_LIST = os.listdir(FILES_PATH)
RESOURCES_PATH = os.path.join(CUR_DIR_PATH, 'resources')
ARCHIVE_PATH = os.path.join(RESOURCES_PATH, 'archive.zip')
