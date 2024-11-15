import physics

def main():
    # Příklad použití funkcí z modulu physics
    print("Hmotnost na Zemi: 70 kg")
    weight_on_earth = 70  # Hmotnost na Zemi v kg
    weight_on_moon = physics.weight_on_moon(weight_on_earth)
    print(f"Hmotnost na Měsíci: {weight_on_moon:.2f} kg")

    distance_to_moon = 384400000  # Vzdálenost na Měsíc v metrech (průměrná)
    time_for_light = physics.time_for_light_to_travel(distance_to_moon)
    print(f"Doba pro světlo, aby dorazilo na Měsíc: {time_for_light:.6f} sekundy")

    distance_in_city = 500  # Vzdálenost v metech, např. mezi dvěma budovami
    time_for_sound = physics.time_for_sound_to_travel(distance_in_city)
    print(f"Doba pro zvuk, aby urazil vzdálenost 500 m: {time_for_sound:.2f} sekundy")

if __name__ == "__main__":
    main()
