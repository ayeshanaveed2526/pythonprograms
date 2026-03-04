import numpy as np
FT_TO_IN = 12

def get_float(prompt, default=None, allow_zero=False):
    """Helper to get a float from user. If default is given and input is empty, return default."""
    while True:
        try:
            value_str = input(prompt).strip()
            if value_str == "" and default is not None:
                return float(default)
            value = float(value_str)
            if not allow_zero and value <= 0:
                print("Value must be positive. Please try again.")
                continue
            if allow_zero and value < 0:
                print("Value cannot be negative. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid number. Please enter a numeric value.")

def main():
    print("=" * 50)
    print("        BRICK CALCULATOR WITH OPENINGS")
    print("=" * 50)

    # Get wall dimensions
    print("\n--- Wall Dimensions ---")
    wall_height_ft = get_float("Wall height (ft): ")
    wall_width_ft  = get_float("Wall width (ft): ")

    # Get brick thickness
    print("\n--- Brick Size ---")
    brick_thickness_in = get_float("Brick thickness (in): ")
    print("(Square bricks assumed)")

    # Get window dimensions (optional)
    print("\n--- Window (optional) ---")
    win_height_ft = get_float("Window height (ft) [0 if none]: ", default=0, allow_zero=True)
    win_width_ft  = get_float("Window width (ft) [0 if none]: ", default=0, allow_zero=True)

    # Get door dimensions (optional)
    print("\n--- Door (optional) ---")
    door_height_ft = get_float("Door height (ft) [0 if none]: ", default=0, allow_zero=True)
    door_width_ft  = get_float("Door width (ft) [0 if none]: ", default=0, allow_zero=True)

    # Convert to inches for brick calculation
    wall_height_in = wall_height_ft * FT_TO_IN
    wall_width_in  = wall_width_ft * FT_TO_IN
    win_height_in  = win_height_ft * FT_TO_IN
    win_width_in   = win_width_ft * FT_TO_IN
    door_height_in = door_height_ft * FT_TO_IN
    door_width_in  = door_width_ft * FT_TO_IN

    # Brick face area (square bricks)
    brick_area = brick_thickness_in * brick_thickness_in

    # Areas in square feet (for display)
    wall_area_sqft = wall_height_ft * wall_width_ft
    win_area_sqft  = win_height_ft * win_width_ft
    door_area_sqft = door_height_ft * door_width_ft
    total_openings_sqft = win_area_sqft + door_area_sqft

    # Areas in square inches (for brick count)
    wall_area_in = wall_height_in * wall_width_in
    win_area_in  = win_height_in * win_width_in
    door_area_in = door_height_in * door_width_in
    total_openings_in = win_area_in + door_area_in

    # Check if openings exceed wall
    if total_openings_in > wall_area_in:
        print("\n❌ ERROR: Openings are larger than the wall area!")
        return

    net_area_in = wall_area_in - total_openings_in

    # NumPy calculations (floor)
    bricks_without_openings = np.floor(wall_area_in / brick_area)
    bricks_with_openings    = np.floor(net_area_in / brick_area)
    bricks_saved = bricks_without_openings - bricks_with_openings

    # Display results
    print("\n" + "=" * 50)
    print("RESULTS")
    print("=" * 50)
    print(f"Wall area:          {wall_area_sqft:.2f} sq ft")
    print(f"Openings area:      {total_openings_sqft:.2f} sq ft")
    print(f"Bricks without openings: {int(bricks_without_openings)}")
    print(f"Bricks with openings:    {int(bricks_with_openings)}")
    print(f"Bricks saved:            {int(bricks_saved)}")
    print("=" * 50)

if __name__ == "__main__":
    main()