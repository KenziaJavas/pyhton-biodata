import tkinter as tk
from tkinter import messagebox

# Daftar menu kopi dan harga
menu_kopi = {
    "Espresso": 15000,
    "Americano": 18000,
    "Cappuccino": 20000,
    "Latte": 22000,
    "Mocaccino": 25000,
    "Caramel Macchiato": 27000,
    "Cold Brew": 24000
}

# Inisialisasi total
total = 0

# Fungsi menambah pesanan
def tambah_pesanan():
    pilihan = listbox_menu.get(tk.ACTIVE)
    if not pilihan:
        messagebox.showwarning("Peringatan", "Pilih menu kopi terlebih dahulu!")
        return

    try:
        jumlah = int(entry_jumlah.get())
        if jumlah <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Salah", "Masukkan jumlah yang valid!")
        return

    nama_kopi = pilihan.split(" - ")[0]
    harga = menu_kopi[nama_kopi]
    subtotal = harga * jumlah

    pesanan_list.insert(tk.END, f"{nama_kopi} x{jumlah} = Rp{subtotal:,}")

    global total
    total += subtotal
    label_total.config(text=f"Total: Rp{total:,}")

    entry_jumlah.delete(0, tk.END)

# Fungsi reset
def reset_pesanan():
    global total
    total = 0
    pesanan_list.delete(0, tk.END)
    label_total.config(text="Total: Rp0")

# Fungsi untuk cetak struk sederhana
def cetak_struk():
    if pesanan_list.size() == 0:
        messagebox.showinfo("Info", "Belum ada pesanan untuk dicetak.")
        return

    struk = "===== STRUK PEMBELIAN =====\n"
    for item in pesanan_list.get(0, tk.END):
        struk += f"{item}\n"
    struk += f"\nTotal: Rp{total:,}\n"
    struk += "Terima kasih telah membeli di Java Brew Coffee ☕"

    messagebox.showinfo("Struk Pembelian", struk)

# Setup window utama
root = tk.Tk()
root.title("☕ Kasir Kopi Digital | Java Brew")
root.geometry("480x550")
root.config(bg="#fdf6f0")

title = tk.Label(root, text="☕ Java Brew Coffee", font=("Arial", 20, "bold"), bg="#fdf6f0", fg="#5a3e2b")
title.pack(pady=10)

# Frame daftar menu
frame_menu = tk.Frame(root, bg="#fdf6f0")
frame_menu.pack()

tk.Label(frame_menu, text="Menu Kopi:", font=("Arial", 12, "bold"), bg="#fdf6f0").grid(row=0, column=0, sticky="w")
listbox_menu = tk.Listbox(frame_menu, width=35, height=8, font=("Arial", 11))
for nama, harga in menu_kopi.items():
    listbox_menu.insert(tk.END, f"{nama} - Rp{harga:,}")
listbox_menu.grid(row=1, column=0, padx=10, pady=5)

# Frame input jumlah
frame_input = tk.Frame(root, bg="#fdf6f0")
frame_input.pack(pady=5)
tk.Label(frame_input, text="Jumlah:", font=("Arial", 11), bg="#fdf6f0").grid(row=0, column=0)
entry_jumlah = tk.Entry(frame_input, width=10)
entry_jumlah.grid(row=0, column=1, padx=5)

btn_tambah = tk.Button(frame_input, text="Tambah", command=tambah_pesanan, bg="#795548", fg="white", width=10)
btn_tambah.grid(row=0, column=2, padx=5)

# Daftar pesanan
tk.Label(root, text="Pesanan Anda:", font=("Arial", 12, "bold"), bg="#fdf6f0").pack()
pesanan_list = tk.Listbox(root, width=40, height=8, font=("Arial", 11))
pesanan_list.pack(pady=5)

# Label total
label_total = tk.Label(root, text="Total: Rp0", font=("Arial", 13, "bold"), bg="#fdf6f0", fg="#000")
label_total.pack(pady=10)

# Tombol aksi
frame_btn = tk.Frame(root, bg="#fdf6f0")
frame_btn.pack(pady=5)

btn_reset = tk.Button(frame_btn, text="Reset", command=reset_pesanan, bg="#d32f2f", fg="white", width=12)
btn_reset.grid(row=0, column=0, padx=5)

btn_cetak = tk.Button(frame_btn, text="Cetak Struk", command=cetak_struk, bg="#4CAF50", fg="white", width=12)
btn_cetak.grid(row=0, column=1, padx=5)

# Footer
footer = tk.Label(root, text="© 2025 Java Brew Coffee | Kasir Digital", bg="#fdf6f0", fg="#5a3e2b", font=("Arial", 9))
footer.pack(side="bottom", pady=10)

root.mainloop()
