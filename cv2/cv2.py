from collections import Counter
from math import log2

def pmi(input):
    words = open(input).read().splitlines()
    word_counts = {x: count for x, count in Counter(words).items() if count > 9}
    pair_counts = {}
    
    for first, second in zip(words, words[1:]):
        if first not in word_counts or second not in word_counts:
            continue

        pair = (first, second)
        if pair not in pair_counts:
            pair_counts[pair] = 1
        else:
            pair_counts[pair] = pair_counts[pair] + 1

    word_count = sum(word_counts.values())
    pair_count = sum(pair_counts.values())

    for pair, count in pair_counts.items():
        first, second = pair
        pair_counts[pair] = log2((count/pair_count)/((word_counts[first]/word_count) * (word_counts[second]/word_count)))

    for pair in sorted(pair_counts, key=pair_counts.get, reverse=True):
        yield (pair, pair_counts[pair])

def pmi_50(input):
    words = open(input).read().splitlines()
    word_counts = {x: count for x, count in Counter(words).items() if count > 9}
    pair_counts = {}

    for i in range(len(words)):
        for j in range(-50, 51):
            if i+j < 0 or i+j > len(words)-1 or i == i+j:
                continue;

            pair = (words[i], words[i+j])
            if pair[0] not in word_counts or pair[1] not in word_counts:
                continue

            if pair not in pair_counts:
                pair_counts[pair] = 1
            else:
                pair_counts[pair] = pair_counts[pair] + 1

    word_count = sum(word_counts.values())
    pair_count = sum(pair_counts.values())

    for pair, count in pair_counts.items():
        first, second = pair
        pair_counts[pair] = log2((count/pair_count)/((word_counts[first]/word_count) * (word_counts[second]/word_count)))

    for pair in sorted(pair_counts, key=pair_counts.get, reverse=True):
        yield (pair, pair_counts[pair])

def print_result(result, output_file):
    out = open(output_file, 'w')
    out.write('<table>')
    for pair, pmi in result:
        out.write('<tr>')
        out.write('<td>' + pair[0] + ' ' + pair[1] + '</td>')
        out.write('<td>' + str(pmi) + '</td>')
        out.write('</tr>')
    out.write('</table>')


print_result(pmi('TEXTCZ1.txt'), 'out_cz.html')
print_result(pmi('TEXTEN1.txt'), 'out_en.html')

print_result(pmi_50('TEXTCZ1.txt'), 'out_50_cz.html')
print_result(pmi_50('TEXTEN1.txt'), 'out_50_en.html')
