from homework4.task03.get_print_output import my_precious_logger


def test_my_precious_logger_stdout(capsys):
    my_precious_logger("OK")
    out, err = capsys.readouterr()
    assert out == "OK"


def test_error_in_my_precious_logger_stderr(capsys):
    my_precious_logger("error: file not found")
    out, err = capsys.readouterr()
    assert err == "error: file not found"
