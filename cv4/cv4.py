from collections import Counter

def bigram(input):
    words = open(input).read().splitlines()
    word_counts = {x: count for x, count in Counter(words).items()}
    pair_counts = {}

    for first, second in zip(words, words[1:]):
        pair = (first, second)
        if pair not in pair_counts:
            pair_counts[pair] = 1
        else:
            pair_counts[pair] = pair_counts[pair] + 1

    model = {pair: count/word_counts[pair[1]] for pair, count in pair_counts.items()}
    return (model, word_counts)

def wb(model, word_counts):
    existing = {}
    smoothed = {}
    for word in word_counts.keys():
        existing[word] = sum(map(lambda key: key[1] == word, model.keys()))
        not_existing = len(word_counts) - existing[word]
        smoothed[(None, word)] = word_counts[word]/(not_existing*(word_counts[word] + existing[word]))

    for pair, count in model.items():
        N = word_counts[pair[1]]
        T = existing[pair[1]]
        smoothed[pair] = count/(N + T)
        
    return smoothed

def output(model, output_file):
    out = open(output_file, 'w')
    out.write('<table>')
    for key in sorted(model, key=model.get, reverse=True):
        out.write('<tr>')
        out.write('<td>' + str(key) + '</td>')
        out.write('<td>' + str(model[key]) + '</td>')
        out.write('</tr>')
    out.write('</table>')

model, counts = bigram("TEXTCZ1.txt")
output(wb(model, counts), "wb-cz.html")

model, counts = bigram("TEXTEN1.txt")
output(wb(model, counts), "wb-en.html")
