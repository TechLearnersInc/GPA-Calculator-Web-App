class Base26Converter:
    def __init__(self):
        self.__BASE26 = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        self.__BASE26INDEX = dict()
        for index, char in enumerate(self.__BASE26):
            self.__BASE26INDEX[char] = index

    def encode_to_base26(self, decimal: int):
        if decimal <= 0:
            return 0
        else:
            quotient, reminder = divmod(decimal, len(self.__BASE26))
            result: str = self.__BASE26[reminder]

            while True:
                if quotient == 0:
                    break
                else:
                    quotient, reminder = divmod(quotient, len(self.__BASE26))
                    result += self.__BASE26[reminder]
            return result

    def encode(self, counter):
        if type(counter) == int:
            decimal = counter  # int.from_bytes(bytes(string, 'utf-8'), 'big')
            return self.encode_to_base26(decimal)


if __name__ == '__main__':
    counter = 3089157776  # 10^26
    i = 0
    while i < 100:
        EncodedText: str = Base26Converter().encode(counter + i)
        print(EncodedText, len(EncodedText))
        i += 1
    # DecodedText: str = Base62Converter().decode(EncodedText)
    # print('Text: {0}\nEncoded: {1}\nDecoded: {2}'.format(string, EncodedText, DecodedText))
    # print(EncodedText, len(EncodedText))
