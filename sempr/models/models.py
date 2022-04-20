
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', ' '
             #'á', 'é', 'í', 'ý' , 'ó', 'ú', 'ů', 'ä', 'š', 'ě', 'č', 'ř', 'ž', 'ť', 'ď', 'ň', 'ô', 'ľ',
             ]

disable_diacritics = True

counts_cz = {}
pairs_cz = {}
counts_sk = {}
pairs_sk = {}

for char1 in characters:
    for char2 in characters:
        pairs_cz[(char1, char2)] = 0
        pairs_sk[(char1, char2)] = 0

        for char3 in characters:
            counts_cz[(char1, char2, char3)] = 0
            counts_sk[(char1, char2, char3)] = 0

cz = open('cs.txt', encoding='utf-8').read().splitlines()
for line in cz:
    line = line.translate(str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "áéíóúůäšěčřžťďňôľ" if disable_diacritics else "",
        "abcdefghijklmnopqrstuvwxyz" + "aeiouuasecrztdnol" if disable_diacritics else ""))

    for first, second, third in zip(line, line[1:], line[2:]):
        try:
            pairs_cz[(first, second)] += 1
            counts_cz[(first, second, third)] += 1
        except:
            None

# Model
count_cz = sum(map(lambda count: count, counts_cz.values()))
model_cz = {tri: 0 if count == 0 else count/pairs_cz[(tri[0], tri[1])] for tri, count in counts_cz.items()}

# Vyhlazení
existing_pairs_cz = {}
for pair in pairs_cz.keys():
    existing_pairs_cz[pair] = sum(map(lambda key: key[0] == pair[0] and key[1] == pair[1], model_cz.keys()))

for trigram, count in model_cz.items():
    pair = (trigram[0], trigram[1])
    T = existing_pairs_cz[pair]
    N = pairs_cz[pair]
    if count == 0:
        Z = len(pairs_cz) - existing_pairs_cz[pair]
        model_cz[trigram] = T / (Z * (N + T))
    else:
        model_cz[trigram] = count / (N + T)

out = open('model_cz.txt', 'w', encoding='utf-8')
out.write(str(model_cz))

sk = open('sk.txt', encoding='utf-8').read().splitlines()
for line in sk:
    for first, second, third in zip(line, line[1:], line[2:]):
        try:
            pairs_sk[(second, third)] += 1
            counts_sk[(first, second, third)] += 1
        except:
            None

count_sk = sum(map(lambda count: count, counts_sk.values()))
model_sk = {tri: 0 if count == 0 else count/pairs_sk[(tri[1], tri[2])] for tri, count in counts_sk.items()}

existing_pairs_sk = {}
for pair in pairs_sk.keys():
    existing_pairs_sk[pair] = sum(map(lambda key: key[0] == pair[0] and key[1] == pair[1], model_sk.keys()))

for trigram, count in model_sk.items():
    pair = (trigram[0], trigram[1])
    T = existing_pairs_sk[pair]
    N = pairs_sk[pair]
    if count == 0:
        Z = len(pairs_sk) - existing_pairs_sk[pair]
        model_sk[trigram] = T / (Z * (N + T))
    else:
        model_sk[trigram] = count / (N + T)

out = open('model_sk.txt', 'w', encoding='utf-8')
out.write(str(model_sk))
