import collections

def lng_n_frq(text):
    words = text.split()
    counter = collections.Counter(words)
    most_common, occurrences = counter.most_common()[0]
    longest = max(words, key=len)
    print(most_common, longest)


text = input('Введите текст: ')
lng_n_frq(text)