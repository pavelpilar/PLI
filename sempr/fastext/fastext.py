import fasttext

model = fasttext.load_model("lid.176.bin")

test_files = ['../bayes/inputs/cz_veta1.txt', '../bayes/inputs/sk_veta1.txt', '../bayes/inputs/cz_clanek1.txt', '../bayes/inputs/sk_clanek1.txt']

disable_diacritics = False
for file in test_files:
    for file in test_files:
        print(file)
        with open(file, encoding='utf-8') as f:
            input = f.read()
            input = input.translate(str.maketrans(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "áéíóúůäšěčřžťďňôľ" if disable_diacritics else "",
                "abcdefghijklmnopqrstuvwxyz" + "aeiouuasecrztdnol" if disable_diacritics else ""))

            print(file + ' ' + str(model.predict(input)))
