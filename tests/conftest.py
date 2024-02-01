from zipfile import ZipFile
import pytest
from Pathes import *


@pytest.fixture
def create_zip():
    if not os.path.exists(RESOURCES_PATH):
        os.mkdir(RESOURCES_PATH)

    with ZipFile(ARCHIVE_PATH, 'w') as zip_file:
        for file in FILES_LIST:
            file_path = os.path.join(FILES_PATH, file)
            zip_file.write(file_path, file)

    with ZipFile(ARCHIVE_PATH, 'r') as zip_file:
        archive_files = zip_file.namelist()

        for file in FILES_LIST:
            assert file in archive_files

        zip_file.extractall(FILES_PATH)

    yield FILES_PATH


