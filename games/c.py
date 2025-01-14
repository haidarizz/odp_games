def c():
    def is_armstrong(n):
        digits = [int(d) for d in str(n)]
        return n == sum(d ** len(digits) for d in digits)

    while True:
        n = int(input("Masukkan angka (tekan 0 untuk keluar): "))
        
        if n == 0:
            print("Program selesai.")
            break

        if is_armstrong(n):
            print(f"{n} adalah bilangan Armstrong")
        else:
            print(f"{n} bukan bilangan Armstrong")
