import pytest
from pathlib import Path

# Assuming students will have functions like these in a file named student_code.py
from assignment import write_numbers_to_file, sum_numbers_in_file, count_lines_words, count_words_in_file

# --- Exercise 1: Write numbers to a file ---
@pytest.mark.parametrize(
    "numbers, expected_content",
    [
        ([10, 20, 30], "10\n20\n30\n"),
        ([1, 2, 3, 4, 5], "1\n2\n3\n4\n5\n"),
    ]
)
def test_write_numbers_to_file(tmp_path, numbers, expected_content):
    file_path = tmp_path / "numbers.txt"
    # Call student function
    write_numbers_to_file(numbers, file_path)
    # Check file content
    assert file_path.read_text() == expected_content


# --- Exercise 2: Sum numbers in a file ---
@pytest.mark.parametrize(
    "file_content, expected_sum",
    [
        ("10\n20\n30\n", 60),
        ("1\n2\n3\n4\n5\n", 15),
    ]
)
def test_sum_numbers_in_file(tmp_path, file_content, expected_sum):
    file_path = tmp_path / "numbers.txt"
    file_path.write_text(file_content)
    # Call student function
    result = sum_numbers_in_file(file_path)
    assert result == expected_sum


# --- Exercise 3: Count lines and words in a text file ---
@pytest.mark.parametrize(
    "file_content, expected_lines, expected_words",
    [
        ("Python is fun.\nIt helps you learn programming.\nFile handling is important.\n", 3, 10),
        ("Hello world\nPython programming\nFile exercises\n", 3, 6),
    ]
)
def test_count_lines_words(tmp_path, file_content, expected_lines, expected_words):
    file_path = tmp_path / "data.txt"
    file_path.write_text(file_content)
    lines, words = count_lines_words(file_path)
    assert lines == expected_lines
    assert words == expected_words


# --- Exercise 4: Count words in a text file ---
@pytest.mark.parametrize(
    "file_content, expected_word_count",
    [
        ("Hello world\nPython programming\nFile exercises\n", 6),
        ("One two three\nFour five\n", 5),
    ]
)
def test_count_words_in_file(tmp_path, file_content, expected_word_count):
    file_path = tmp_path / "data.txt"
    file_path.write_text(file_content)
    count = count_words_in_file(file_path)
    assert count == expected_word_count
