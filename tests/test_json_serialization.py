import os
import tempfile
from pathlib import Path

from seagoat.result import Result
from seagoat.result import ResultLine


def test_to_result_line_correct_output_example1():
    line = ResultLine(1, 0.5, "some line text")
    result_dict = line.to_json()
    assert result_dict == {
        "line": 1,
        "line_text": "some line text",
    }


def test_to_result_line_correct_output_example2():
    line = ResultLine(2, 0.2, "another line of text")
    result_dict = line.to_json()
    assert result_dict == {
        "line": 2,
        "line_text": "another line of text",
    }


def test_to_result_json_correct_output_example1():
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_path = os.path.join(tmpdirname, "example1.txt")
        with open(file_path, "w", encoding="utf-8") as tmp_file:
            tmp_file.write("Line 1\nLine 2\nLine 3\n")

        result = Result("example1.txt", Path(file_path))
        result.add_line(1, 0.5)
        result.add_line(2, 0.3)

        result_dict = result.to_json()
        assert result_dict == {
            "path": "example1.txt",
            "full_path": file_path,
            "lines": [
                {"line": 1, "line_text": "Line 1"},
                {"line": 2, "line_text": "Line 2"},
            ],
        }


def test_to_result_json_correct_output_example2():
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_path = os.path.join(tmpdirname, "example2.txt")
        with open(file_path, "w", encoding="utf-8") as tmp_file:
            tmp_file.write("This is line 1\nThis is line 2\nThis is line 3\n")

        result = Result("example2.txt", Path(file_path))
        result.add_line(1, 0.5)
        result.add_line(3, 0.1)

        result_dict = result.to_json()
        assert result_dict == {
            "path": "example2.txt",
            "full_path": file_path,
            "lines": [
                {"line": 1, "line_text": "This is line 1"},
                {"line": 3, "line_text": "This is line 3"},
            ],
        }