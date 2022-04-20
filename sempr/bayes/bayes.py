import ast
from math import log2

model_cz = ast.literal_eval(open('model_cz_nodia.txt', encoding='utf-8').read())
model_sk = ast.literal_eval(open('model_sk_nodia.txt', encoding='utf-8').read())

disable_diacritics = True

test_files = ['inputs/cz_veta1.txt', 'inputs/sk_veta1.txt', 'inputs/cz_clanek1.txt', 'inputs/sk_clanek1.txt']

for file in test_files:
    print(file)
    with open(file, encoding='utf-8') as f:
        input = f.read()
        input = input.translate(str.maketrans(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "áéíóúůäšěčřžťďňôľ" if disable_diacritics else "",
            "abcdefghijklmnopqrstuvwxyz" + "aeiouuasecrztdnol" if disable_diacritics else ""))

        res_cz = 0
        res_sk = 0
        for first, second, third in zip(input, input[1:], input[2:]):
            try:
                res_cz += log2(model_cz[(first, second, third)])
                res_sk += log2(model_sk[(first, second, third)])
            except: 
                None

        print('CZ: ' + str(res_cz))
        print('SK: ' + str(res_sk))
