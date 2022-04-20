# Vytváření znakového modelu

Jako korpusy pro český a slovenský jazyk byly použity soubory `cs.txt` a `sk.txt`[[1]](https://lindat.mff.cuni.cz/repository/xmlui/handle/11234/1-2735). (Kvůli velikosti nejsou součástí repozitáře)

Modely obsahují znaky z následujícího seznamu: `['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ý' , 'ó', 'ú', 'ů', 'ä', 'š', 'ě', 'č', 'ř', 'ž', 'ť', 'ď', 'ň', 'ô', 'ľ', ',', '.', ' ']`. Velká písmena se mění na malá. Trigramy obsahující jiné znaky se přeskakují. (Např. řecká abeceda, závorky atp.)

Vyhlazeny jsou metodou Witten-Bell.

# Výsledky

Výsledky pro jazyky jsou dány jako logaritmus pravděpodobnosti.

| Vstup       | CZ          | SK          | Správný výsledek |
| ----------- | ----------- | ----------- | -----------      |
| cz_veta     | -921.906    | -853.414    | ❌              |
| sk_veta     | -1639.637   | -1497.137   | ✅              |
| cz_clanek   | -25758.770  | -24278.097  | ❌              |
| sk_clanek   | -37227.706  | -33928.676  | ✅              |

## Bez diakritiky

| Vstup       | CZ          | SK          | Správný výsledek |
| ----------- | ----------- | ----------- | -----------      |
| cz_veta     | -1642.817   | -1539.457   | ❌              |
| sk_veta     | -2700.578   | -2471.530   | ✅              |
| cz_clanek   | -51571.765  | -48349.854  | ❌              |
| sk_clanek   | -71713.812  | -66053.534  | ✅              |
