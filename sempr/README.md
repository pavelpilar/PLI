# Vytváření znakového modelu

Jako korpusy pro český a slovenský jazyk byly použity soubory `cs.txt` a `sk.txt`[[1]](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2735). Soubor `cs.txt` byl zkrácen tak, aby měl stejnou délku jako `sk.txt`. (Kvůli velikosti nejsou součástí repozitáře)

Modely obsahují znaky z následujícího seznamu: `['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ý' , 'ó', 'ú', 'ů', 'ä', 'š', 'ě', 'č', 'ř', 'ž', 'ť', 'ď', 'ň', 'ô', 'ľ', ',', '.', ' ']`. Velká písmena se mění na malá. Trigramy obsahující jiné znaky se přeskakují. (Např. řecká abeceda, závorky atp.) Jejich vytváření se provádí skriptem `models.py`.

Vyhlazeny jsou metodou Witten-Bell.

# Výsledky

Výsledky se počítají skriptem `bayes.py`. Jsou dány jako logaritmus pravděpodobnosti.

| Vstup       | CZ          | SK          | Správný výsledek |
| ----------- | ----------- | ----------- | -----------      |
| cz_veta     | -769.274    | -778.218    | ✅              |
| sk_veta     | -540.370    | -507.468    | ✅              |
| cz_clanek   | -5233.617   | -5403.586   | ✅              |
| sk_clanek   | -4609.523   | -4515.269   | ✅              |

## Bez diakritiky

| Vstup       | CZ          | SK          | Správný výsledek |
| ----------- | ----------- | ----------- | -----------      |
| cz_veta     | -2166.839   | -2201.071   | ✅              |
| sk_veta     | -1095.331   | -1093.852   | ✅              |
| cz_clanek   | -10736.802  | -10874.661  | ✅              |
| sk_clanek   | -9248.217   | -9244.777   | ✅              |
