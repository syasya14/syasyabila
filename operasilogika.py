def cek_tipe_input(a, b, c):
    if isinstance(a, str) and isinstance(b, int) and isinstance(c, float):
        return "Tipe input valid"
    else:
        return "Tipe input tidak valid"

# Kasus uji
print(cek_tipe_input("Halo", 10, 3.14))  # Tipe input valid
print(cek_tipe_input(100, 10, 3.14))  # Tipe input tidak valid
print(cek_tipe_input("Tes", "20", 2.5))  # Tipe input tidak valid
print(cek_tipe_input("Python", 5, 2.0))  # Tipe input valid
