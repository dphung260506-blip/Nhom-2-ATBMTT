import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
from math import gcd

# ==========================
# Miller Rabin
# ==========================

def is_prime(n, k=5):
    if n < 2:
        return False

    if n in (2, 3):
        return True

    if n % 2 == 0:
        return False

    r = 0
    d = n - 1

    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 2)

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


def generate_prime():
    while True:
        num = random.randint(100, 500)

        if is_prime(num):
            return num


# ==========================
# Euclid mở rộng
# ==========================

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd_value, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd_value, x, y


def mod_inverse(e, phi):
    gcd_value, x, y = extended_gcd(e, phi)

    if gcd_value != 1:
        return None

    return x % phi


# ==========================
# RSA
# ==========================

public_key = None
private_key = None


def taoKhoa():
    global public_key, private_key

    p = generate_prime()
    q = generate_prime()

    while p == q:
        q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537

    if gcd(e, phi) != 1:
        e = 3

        while gcd(e, phi) != 1:
            e += 2

    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)

    txtPublic.delete("1.0", tk.END)
    txtPrivate.delete("1.0", tk.END)

    txtPublic.insert(
        tk.END,
        f"p = {p}\n"
        f"q = {q}\n\n"
        f"e = {e}\n"
        f"n = {n}"
    )

    txtPrivate.insert(
        tk.END,
        f"d = {d}\n"
        f"n = {n}"
    )

    messagebox.showinfo(
        "RSA",
        "Đã tạo khóa thành công!"
    )


# ==========================
# Mã hóa
# ==========================

def maHoa():
    if public_key is None:
        messagebox.showerror(
            "Lỗi",
            "Vui lòng tạo khóa trước."
        )
        return

    plaintext = txtPlain.get(
        "1.0",
        tk.END
    ).strip()

    if plaintext == "":
        return

    e, n = public_key

    cipher = []

    for ch in plaintext:
        m = ord(ch)
        c = pow(m, e, n)
        cipher.append(str(c))

    txtCipher.delete("1.0", tk.END)

    txtCipher.insert(
        tk.END,
        " ".join(cipher)
    )


# ==========================
# Giải mã
# ==========================

def giaiMa():
    if private_key is None:
        messagebox.showerror(
            "Lỗi",
            "Vui lòng tạo khóa trước."
        )
        return

    cipher_text = txtCipher.get(
        "1.0",
        tk.END
    ).strip()

    if cipher_text == "":
        return

    try:
        d, n = private_key

        cipher_list = list(
            map(int, cipher_text.split())
        )

        plaintext = ""

        for c in cipher_list:
            m = pow(c, d, n)
            plaintext += chr(m)

        txtResult.delete("1.0", tk.END)

        txtResult.insert(
            tk.END,
            plaintext
        )

    except:
        messagebox.showerror(
            "Lỗi",
            "Bản mã không hợp lệ."
        )


# ==========================
# Reset
# ==========================

def resetDuLieu():
    txtPlain.delete("1.0", tk.END)
    txtCipher.delete("1.0", tk.END)
    txtResult.delete("1.0", tk.END)


def resetTatCa():
    global public_key, private_key

    public_key = None
    private_key = None

    txtPublic.delete("1.0", tk.END)
    txtPrivate.delete("1.0", tk.END)

    txtPlain.delete("1.0", tk.END)
    txtCipher.delete("1.0", tk.END)
    txtResult.delete("1.0", tk.END)

    messagebox.showinfo(
        "RSA",
        "Đã xóa toàn bộ dữ liệu."
    )


# ==========================
# Giao diện
# ==========================

root = tk.Tk()
root.title("Hệ mật mã RSA")
root.geometry("900x700")

# Khóa công khai

tk.Label(
    root,
    text="Khóa công khai",
    font=("Arial", 10, "bold")
).pack(anchor="w")

txtPublic = scrolledtext.ScrolledText(
    root,
    height=6
)

txtPublic.pack(fill="x", padx=5, pady=5)

# Khóa bí mật

tk.Label(
    root,
    text="Khóa bí mật",
    font=("Arial", 10, "bold")
).pack(anchor="w")

txtPrivate = scrolledtext.ScrolledText(
    root,
    height=4
)

txtPrivate.pack(fill="x", padx=5, pady=5)

# Bản rõ

tk.Label(
    root,
    text="Bản rõ",
    font=("Arial", 10, "bold")
).pack(anchor="w")

txtPlain = scrolledtext.ScrolledText(
    root,
    height=6
)

txtPlain.pack(fill="x", padx=5, pady=5)

# Bản mã

tk.Label(
    root,
    text="Bản mã",
    font=("Arial", 10, "bold")
).pack(anchor="w")

txtCipher = scrolledtext.ScrolledText(
    root,
    height=6
)

txtCipher.pack(fill="x", padx=5, pady=5)

# Kết quả giải mã

tk.Label(
    root,
    text="Kết quả giải mã",
    font=("Arial", 10, "bold")
).pack(anchor="w")

txtResult = scrolledtext.ScrolledText(
    root,
    height=6
)

txtResult.pack(fill="x", padx=5, pady=5)

# ==========================
# Giao diện
# ==========================

frameButton = tk.Frame(root)
frameButton.pack(side=tk.BOTTOM, pady=15)

tk.Button(
    frameButton,
    text="TẠO KHÓA",
    width=15,
    command=taoKhoa
).grid(row=0, column=0, padx=5)

tk.Button(
    frameButton,
    text="MÃ HÓA",
    width=15,
    command=maHoa
).grid(row=0, column=1, padx=5)

tk.Button(
    frameButton,
    text="GIẢI MÃ",
    width=15,
    command=giaiMa
).grid(row=0, column=2, padx=5)

tk.Button(
    frameButton,
    text="RESET DỮ LIỆU",
    width=15,
    command=resetDuLieu
).grid(row=0, column=3, padx=5)

tk.Button(
    frameButton,
    text="RESET TẤT CẢ",
    width=15,
    command=resetTatCa
).grid(row=0, column=4, padx=5)

root.mainloop()