def convert_minutes_to_seconds(minutes):
    
    # seconds = minutes * 60
    # seconds_int = int(round(seconds))
    # return seconds_int
    return round(minutes * 60)

def main():

    min_to_sec = float(input("Skriv inn hvor mange minutter du vil ha om til sekunder: "))
    print(f"{min_to_sec} minutter blir {convert_minutes_to_seconds(min_to_sec)} sekunder")
if __name__ == "__main__":
    main()