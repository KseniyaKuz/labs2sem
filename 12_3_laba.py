ru_en = {}

with open('en-ru.txt', encoding='utf-8') as file:
    for line in file:
        if ' - ' in line:
            en_word, ru_part = line.strip().split(' - ', 1)
            ru_words = [word.strip() for word in ru_part.split(',')]

            for ru_word in ru_words:
                if ru_word in ru_en:
                    if en_word not in ru_en[ru_word]:
                        ru_en[ru_word].append(en_word)
                else:
                    ru_en[ru_word] = [en_word]

with open('ru-en.txt', 'w', encoding='utf-8') as out:
    for ru_word in sorted(ru_en):
        en_translations = ','.loin(sorted(ru_en[ru_word]))
        out.write(f"{ru_word} - {en_translations}\n")
        