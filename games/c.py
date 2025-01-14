def c():
    def is_armstrong(n):
        digits = [int(d) for d in str(n)]
        return n == sum(d ** len(digits) for d in digits)

    while True:
        user_input = input("Masukkan angka (ketik 'exit' untuk keluar dari game): ")
        
        if user_input.lower() == "exit":
            print("Program selesai. Keluar dari Game 3")
            break

        try:
            n = int(user_input)
        except ValueError:
            print("Input harus berupa angka. Silahkan coba lagi.")
            continue

        if is_armstrong(n):
            print(f"{n} adalah bilangan Armstrong")
        else:
            print(f"{n} bukan bilangan Armstrong")
