import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox

# Conversion constant
FT_TO_IN = 12

def calculate_bricks():
    """Calculate bricks needed for a wall, subtracting windows and doors."""
    try:
        # ---------- Get all inputs from the user ----------
        wall_height_ft = float(entry_height.get())
        wall_width_ft  = float(entry_width.get())
        brick_thickness_in = float(entry_thickness.get())

        win_height_ft = float(entry_win_height.get() or 0)
        win_width_ft  = float(entry_win_width.get() or 0)
        door_height_ft = float(entry_door_height.get() or 0)
        door_width_ft  = float(entry_door_width.get() or 0)

        # ---------- Validate ----------
        if wall_height_ft <= 0 or wall_width_ft <= 0 or brick_thickness_in <= 0:
            raise ValueError("Wall dimensions and brick thickness must be positive.")
        if win_height_ft < 0 or win_width_ft < 0 or door_height_ft < 0 or door_width_ft < 0:
            raise ValueError("Opening dimensions cannot be negative.")

        # ---------- Convert wall to inches (for brick calculation) ----------
        wall_height_in = wall_height_ft * FT_TO_IN
        wall_width_in  = wall_width_ft * FT_TO_IN
        win_height_in  = win_height_ft * FT_TO_IN
        win_width_in   = win_width_ft * FT_TO_IN
        door_height_in = door_height_ft * FT_TO_IN
        door_width_in  = door_width_ft * FT_TO_IN

        # ---------- Brick face area (square bricks) ----------
        brick_area = brick_thickness_in * brick_thickness_in

        # ---------- Areas in square feet (for display) ----------
        wall_area_sqft = wall_height_ft * wall_width_ft
        win_area_sqft  = win_height_ft * win_width_ft
        door_area_sqft = door_height_ft * door_width_ft
        total_openings_sqft = win_area_sqft + door_area_sqft

        # ---------- Areas in square inches (for brick calculation) ----------
        wall_area_in = wall_height_in * wall_width_in
        win_area_in  = win_height_in * win_width_in
        door_area_in = door_height_in * door_width_in
        total_openings_in = win_area_in + door_area_in

        if total_openings_in > wall_area_in:
            raise ValueError("Openings are larger than the wall area!")

        net_area_in = wall_area_in - total_openings_in

        # ---------- NumPy calculations ----------
        bricks_without_openings = np.floor(wall_area_in / brick_area)
        bricks_with_openings    = np.floor(net_area_in / brick_area)
        bricks_saved = bricks_without_openings - bricks_with_openings

        # ---------- Update display (all areas in sq ft) ----------
        result_wall_area.set(f"Wall area: {wall_area_sqft:.2f} sq ft")
        result_openings.set(f"Openings area: {total_openings_sqft:.2f} sq ft")
        result_without.set(f"Bricks without openings: {int(bricks_without_openings)}")
        result_with.set(f"Bricks with openings: {int(bricks_with_openings)}")
        result_saved.set(f"Bricks saved: {int(bricks_saved)}")

    except ValueError as e:
        messagebox.showerror("Input Error", f"Please enter valid numbers.\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("🧱 Brick Calculator with Openings 🧱")
root.geometry("750x600")
root.resizable(False, False)

# Styling
bg_color = "#f0f4f8"
fg_color = "#2c3e50"
accent_color = "#3498db"
button_color = "#2980b9"
font_title = ("Helvetica", 20, "bold")
font_label = ("Helvetica", 12)
font_result = ("Helvetica", 14, "bold")

root.configure(bg=bg_color)

# Title
title_label = tk.Label(
    root,
    text="🏗️  Wall Brick Calculator with Openings  🏗️",
    font=font_title,
    bg=bg_color,
    fg=fg_color
)
title_label.pack(pady=15)

# Main input frame
main_frame = tk.Frame(root, bg=bg_color)
main_frame.pack(pady=10)

# Wall section
wall_frame = tk.LabelFrame(main_frame, text="Wall Dimensions", font=font_label, bg=bg_color, fg=fg_color, padx=15, pady=10)
wall_frame.grid(row=0, column=0, padx=20, pady=10, sticky="n")

tk.Label(wall_frame, text="Height (ft):", font=font_label, bg=bg_color, fg=fg_color).grid(row=0, column=0, sticky="w", pady=5)
entry_height = ttk.Entry(wall_frame, width=15, font=font_label)
entry_height.grid(row=0, column=1, padx=10, pady=5)
entry_height.insert(0, "8")

tk.Label(wall_frame, text="Width (ft):", font=font_label, bg=bg_color, fg=fg_color).grid(row=1, column=0, sticky="w", pady=5)
entry_width = ttk.Entry(wall_frame, width=15, font=font_label)
entry_width.grid(row=1, column=1, padx=10, pady=5)
entry_width.insert(0, "12")

# Brick section
brick_frame = tk.LabelFrame(main_frame, text="Brick Size", font=font_label, bg=bg_color, fg=fg_color, padx=15, pady=10)
brick_frame.grid(row=0, column=1, padx=20, pady=10, sticky="n")

tk.Label(brick_frame, text="Thickness (in):", font=font_label, bg=bg_color, fg=fg_color).grid(row=0, column=0, sticky="w", pady=5)
entry_thickness = ttk.Entry(brick_frame, width=15, font=font_label)
entry_thickness.grid(row=0, column=1, padx=10, pady=5)
entry_thickness.insert(0, "4")
tk.Label(brick_frame, text="(Square bricks assumed)", font=("Helvetica", 9, "italic"), bg=bg_color, fg="#7f8c8d").grid(row=1, column=0, columnspan=2, pady=5)

# Openings frame
openings_frame = tk.LabelFrame(root, text="Openings (leave blank or 0 if none)", font=font_label, bg=bg_color, fg=fg_color, padx=20, pady=10)
openings_frame.pack(pady=10)

# Window
tk.Label(openings_frame, text="Window Height (ft):", font=font_label, bg=bg_color, fg=fg_color).grid(row=0, column=0, sticky="w", pady=5)
entry_win_height = ttk.Entry(openings_frame, width=10, font=font_label)
entry_win_height.grid(row=0, column=1, padx=5, pady=5)
entry_win_height.insert(0, "2")

tk.Label(openings_frame, text="Window Width (ft):", font=font_label, bg=bg_color, fg=fg_color).grid(row=0, column=2, sticky="w", pady=5, padx=(20,0))
entry_win_width = ttk.Entry(openings_frame, width=10, font=font_label)
entry_win_width.grid(row=0, column=3, padx=5, pady=5)
entry_win_width.insert(0, "2")

# Door
tk.Label(openings_frame, text="Door Height (ft):", font=font_label, bg=bg_color, fg=fg_color).grid(row=1, column=0, sticky="w", pady=5)
entry_door_height = ttk.Entry(openings_frame, width=10, font=font_label)
entry_door_height.grid(row=1, column=1, padx=5, pady=5)
entry_door_height.insert(0, "7")

tk.Label(openings_frame, text="Door Width (ft):", font=font_label, bg=bg_color, fg=fg_color).grid(row=1, column=2, sticky="w", pady=5, padx=(20,0))
entry_door_width = ttk.Entry(openings_frame, width=10, font=font_label)
entry_door_width.grid(row=1, column=3, padx=5, pady=5)
entry_door_width.insert(0, "4")

# Calculate button
calculate_btn = tk.Button(
    root,
    text="🔨 Calculate Bricks 🔨",
    font=("Helvetica", 14, "bold"),
    bg=button_color,
    fg="white",
    activebackground="#1f618d",
    activeforeground="white",
    padx=20,
    pady=8,
    relief=tk.RAISED,
    bd=3,
    command=calculate_bricks
)
calculate_btn.pack(pady=15)

# Result frame
result_frame = tk.Frame(root, bg=bg_color)
result_frame.pack(pady=10)

result_wall_area = tk.StringVar()
result_openings = tk.StringVar()
result_without = tk.StringVar()
result_with = tk.StringVar()
result_saved = tk.StringVar()

result_wall_area.set("Wall area: —")
result_openings.set("Openings area: —")
result_without.set("Bricks without openings: —")
result_with.set("Bricks with openings: —")
result_saved.set("Bricks saved: —")

# Result labels
tk.Label(result_frame, textvariable=result_wall_area, font=font_result, bg=bg_color, fg=accent_color).pack()
tk.Label(result_frame, textvariable=result_openings, font=font_result, bg=bg_color, fg=accent_color).pack()
tk.Label(result_frame, textvariable=result_without, font=font_result, bg=bg_color, fg=accent_color).pack()
tk.Label(result_frame, textvariable=result_with, font=font_result, bg=bg_color, fg=accent_color).pack()
tk.Label(result_frame, textvariable=result_saved, font=font_result, bg=bg_color, fg=accent_color).pack()

# Footer
footer_label = tk.Label(
    root,
    text="Calculations use NumPy's floor function. Bricks assumed square.",
    font=("Helvetica", 9),
    bg=bg_color,
    fg="#7f8c8d"
)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Start GUI loop
root.mainloop()