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
    if not keyword: 
        raise ValueError('Ключ не может быть пустым')
    
    lst_plaintect_code = [ord(i) for i in plaintext]
    lst_keyword_code = [
        ord(i.lower()) - ord("a") for i in keyword
    ]  # Приведение ключа к нижнему регистру
    
    lst_result = []
    keyword_index = 0
    
    for code in lst_plaintect_code:
        if chr(code).isalpha():
            if chr(code).isupper():
                start_indx = ord('A')
            else:
                start_indx = ord('a')
                
            shift_value = lst_keyword_code[keyword_index % len(lst_keyword_code)]
            
            formula = (code - start_indx + shift_value) % 26 + start_indx
            lst_result.append(formula)
            keyword_index += 1
        else: 
            lst_result.append(code)
            keyword_index += 1
    
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
    if not keyword:
        raise ValueError('Ключ не может быть пустым')
    
    lst_keyword_code = [ord(char.lower()) - ord("a") for char in keyword ]  
    
    lst_result = []
    keyword_index = 0
    
    for cipher_char in ciphertext:
        if cipher_char.isalpha(): 
            if cipher_char.isupper():
                start_indx = ord("A") 
            else:
                start_indx = ord("a")  
                
            # Получаем текущий сдвиг из ключевого слова, используя оператор % для циклического доступа
            shift = lst_keyword_code[keyword_index % len(lst_keyword_code)]
            
             # Преобразуем текущий зашифрованный символ в его относительную позицию (0-25)
            cipher_char_relative = ord(cipher_char) - start_indx
            
            # Применяем формулу дешифрования: (относительный_зашифрованный - сдвиг_ключа + 26) % 26
            # +26 гарантирует положительный результат перед %
            decrypted_relative = (cipher_char_relative - shift + 26) % 26
            
            decrypted_code = decrypted_relative + start_indx
            lst_result.append(chr(decrypted_code))
            
            keyword_index += 1
        else:
            lst_result.append(cipher_char)
            keyword_index += 1

    return "".join(lst_result)