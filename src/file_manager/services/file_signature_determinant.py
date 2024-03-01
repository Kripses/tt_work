def file_img(f):
    """
    обработчик фалйа картинки
    :return: None.
    """
    pass


def file_document(f):
    """
    обработчик текстового файла
    :return: None.
    """
    pass


def file_video(f):
    """
    обработчик видеофайла
    :return: None.
    """
    pass


def file_sound(f):
    """
    обработчик звуковых файлов
    :return: None.
    """
    pass


signature = {
    "FF D8 FF E0": file_img,
    "49 46 00 01": file_img,
    "89 50 4E 47 0D 0A 1A 0A": file_img,
    "25 50 44 46 2D": file_document,
    "52 49 46 46": file_sound,
    "57 41 56 45": file_sound,
    "41 56 49 20": file_video,
    "FF FB": file_sound,
    "FF F3": file_sound,
    "FF F2": file_sound,
    "49 44 33": file_sound,
    "66 74 79 70 4D 53 4E 56": file_video,
    "66 74 79 70 69 73 6F 6D": file_video,
}


def read_file(file) -> None:
    """
    Получение сигнатуры файла. Итерация по словарю сигнатур и сравнение
    их с полученной сигнатурой в соответствии со смещением.

    :param file: файл.
    :return: None.
    """
    with open(file.path, 'rb') as f:
        file = f.read(256)
        hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])
        for hex_ch in signature:
            for i in range(13):
                if hex_ch == str(hex_bytes[i:len(hex_ch) + i]):
                    signature.get(hex_ch)(f)
                    return
                continue
