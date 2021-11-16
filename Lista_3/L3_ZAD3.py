def counting_chars_without_ifs(filename):
    file_ref = open(filename, 'r')
    text = file_ref.read()
    text = text.replace(" ", "").lower()

    char_count = {k: 0 for k in text}
    for i in text:
        char_count[i] += 1

    return char_count
