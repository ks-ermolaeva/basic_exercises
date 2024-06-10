# Вывести последнюю букву в слове
word = 'Архангельск'

last_letter = word[-1]
print(f'Последняя буква в слове {word}: {last_letter}')


# Вывести количество букв "а" в слове
word = 'Архангельск'

word_low = word.lower()
count = 0
for letter in word_low:
    if letter == 'а':
        count += 1
print(f'Кол-во букв "а" в слове {word}: {count}')


# Вывести количество гласных букв в слове
word = 'Архангельск'

vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
word_low = word.lower()
count = 0
for letter in word_low:
    if letter in vowel:
        count += 1
print(f'Кол-во гласных букв в слове {word}: {count}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

words = sentence.split()
count_w = len(words)
print(f'Кол-во слов в предложении "{sentence}": {count_w}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

words_list = sentence.split()
for words in words_list:
    print(words[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

words_list = sentence.split()
count_w = len(words)
total_length = 0
for words in words_list:
    length = len(words)
    total_length += length
length_avg = total_length / count_w
print(f'Средняя длина слов в предложении: {length_avg}')
