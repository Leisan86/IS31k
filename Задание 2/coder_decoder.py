hard_dictionary = {"A":"11", "B":"12", "C":"13","D":"14", "E":"15",
                   "F":"21", "G":"22", "H":"23", "I":"24","K":"25",
                   "L":"31", "M":"32", "N":"33", "O":"34", "P":"35",
                   "Q":"41", "R":"42", "S":"43", "T":"44", "U":"45",
                   "V":"51", "W":"52", "X":"53", "Y":"54", "Z":"55"}
def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def code(phrase):
    new_txt = ""
    list_phrase = list(phrase) #из строки в лист
    #подставка значений из фразы в цифры, то есть кодирование
    for x in phrase:
        if x in hard_dictionary:
            new_txt += hard_dictionary.get(x)
        else:
            new_txt += (x + x)
    return new_txt

def decode(phrase):
    new_txt = ""
    list_phrase = []
    #перевод из строки в лист используя ключи букв
    step = 2
    for i in range(0, len(str(phrase)), 2):
        list_phrase.append(phrase[i:step])
        step += 2
    # лист для декодирования фразы
    key_hard_dictionary_list = list(hard_dictionary.keys())
    val_hard_dictionary_list = list(hard_dictionary.values())

    for x in list_phrase:
        if x in val_hard_dictionary_list:
            i = val_hard_dictionary_list.index(x)
            new_txt += key_hard_dictionary_list[i]
        else:
            new_txt += x[0:1]
    return new_txt