import pytest

from Dz62 import merge_and_write


def test_merge_and_write():
    assert merge_and_write('apple.txt', 'pen.txt', 'apple_pen.txt') != "app"


def test_merge_and_write2():
    assert merge_and_write('banana.txt', 'pen.txt', 'apple_pen.txt') == "Один из файлов не найден"


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        ("apple.txt", "pen.txt", "apple_pen.txt", "apple pen"),
        ("pen.txt", "pineapple.txt", "pen_pineapple.txt", "pen pineapple"),
        ("pen_pineapple.txt", "apple_pen.txt", "pen_pineapple_apple_pen.txt", "pen pineapple apple pen")
    ]
)
def test_merge_and_write3(a, b, c, expected):
    assert merge_and_write(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, c, not_expected",
    [
        ("apple.txt", "pen.txt", "apple_pen.txt", "banana"),
        ("pen.txt", "pineapple.txt", "pen_pineapple.txt", "pear"),
        ("pen_pineapple.txt", "apple_pen.txt", "pen_pineapple_apple_pen.txt", "watermelon")
    ]
)
def test_merge_and_write4(a, b, c, not_expected):
    assert merge_and_write(a, b, c) != not_expected
