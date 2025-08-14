"""
1 - найти текст
2 - почистить от мусора
3 - посчитать слова

4 - в будущем добавить визуализацию

"""
from collections import Counter
from data.text import mail_tatiana_oneginu, angelo


def parser_prose(txt: str):
    res = (x for x in txt if x == ' ' or x.isalpha() or x == '\n')
    ob = Counter(''.join(res).lower().split())
    print(ob)
    return


if __name__ == '__main__':
    print(parser_prose(mail_tatiana_oneginu))
    print(parser_prose(angelo))
