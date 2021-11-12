import collections

def lng_n_frq(text):
    text = input('Введите текст: ')
    words = text.split()
    counter = collections.Counter(words)
    most_common, occurrences = counter.most_common()[0]
    longest = max(words, key=len)
    print(most_common, longest)


text = 0
lng_n_frq(text)