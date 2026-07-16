def int_change():
    while True:
        n = input("桁数を入力してください（1～9、Enterで3桁）> ").strip()

        if n == "":
            return 3

        if n.isdigit() and 1 <= int(n) <= 9:
            return int(n)

        print("1～9の数字を入力してください。")