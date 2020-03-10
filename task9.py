def word():
    stroka = input('Введите текст : ')
    stroka = stroka.replace('!','')
    stroka = stroka.replace('?','')
    stroka = stroka.replace(',','')
    stroka = stroka.replace('.','')
    stroka = stroka.replace('#','')
    return(stroka)
print(word())