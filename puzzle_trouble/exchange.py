import tkinter as tk
import subprocess

# Global variables to store click coordinates
click1 = None
click2 = None

# Function to calculate closest grid coordinates
def get_closest_coordinates(x, y):
    grid_size = 16
    grid_x = int(x / (canvas_width / grid_size))
    grid_y = int(y / (canvas_height / grid_size))
    return grid_x, grid_y

# Function to handle mouse clicks
def on_canvas_click(event):
    global click1, click2
    x, y = event.x, event.y
    grid_x, grid_y = get_closest_coordinates(x, y)
    #print("Clicked coordinates:", grid_x, grid_y)

    if click1 is None:
        click1 = format_coor((grid_y, grid_x))
    elif click2 is None:
        click2 = format_coor((grid_y, grid_x))
        call_script()

        # Reset click coordinates
        click1 = None
        click2 = None

# Function to format coordinates as four-digit numbers
def format_coor(coord):
    return f"{coord[0]:02d}{coord[1]:02d}"

# Function to call script.sh with click1 and click2 arguments
def call_script():
    if click1 is not None and click2 is not None:
        subprocess.run(["./simple_swap.sh", str(click1), str(click2)])
        #pause(0.2)
        refresh_canvas()  # Refresh the canvas after calling the script
        #root.after(200, refresh_canvas)  # Wait 0.2 seconds and then refresh the canvas

# Function to refresh the canvas by clearing and redrawing the modified image
def refresh_canvas():
    global image
    canvas.delete("all")  # Clear all items on the canvas
    # Reload the modified image
    image_path = "output.png"  # Update with the path to the modified image
    image = tk.PhotoImage(file=image_path)
    canvas.create_image(0, 0, anchor="nw", image=image)  # Redraw the modified image


# Create Tkinter window
root = tk.Tk()
root.title("Image Grid")

# Load image
image_path = "output.png"  # Update with your image file path
image = tk.PhotoImage(file=image_path)

# Get image dimensions
image_width = image.width()
image_height = image.height()

# Create canvas
canvas_width = image_width
canvas_height = image_height
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Display image on canvas
canvas.create_image(0, 0, anchor="nw", image=image)

# Bind click event to canvas
canvas.bind("<Button-1>", on_canvas_click)

# Run the Tkinter event loop
root.mainloop()

