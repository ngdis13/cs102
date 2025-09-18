def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    lst_plaintect_code = [ord(i) for i in plaintext]
    lst_keyword_code = [
        ord(i.lower()) - ord("a") for i in keyword
    ]  # Приведение ключа к нижнему регистру
    lst_result = []
    indx_code = 0
    for code in lst_plaintect_code:
        if chr(code) == chr(code).upper():
            start_indx = ord("A")
        else:
            start_indx = ord("a")
        if chr(code).isalpha():
            if indx_code < len(lst_keyword_code):
                formula = (code - start_indx + lst_keyword_code[indx_code]) % 26 + start_indx
                indx_code += 1
            else:
                formula = (code - start_indx + lst_keyword_code[0]) % 26 + start_indx
                indx_code = 1
            lst_result.append(formula)
        else:
            if indx_code < len(lst_keyword_code):
                indx_code += 1
            else:
                indx_code = 1
            lst_result.append(code)  # Если это не буква, оставляем символ без изменений
    string_result = ""
    for code in lst_result:
        string_result += chr(code)
    return string_result


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    lst_keyword_code = [
        ord(i.lower()) - ord("a") for i in keyword
    ]  # Приведение ключа к нижнему регистру
    lst_result = []
    indx_code = 0
    for code in ciphertext:
        if code.isalpha():  # Проверяем, является ли символ буквой
            if code.isupper():
                start_indx = ord("A")  # Начало алфавита для заглавных букв
            else:
                start_indx = ord("a")  # Начало алфавита для строчных букв
            # Считаем формулу расшифровки
            shift = lst_keyword_code[indx_code % len(lst_keyword_code)]  # Сдвиг по ключевому слову
            formula = (
                ord(code) - start_indx - shift + 26
            ) % 26 + start_indx  # Применяем формулу сдвига
            lst_result.append(chr(formula))  # Добавляем расшифрованный символ
            indx_code += 1  # Переход к следующему символу ключа
        else:
            lst_result.append(code)  # Если это не буква, оставляем символ без изменений
            indx_code += 1

    string_result = ""
    for i in lst_result:
        string_result += i
    return string_result