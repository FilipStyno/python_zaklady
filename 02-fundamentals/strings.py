# Znakové řetězce mohou být uvozeny jednoduchými i dvojitými uvozovkami
course_name = "Python programming"

'''
Mnohdy programátor potřebuje řetězec, který je rozložen přes více řádků. Dosáhnout toho opět můžeme několika způsoby. 
První z nich, který se neváže pouze na řetězce, je spojení dvou po sobě jdoucích řádků znakem zpětného lomítka:
'''
# Obrácené lomítka - použití escape sekvence
hello = 'Toto je dlouhý řetězec obsahující mnoho\n\
řádek textu, stejně jej zapisujete i v C.\n\
    "Bílé" znaky na začátku řádku se samozřejmě\
 berou v úvahu.'

# print(hello)

'''
Python podporuje i tzv. raw řetězce (cosi jak ryzí, syrové řetězce), u nichž se řídící (escape) sekvence 
nepřevádí na odpovídající znaky.3.2. Raw řetězce charakterizuje předpona r. 
Potom řetězec r'\n' odpovídá dvěma znakům - zpětnému lomítku a znaku n, kdežto řetězec '\n' je jediný znak nového řádku:
'''

hello = r'Toto je dlouhý řetězec obsahující mnoho\n\
řádek textu, stejně jej zapisujete i v C.'

# print(hello)

'''
Další možností, jak vytvořit víceřádkový řetězec je jeho uzavření mezi odpovídající pár trojitých uvozovek. 
To má tu výhodu, že nemusíme explicitně zapisovat konce řádků, ty bude řetězec obsahovat přesně tak, 
jak jsou zapsány ve zdrojovém kódu
'''
# Předformátovaný text je uvozen trojími uvozovkami
message = '''
    Krásný pozdrav z výletu do \"přírody\"

    posílá 

       Andrej
'''
# print(message)

# Funkce len vrací délku řetězce
# print(len(message))

'''
Řetězce můžeme (podobně jako v jazyce C) indexovat. První znak řetězce pak má index 0. 
Poněvadž je Python velice uživatelsky přítulný, nekomplikuje život programátora speciálním typem určeným pro jediný znak - 
každý znak řetězce je opět řetězec s délkou 1. 
Na získání podřetězce nepotřebujeme žádné speciální funkce, samotný jazyk podporuje indexování subsekvencí. 
Subsekvenci indexujeme podobně jako jednotlivé znaky, pouze potřebuje dva indexy (začátek a konec subsekvence), 
které oddělíme dvojtečkou:
'''

# Vypíše 4. znak z řetězce
# print(course_name[3])

'''
Důležité je si zapamatovat, že slice indexy ukazují mezi znaky, přičemž levá hrana prvního znaku má číslo 0 
a pravá hrana posledního znaku řetězce o n znacích má index n:

 +---+---+---+---+---+ 
 | H | e | l | p | A |
 +---+---+---+---+---+ 
 0   1   2   3   4   5 
-5  -4  -3  -2  -1
Na prvním řádku jsou uvedeny všechny možné slice-indexy 0...5 v řetězci 'HelpA', na druhém pak odpovídající záporné hodnoty. 
Řez od i do j je tedy tvořen všemi znaky mezi hranami označenými mezi hranami označenými i a j.
'''

# Vypíše poslední znak z řetězce
# print(course_name[-1])
# Vypíše vše od 2. do 4. znaku (bez něj)
# print(course_name[1:3])

'''
Slice indexy mají specifické vlastnosti. Vynecháme-li první index, je za něj automaticky dosazena nula (začátek řetězce). 
Při neuvedení druhého indexu se použije délka řetězce (čili konec řetězce). 
'''

# Vypíše vše od 2. znaku
# print(course_name[1:])
# Vypíše vše od 2. znaku do předposledního
# print(course_name[1:-1])
# Vypíše 3 znaky od začátku
# print(course_name[:3])

'''
Další vlastností slice indexů je jejich automatické "zarovnávání" na rozměr řetězce. 
Je-li totiž index použitý ve slice konstrukci příliš velký, je nahrazen délkou řetězce. 
'''
# print(course_name[1:50])
# Pokud je dolní index větší než horní, je výsledkem prázdný řetězec:
# print(course_name[2:1])

first_name = "Donald  "
second_name = "  Trump"
# Spojování řetězců
# print(first_name + second_name)

# Opakování řetězců
# print(first_name + second_name * 3)

'''
Řetězce v jazyce Python nelze měnit. Pokusíme-li se změnit určitou pozici v řetězci, dojde k chybě.
'''
# first_name[0] = 'R'
'''
Proto jedinou cestou, jak vytvářet nové řetězce, je jejich kombinování, které je velice jednoduché a přitom efektivní:
'''
# print('R' + first_name[1:])

# Formátovaný výstup, použití řetězcových funkcí
# print(f"{first_name.upper().rstrip()} {second_name.lower().lstrip()} {5 * 4} {len(message)}")

# Nalezení pozice podřetězce v řetězci
# print(first_name.find("na"))

# Nahrazení podřetězce v řetězci
# print(first_name.upper().replace("D", "*"))

# Zjištění výskytu podřetězce
# print("na" not in first_name)

'''
Python umí pracovat s Unicode řetězci úplně stejným způsobem jako s obyčejnými řetězci. 
Dokonce je možné díky konverzním funkcím snadno převádět obyčejné řetězce na Unicode a zpět.
Unicode řetězce můžeme zapisovat přímo ve zdrojovém kódu programu. 
Pouze před samotný řetězec vložíme prefix u (podobně jako u raw řetězců prefix r):
'''

# print(u'\xe4\xf6\xfc')

'''Pro konverzi znaků můžeme použít interní funkci encode(), 
která umožňuje přístup ke všem registrovaným kodekům (např. Latin-1, ASCII, UTF-8 nebo UTF-16). '''

# print(u'äöü'.encode('utf-8'))
# print(u'čřž'.encode('latin2'))

'''Opačnou konverzi umožňuje funkce decode(), které lze opět předat jediný argument - jméno kódování, 
ve kterém je původní osmibitový řetězec.
'''

# print(b'\xc3\xa4\xc3\xb6\xc3\xbc'.decode('utf-8'))
# print(b'\xe8\xf8\xbe'.decode('windows-1250'))

''' 
Programátorská výzva:
Použijte kombinaci různý možností pro práci s řetězci (včetně různých funkcí) i jiných prvků jazyka Python 
(ternární operátor, matematické funkce atd.) k co nejefektivnějšímu řešení následujících cvičení (čím kratší
funkční kód, tím lepší).

1. Převeďte "česky" zadané datum - např. 12. 10. 2020 - do podoby "databázové" podoby - např. 2020-10-12

def prevod_data(ceske_datum):
    """
    Funkce převede datum ve formátu 'dd.mm.yyyy' na formát 'yyyy-mm-dd',
    což je běžný formát používaný například v databázích nebo ISO standardech.
    
    Parametry:
    ceske_datum (str): Datum ve formátu 'dd.mm.yyyy'.
    
    Návratová hodnota:
    str: Datum ve formátu 'yyyy-mm-dd'.
    """
    # Rozdělení zadaného českého datumu podle teček na den, měsíc a rok
    d, m, r = ceske_datum.split('.')
    
    # Vrácení nového formátu datumu 'yyyy-mm-dd'
    return f"{r}-{m}-{d}"

# Získání datumu od uživatele ve formátu 'dd.mm.yyyy'
datum = input("Zadejte datum ve formátu 'dd.mm.yyyy': ")  # např. 12.10.2020

# Převedení datumu do formátu 'yyyy-mm-dd' a vypsání výsledku
print(prevod_data(datum))


2. Vytvořte funkci, která vyrobí ze zadaného sousloví:
   a) identifikátor pro proměnné používané v Pythonu - např. To je proměnná v Pythonu = to_je_promenna_v_pythonu
   b) identifikátor pro camel syntax v JS - např. To je proměnná v Pythonu = toJePromennaVPythonu 
   Obě možnosti by měly být vyřešeny v jedné funkci s využitím parametrů.
   Kdo si chce úkol trochu zjednodušit, nemusí řešit znaky s českou diakritikou. 

   def convert_to_identifiers():
    """
    Funkce převede uživatelem zadané sousloví na dva identifikátory:
    1. Snake case - vhodné pro Python (např. to_je_promenna_v_pythonu)
    2. Camel case - vhodné pro JavaScript (např. toJePromennaVPythonu)
    
    Uživatel zadá sousloví a funkce vypíše obě verze.
    """
    # Získání sousloví od uživatele
    text = input("Zadejte sousloví: ")
    
    # Rozdělení textu na jednotlivá slova a jejich převedení na malá písmena
    words = text.lower().split()

    # Snake_case verze: spojení slov podtržítkem
    snake_case = '_'.join(words)
    
    # CamelCase verze: první slovo zůstává malé, další slova začínají velkým písmenem
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])

    # Výstup obou verzí
    print(f"Snake case: {snake_case}")
    print(f"Camel case: {camel_case}")

# Zavolání funkce a výstup obou verzí
convert_to_identifiers()

3. Vytvořte funkci, která vygeneruje náhodná hesla pro počet osob zadaný v parametru tak, aby heslo začínalo
   3 velkými písmeny, pokračovalo 3 malými písmeny, jedním speciálním znakem (-/+*) a končilo 3 náhodnými číslicemi.

import random
import string

def generuj_hesla(pocet_osob):
    """
    Funkce vygeneruje náhodná hesla podle specifikovaných pravidel:
    - Heslo začíná 3 velkými písmeny
    - Následuje 3 malá písmena
    - Jeden speciální znak (-, +, *)
    - Končí 3 náhodnými číslicemi
    
    Parametry:
    pocet_osob (int): Počet hesel, které se mají vygenerovat.

    Výstup:
    Seznam vygenerovaných hesel.
    """
    hesla = []  # Seznam, kam uložíme vygenerovaná hesla
    specialni_znaky = "-+*"  # Speciální znaky povolené pro heslo
    
    for _ in range(pocet_osob):
        # Vygenerování 3 velkých písmen
        velka_pismena = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
        
        # Vygenerování 3 malých písmen
        mala_pismena = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
        
        # Výběr jednoho speciálního znaku
        specialni_znak = random.choice(specialni_znaky)
        
        # Vygenerování 3 náhodných číslic
        cislice = ''.join(random.choice(string.digits) for _ in range(3))
        
        # Sestavení finálního hesla
        heslo = velka_pismena + mala_pismena + specialni_znak + cislice
        hesla.append(heslo)  # Přidání vygenerovaného hesla do seznamu
    
    return hesla

# Příklad použití:
pocet = int(input("Zadejte počet osob: "))  # Získání počtu osob od uživatele
vygenerovana_hesla = generuj_hesla(pocet)

# Vypsání všech vygenerovaných hesel
for idx, heslo in enumerate(vygenerovana_hesla, 1):
    print(f"Heslo pro osobu {idx}: {heslo}")
'''
