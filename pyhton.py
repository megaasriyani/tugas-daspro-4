input("""***********program konversi bilangan angka*************""")

def konversi_biner(angka):
    return bin(angka)[2:]

def konversi_oktal(angka):
    return oct(angka)[2:]

def konversi_desimal(angka):
    return str(angka)

def konversi_heksadesimal(angka):
    return hex(angka)[2:]

def main():
    a = 3
    b = 12

    biner_a = konversi_biner(a)
    oktal_a = konversi_oktal(a)
    desimal_a = konversi_desimal(a)
    heksadesimal_a = konversi_heksadesimal(a)

    biner_b = konversi_biner(b)
    oktal_b = konversi_oktal(b)
    desimal_b = konversi_desimal(b)
    heksadesimal_b = konversi_heksadesimal(b)
   
    print("Hasil konversi untuk a = 3:")
    print("Biner:", biner_a)
    print("Oktal:", oktal_a)
    print("Desimal:", desimal_a)
    print("Heksadesimal:", heksadesimal_a)

    print("\nHasil konversi untuk b = 12:")
    print("Biner:", biner_b)
    print("Oktal:", oktal_b)
    print("Desimal:", desimal_b)
    print("Heksadesimal:", heksadesimal_b)

if __name__ == "__main__":
    main()