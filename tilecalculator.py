import numpy as np
import tkinter as tk
from tkinter import messagebox

class TileCalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("🧱 Tile Calculator")
        root.geometry("500x550")
        root.resizable(False, False)
        root.configure(bg="#f0f4f8")

        # Style configuration
        self.font_label = ("Segoe UI", 11)
        self.font_entry = ("Segoe UI", 11)
        self.font_result = ("Segoe UI", 12, "bold")
        self.bg_color = "#f0f4f8"
        self.entry_bg = "#ffffff"

        # Header
        header = tk.Label(root, text="🏠 Tile Calculator", font=("Segoe UI", 18, "bold"),
                          bg="#2c3e50", fg="white", pady=10)
        header.pack(fill=tk.X)

        # Main frame
        main_frame = tk.Frame(root, bg=self.bg_color, padx=30, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input fields
        self.create_input(main_frame, "📏 Room length (m):", 0)
        self.length_entry = self.entries[0]

        self.create_input(main_frame, "📐 Room width (m):", 1)
        self.width_entry = self.entries[1]

        self.create_input(main_frame, "🧱 Tile length (m):", 2)
        self.tile_length_entry = self.entries[2]

        self.create_input(main_frame, "🧱 Tile width (m):", 3)
        self.tile_width_entry = self.entries[3]

        self.create_input(main_frame, "💰 Price per tile ($):", 4)
        self.price_entry = self.entries[4]

        # Calculate button
        calc_btn = tk.Button(main_frame, text="Calculate", font=("Segoe UI", 12, "bold"),
                             bg="#27ae60", fg="white", padx=20, pady=8,
                             command=self.calculate_tiles)
        calc_btn.grid(row=5, column=0, columnspan=2, pady=20)

        # Results frame
        result_frame = tk.LabelFrame(main_frame, text=" Results ", font=("Segoe UI", 11, "bold"),
                                      bg=self.bg_color, fg="#2c3e50", padx=10, pady=10)
        result_frame.grid(row=6, column=0, columnspan=2, sticky="ew", pady=10)

        self.result_vars = {}
        labels = [
            ("📦 Total tiles needed:", "total_tiles"),
            ("💵 Total cost ($):", "total_cost"),
            ("🔢 Tiles along length:", "tiles_length"),
            ("🔢 Tiles along width:", "tiles_width")
        ]
        for i, (text, key) in enumerate(labels):
            lbl = tk.Label(result_frame, text=text, font=self.font_label, bg=self.bg_color, anchor="w")
            lbl.grid(row=i, column=0, sticky="w", pady=2)
            var = tk.StringVar(value="-")
            self.result_vars[key] = var
            val_lbl = tk.Label(result_frame, textvariable=var, font=self.font_result, bg=self.bg_color, fg="#2980b9")
            val_lbl.grid(row=i, column=1, sticky="w", padx=(20, 0), pady=2)

        # Footer
        footer = tk.Label(root, text="Made with NumPy & Tkinter", font=("Segoe UI", 9),
                          bg="#2c3e50", fg="#bdc3c7", pady=5)
        footer.pack(side=tk.BOTTOM, fill=tk.X)

    def create_input(self, parent, label_text, row):
        lbl = tk.Label(parent, text=label_text, font=self.font_label, bg=self.bg_color, anchor="w")
        lbl.grid(row=row, column=0, sticky="w", pady=8)
        entry = tk.Entry(parent, font=self.font_entry, bg=self.entry_bg, relief=tk.FLAT, bd=3)
        entry.grid(row=row, column=1, sticky="ew", padx=(10, 0), pady=8)
        parent.columnconfigure(1, weight=1)
        if not hasattr(self, 'entries'):
            self.entries = []
        self.entries.append(entry)

    def calculate_tiles(self):
        try:
            # Get values from entries
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            tile_length = float(self.tile_length_entry.get())
            tile_width = float(self.tile_width_entry.get())
            price = float(self.price_entry.get())

            # Validation
            if length <= 0 or width <= 0 or tile_length <= 0 or tile_width <= 0:
                messagebox.showerror("Invalid Input", "All dimensions must be positive.")
                return
            if price < 0:
                messagebox.showerror("Invalid Input", "Price cannot be negative.")
                return

            # NumPy calculations
            tiles_along_length = np.ceil(length / tile_length)
            tiles_along_width = np.ceil(width / tile_width)
            total_tiles = int(tiles_along_length * tiles_along_width)
            total_cost = total_tiles * price

            # Update results
            self.result_vars["total_tiles"].set(str(total_tiles))
            self.result_vars["total_cost"].set(f"${total_cost:.2f}")
            self.result_vars["tiles_length"].set(str(int(tiles_along_length)))
            self.result_vars["tiles_width"].set(str(int(tiles_along_width)))

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numeric values.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TileCalculatorApp(root)
    root.mainloop()