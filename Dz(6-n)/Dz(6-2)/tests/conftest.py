import pytest


@pytest.fixture(autouse=True)
def my_create_files_fixture():
    with open("pen.txt", "w") as f:
        pen = open("pen.txt", "w")
        pen.write("pen")
        pass
    with open("apple.txt", "w") as f:
        apple = open("apple.txt", "w")
        apple.write("apple")
        pass
    with open("pineapple.txt", "w") as f:
        pineapple = open("pineapple.txt", "w")
        pineapple.write("pineapple")
        pass
