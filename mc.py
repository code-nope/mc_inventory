inventorius = {}

def prideti(daiktas, kiekis):
    for langelis in inventorius:
        if inventorius[langelis]["daiktas"] == daiktas:
            vieta = 64 - inventorius[langelis]["kiekis"]
            if vieta > 0:
                if kiekis <= vieta:
                    inventorius[langelis]["kiekis"] += kiekis
                    return
                inventorius[langelis]["kiekis"] = 64
                kiekis -= vieta



    while kiekis > 0:
        for langelis in range(1, 10):
            if langelis not in inventorius:
                if kiekis <= 64:
                    inventorius[langelis] = {
                        "daiktas": daiktas,
                        "kiekis": kiekis
                    }
                    return
                inventorius[langelis] = {
                    "daiktas": daiktas,
                    "kiekis": 64
                }
                kiekis -= 64
                break
        else:
            print("Inventorius pilnas!")
            return



def rodyti():
    for langelis in range(1, 10):
        print(langelis, inventorius.get(langelis, "Tuščias"))
def perkelti(is_langelio, i_langelio):
    if is_langelio not in inventorius:
        print("Langelis tuščias!")
    elif i_langelio not in range(1, 10):
        print("Neteisingas langelis!")
    elif i_langelio not in inventorius:
        inventorius[i_langelio] = inventorius.pop(is_langelio)
    else:
        inventorius[is_langelio], inventorius[i_langelio] = inventorius[i_langelio], inventorius[is_langelio]

while True:
    print("1. Pridėti daiktą")
    print("2. Rodyti inventorių")
    print("3. Perkelti daiktą")
    print("4. Baigti")
    pasirinkimas = input("Pasirinkimas: ")

    
    if pasirinkimas == "1":
        daiktas = input("Daikto pavadinimas: ")
        kiekis = int(input("Kiekis: "))
        prideti(daiktas, kiekis)
    elif pasirinkimas == "2":
        rodyti()
    elif pasirinkimas == "3":
        pradinis = int(input("Iš kurio langelio? "))
        galutinis = int(input("Į kurį langelį? "))
        perkelti(pradinis, galutinis)
    elif pasirinkimas == "4":
        break