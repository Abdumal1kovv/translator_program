import csv
import json
from io import open
from pprint import pprint

with open("dictionary.json") as file:
    a = json.load(file)

with open("languages.csv") as file:
    list_lang = csv.reader(file)

def save_d_to_json():
    with open("dictionary.json", "w") as file:
        json.dump(a, file, indent=2)

def save_l_to_csv():
    with open("languages.csv", "w") as file1:
        file1.write(','.join(list_lang))

list_lang = ['en', 'uz', 'ru', 'jp', 'cn']

from_language = 'en'  # en -> cn
to_language = 'uz'
n = 'word_en'
text = '''Menyu:
1 - Qidirish
2 - Soz qoshish
3 - Holatni korish
4 - Holatni ozgartirish
5 - Sinonim qoshish
6 - Tarjimasi yoqlar
7 - Til qoshish
8 - Tillarni korish
9 - Slovarni korish

10 - Chiqish'''

print(text)
while True:
    try:
        key = int(input("Menyuni tanlang: "))
    except ValueError as e:
        print("Menyuni togri tanlang")
        continue
    if key == 1:  # 1-qidirish
        _word = input(f"Sozni kiriting [{from_language}]: ")
        for v in a.values():
            __word = v[from_language]
            if isinstance(__word, list) and _word in __word or \
                    isinstance(__word, str) and _word in __word == _word:
                print(v.get(to_language, "Shu tilda tarjimasi yoq"))
                break
        else:
            print("Topilmadi")
    elif key == 2:  # soz qoshish
        _temp = {}
        for _lang in list_lang:
            _l = input(f"Sozni {_lang} dagi tarjimasini kiriting: ")
            _temp[_lang] = _l

        a[_temp["en"]] = _temp
        save_d_to_json()

    elif key == 3:  # 3-holatni korish
        print(f"{from_language}->{to_language}")
    elif key == 4:  # 4-holatni ozgartirish
        _from = input(f"birinchi tilni kiriting {list_lang}: ")
        _to = input(f"ikkinchi tilni kiriting {list_lang}: ")
        from_language = _from
        to_language = _to
    elif key == 5:  # 5-sinonim qoshish
        from_word = input(f"Qaysi sozga sinonim kiritasiz {from_language} ?: ")
        to_word = input(f"Sinonimni kiriting {to_language}: ").split(", ")

        for v in a.values():
            __word = v[from_language]
            if isinstance(__word, list) and from_word in __word:
                v[to_language].append(to_word)
                break
            if isinstance(__word, str) and from_word in __word == from_word:
                to_word.append(v[to_language])
                v[to_language] = to_word
                break
        else:
            print("Topilmadi")
    elif key == 6:  # 6-tarjimasi yoqlar
        print("all words: ", len(a))
        maximum_lang = max(len(v) for v in a.values())
        for k, v in a.items():
            if len(v) != maximum_lang:
                print(k, list(set(list_lang).difference(set(v.keys()))))
    elif key == 7:
        lang = input("Yangi tilni kiriting")
        list_lang.append(lang)
        save_l_to_csv()

    elif key == 8:  # 8-tillarni korish
        pprint(list_lang)
    elif key == 9:  # 9-slovarni korish
        pprint(a)
    else:
        print("Chiqish")
        break