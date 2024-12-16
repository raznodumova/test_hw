import pytest
from ya_folder import create_folder


@pytest.mark.parametrize("folder_name, expected", [
    ('test_folder', True),
    ('test_folder', False),
    ('test_folder2', True),
    ('test_folder2', False),
    ('test_folder3', True),
    ('test_folder3', False),
])
def test_create_foldef(folder_name, expected):
    assert create_folder(folder_name) == expected