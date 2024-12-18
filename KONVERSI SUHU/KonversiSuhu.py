import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        # Ambil nilai suhu dari input
        temperature = float(entry_temperature.get())

        # Konversi sesuai pilihan pengguna
        if selected_unit.get() == "Celcius":
            result = temperature
        elif selected_unit.get() == "Fahrenheit":
            result = (temperature * 9/5) + 32
        elif selected_unit.get() == "Reamur":
            result = temperature * 4/5
        elif selected_unit.get() == "Kelvin":
            result = temperature + 273.15

        # Tampilkan hasil konversi
        result_str.set(f"Hasil Konversi: {result:.2f} {selected_unit.get()}")
    except ValueError:
        result_str.set("Masukkan angka yang valid!")

# Buat jendela Tkinter
root = tk.Tk()
root.title("Konversi Suhu")

# Label nama
label_name = ttk.Label(root, text="DANI FATURRAHMAN 220511045")
label_name.grid(row=0, column=1, pady=10)

# Buat variabel untuk menyimpan pilihan unit
selected_unit = tk.StringVar()
selected_unit.set("Celcius")

# Label dan input untuk suhu
label_temperature = ttk.Label(root, text="Masukkan Suhu:")
label_temperature.grid(row=1, column=0, padx=10, pady=10)
entry_temperature = ttk.Entry(root)
entry_temperature.grid(row=1, column=1, padx=10, pady=10)

# Pilihan unit suhu
unit_options = ["Celcius", "Fahrenheit", "Reamur", "Kelvin"]
label_unit = ttk.Label(root, text="Pilih Unit:")
label_unit.grid(row=2, column=0, padx=10, pady=10)
combo_unit = ttk.Combobox(root, values=unit_options, textvariable=selected_unit)
combo_unit.grid(row=2, column=1, padx=10, pady=10)
combo_unit.current(0)

# Tombol konversi
button_convert = ttk.Button(root, text="Konversi", command=convert_temperature)
button_convert.grid(row=3, column=0, columnspan=2, pady=10)

# Hasil konversi
result_str = tk.StringVar()
label_result = ttk.Label(root, textvariable=result_str)
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Jalankan aplikasi
root.mainloop()