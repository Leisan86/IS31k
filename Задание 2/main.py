from coder_decoder import code
from coder_decoder import decode


phrase = input('Введите слово для шифровки: ')
if phrase.isdigit() == True:
    print("Вы ввели число в фазу кодирования! Отмена кодирования!")
    print("Декодирование фразы:", decode(phrase))
elif phrase.isdigit() == False:
    print("Ваш код:", code(phrase))
