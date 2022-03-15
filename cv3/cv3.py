from collections import Counter
from math import log2

def unigram(input):
    words = open(input).read().splitlines()
    word_count = len(words)
    model = {x: count/word_count for x, count in Counter(words).items()}
    perplexity = 2**(-sum(map(lambda x: x*log2(x), model.values())))
    return (model, perplexity)

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
    pair_count = sum(map(lambda count: count, pair_counts.values()))

    model = {pair: count/word_counts[pair[1]] for pair, count in pair_counts.items()}
    perplexity = 2**(-sum(map(lambda x: (pair_counts[x]/pair_count)*log2(model[x]), model)))
    return (model, perplexity)

def trigram(input):
    words = open(input).read().splitlines()
    pair_counts = {}
    tri_counts = {}
    for first, second, third in zip(words, words[1:], words[2:]):
        pair = (second, third)
        tri = (first, second, third)

        if pair not in pair_counts:
            pair_counts[pair] = 1
        else:
            pair_counts[pair] = pair_counts[pair] + 1

        if tri not in tri_counts:
             tri_counts[tri] = 1
        else:
            tri_counts[tri] = tri_counts[tri] + 1
    tri_count = sum(map(lambda count: count, tri_counts.values()))

    model = {tri: count/pair_counts[(tri[1], tri[2])] for tri, count in tri_counts.items()}
    perplexity = 2**(-sum(map(lambda x: (tri_counts[x]/tri_count)*log2(model[x]), model)))
    return (model, perplexity)

def print_result(model, output_file):
    out = open(output_file, 'w')
    out.write('Perplexita: ' + str(model[1]) + '\n')
    out.write('<table>')
    for item in sorted(model[0], key=model[0].get, reverse=True):
        out.write('<tr>')
        out.write('<td>' + str(item) + '</td>')
        out.write('<td>' + str(model[0][item]) + '</td>')
        out.write('</tr>')
    out.write('</table>')
    
unigram_result = list(unigram('TEXTCZ1.txt'))
bigram_result = list(bigram('TEXTCZ1.txt'))
trigram_result = list(trigram('TEXTCZ1.txt'))

print_result(unigram_result, "unigram_cz.html")
print_result(bigram_result, "bigram_cz.html")
print_result(trigram_result, "trigram_cz.html")

unigram_result = list(unigram('TEXTEN1.txt'))
bigram_result = list(bigram('TEXTEN1.txt'))
trigram_result = list(trigram('TEXTEN1.txt'))

print_result(unigram_result, "unigram_en.html")
print_result(bigram_result, "bigram_en.html")
print_result(trigram_result, "trigram_en.html")
