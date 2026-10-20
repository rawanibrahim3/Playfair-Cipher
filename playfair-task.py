key = input("Enter key: ").upper().replace(" ", "")
text = input("Enter text: ").upper().replace(" ", "")
choice = input("1- Encryption, 2- Decryption: ")

if not key.isalpha() or not text.isalpha():
    print("Use English letters only!")

elif choice not in ["1", "2"]:
    print("Invalid choice!")

else:
    key = key.replace("J", "I")
    text = text.replace("J", "I")

    s = ""
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in s:
            s += c

    matrix = [s[i:i+5] for i in range(0, 25, 5)]

    if choice == "1":
        pairs = []
        i = 0

        while i < len(text):
            a = text[i]

            if i + 1 == len(text):
                b = "X"
                i += 1
            elif text[i] == text[i+1]:
                b = "X"
                i += 1
            else:
                b = text[i+1]
                i += 2

            pairs.append(a + b)

        text = "".join(pairs)

    elif len(text) % 2 != 0:
        print("Ciphertext must have even length!")
        text = ""

    if text:
        out = ""
        step = 1 if choice == "1" else -1

        for i in range(0, len(text), 2):
            a, b = text[i], text[i+1]

            r1, c1 = next(
                (r, c) for r in range(5) for c in range(5)
                if matrix[r][c] == a
            )
            r2, c2 = next(
                (r, c) for r in range(5) for c in range(5)
                if matrix[r][c] == b
            )

            if r1 == r2:
                out += matrix[r1][(c1+step) % 5]
                out += matrix[r2][(c2+step) % 5]

            elif c1 == c2:
                out += matrix[(r1+step) % 5][c1]
                out += matrix[(r2+step) % 5][c2]

            else:
                out += matrix[r1][c2]
                out += matrix[r2][c1]

        print("Result:", out)