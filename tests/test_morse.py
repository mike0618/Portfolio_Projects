from src.morse_text_miked import morse_text


def test_encode():
    assert '.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.-- ' == morse_text.encode('Hello, World!')


def test_decode():
    assert 'HELLO, WORLD!' == morse_text.decode('.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.-- ')
