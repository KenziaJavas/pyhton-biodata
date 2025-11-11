import tkinter as tk
from tkinter import messagebox

# Data menu dan harga
menu = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Bakar": 18000,
    "Soto Ayam": 13000,
    "Es Teh": 5000,
    "Es Jeruk": 6000,
    "Air Mineral": 4000
}

# Fungsi untuk menambahkan pesanan
def tambah_pesanan():
    makanan = listbox_menu.get(tk.ACTIVE)
    try:
        jumlah = int(entry_jumlah.get())
        if jumlah <= 0:
            raise ValueError
        subtotal = menu[makanan] * jumlah
        pesanan_list.insert(tk.END, f"{makanan} x{jumlah} = Rp{subtotal:,}")
        global total
        total += subtotal
        label_total.config(text=f"Total: Rp{total:,}")
        entry_jumlah.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Input Salah", "Masukkan jumlah yang valid!")

# Fungsi untuk reset pesanan
def reset_pesanan():
    global total
    pesanan_list.delete(0, tk.END)
    total = 0
    label_total.config(text="Total: Rp0")

# Setup GUI
root = tk.Tk()
root.title("💸 Kantin Digital Sekolah")
root.geometry("480x500")
root.config(bg="#f5f5f5")

title = tk.Label(root, text="🍱 Kantin Sekolah", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
title.pack(pady=10)

# Frame menu
frame_menu = tk.Frame(root, bg="#f5f5f5")
frame_menu.pack(pady=5)

tk.Label(frame_menu, text="Pilih Menu:", font=("Arial", 12, "bold"), bg="#f5f5f5").grid(row=0, column=0, sticky="w")
listbox_menu = tk.Listbox(frame_menu, width=30, height=8, font=("Arial", 11))
for item, harga in menu.items():
    listbox_menu.insert(tk.END, f"{item} - Rp{harga:,}")
listbox_menu.grid(row=1, column=0, padx=10, pady=5)

# Entry jumlah
frame_jumlah = tk.Frame(root, bg="#f5f5f5")
frame_jumlah.pack(pady=5)
tk.Label(frame_jumlah, text="Jumlah:", font=("Arial", 11), bg="#f5f5f5").grid(row=0, column=0)
entry_jumlah = tk.Entry(frame_jumlah, width=10)
entry_jumlah.grid(row=0, column=1, padx=5)
btn_tambah = tk.Button(frame_jumlah, text="Tambah", command=tambah_pesanan, bg="#4CAF50", fg="white", width=10)
btn_tambah.grid(row=0, column=2, padx=5)

# Daftar pesanan
tk.Label(root, text="Pesanan:", font=("Arial", 12, "bold"), bg="#f5f5f5").pack()
pesanan_list = tk.Listbox(root, width=40, height=8, font=("Arial", 11))
pesanan_list.pack(pady=5)

# Total dan tombol reset
label_total = tk.Label(root, text="Total: Rp0", font=("Arial", 13, "bold"), bg="#f5f5f5", fg="#000")
label_total.pack(pady=10)
btn_reset = tk.Button(root, text="Reset Pesanan", command=reset_pesanan, bg="#f44336", fg="white", width=15)
btn_reset.pack()

# Variabel total
total = 0

root.mainloop()
