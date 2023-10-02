def read_data(file_name):
    data=[]
    try:
        with open("ki.txt", 'r') as file:
            for line in file:
                data.append(line.strip())
        return data
    except FileNotFoundError:
        print("A megadott fájl nem található.")
        return None

def is_numeric(data):
    for item in data:
        if not item.isdigit():
            return False
    return True

def choose_sort_algorithm():
    print("Válassz rendezési algoritmust:")
    print("1. Egyszerű cserés rendezés")
    print("2. Buborékrendezés")
    print("3. Továbbfejlesztett buborékrendezés")
    print("4. Beszúrásos rendezés")
    print("5. Továbbfejlesztett beszúrásos rendezés")
    print("6. Minimum/maximum kiválasztásos rendezés")
    choice = int(input("Választott algoritmus (1-6): "))
    return choice

def sort_data(data, ascending):
    if ascending:
        return sorted(data)
    else:
        return sorted(data, reverse=True)

def search_data(data, item):
    for i in range(len(data)):
        if data[i] == item:
            return i
    return -1

def insert_data(data, item):
    data.append(item)
    data.sort()

def main():
    file_name = "ki.txt"
    data = read_data(file_name)
    
    if data is None:
        return

    is_numeric_data = is_numeric(data)

    if is_numeric_data:
        data = [int(item) for item in data]
    else:
        data = [str(item) for item in data]

    ascending = bool(int(input("Rendezési irány (növekvő: 1, csökkenő: 0): ")))
    
    choice = choose_sort_algorithm()
    
    if choice == 1:
        data = sort_data(data, ascending)
    elif choice == 2:
        data = sort_data(data, ascending)
    elif choice == 3:
        data = sort_data(data, ascending)
    elif choice == 4:
        data = sort_data(data, ascending)
    elif choice == 5:
        data = sort_data(data, ascending)
    elif choice == 6:
        data = sort_data(data, ascending)
    else:
        print("Érvénytelen választás.")

    print("Rendezett adatok:")
    print(data)

    new_item = input("Új elem hozzáadása: ")
    if is_numeric_data:
        new_item = int(new_item)
    
    insert_data(data, new_item)

    print("Rendezett adatok új elemmel:")
    print(data)

if __name__ == "__main__":
    main()
