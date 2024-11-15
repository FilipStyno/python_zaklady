'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81  # Normální pozemské tíhové zrychlení (m/s²)
MOON_GRAVITY = 1.625  # Měsíční gravitace (m/s²)
SPEED_OF_LIGHT = 299792458  # Rychlost světla ve vakuu (m/s)
SPEED_OF_SOUND = 343  # Rychlost zvuku při teplotě 20°C v suchém vzduchu (m/s)

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def weight_on_moon(weight_on_earth):
    """
    Funkce pro výpočet hmotnosti tělesa na Měsíci na základě hmotnosti na Zemi.
    
    :param weight_on_earth: Hmotnost tělesa na Zemi v kg.
    :return: Hmotnost tělesa na Měsíci v kg.
    """
    return weight_on_earth * (MOON_GRAVITY / EARTH_GRAVITY)

def time_for_light_to_travel(distance):
    """
    Funkce pro výpočet doby, za kterou světlo urazí danou vzdálenost.
    
    :param distance: Vzdálenost, kterou světlo urazí (v metrech).
    :return: Doba v sekundách, za kterou světlo urazí danou vzdálenost.
    """
    return distance / SPEED_OF_LIGHT

def time_for_sound_to_travel(distance):
    """
    Funkce pro výpočet doby, za kterou zvuk urazí danou vzdálenost.
    
    :param distance: Vzdálenost, kterou zvuk urazí (v metrech).
    :return: Doba v sekundách, za kterou zvuk urazí danou vzdálenost.
    """
    return distance / SPEED_OF_SOUND
