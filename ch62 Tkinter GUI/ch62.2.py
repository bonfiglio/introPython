import tkinter as tk


# GUI window is a subclass of the basic tkinter Frame object
class HelloWorldFrame(tk.Frame):
    def __init__(self, master):
        # Call superclass constructor
        tk.Frame.__init__(self, master)
        # Place frame into main window
        self.grid()
        # Create label with "Hello World" text
        grlst = []
        s = int(input("Lato :"))
        for r in range(s * s):
            grlst.append(tk.Label(self, text=str((r + 1) % 2)))
            grlst[r].grid(row=r // s, column=r % s)


if __name__ == "__main__":
    # Create main window object
    root = tk.Tk()
    # Set title of window
    root.title("bit GRID!")
    # Instantiate HelloWorldFrame object
    hello_frame = HelloWorldFrame(root)
    # Start GUI
    hello_frame.mainloop()
