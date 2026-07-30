from src.parser import extract_ip, extract_time, extract_port


def test_extract_ip():
    line = "Jul 30 10:10:15 sshd: Failed password from 192.168.1.50"

    assert extract_ip(line) == "192.168.1.50"


def test_extract_time():
    line = "Jul 30 10:10:15 sshd: Failed password from 192.168.1.50"

    assert extract_time(line) == "Jul 30 10:10:15"


def test_extract_port():
    line = "Failed password from 192.168.1.50 port 52122 ssh2"

    assert extract_port(line) == "52122"
