import tkinter as tk
from tkinter import ttk, messagebox

def calculate_new_lot_size(current_lot_size, current_loss, risk_amount):
    return current_lot_size * (risk_amount / current_loss)

class LotSizeCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Lot Size Calculator")
        master.geometry("300x200")
        master.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')

        self.frame = ttk.Frame(master, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(self.frame, text="Current Lot Size:").grid(column=0, row=0, sticky=tk.W, pady=5)
        self.current_lot_size = ttk.Entry(self.frame, width=15)
        self.current_lot_size.grid(column=1, row=0, sticky=tk.E, pady=5)

        ttk.Label(self.frame, text="Current Loss:").grid(column=0, row=1, sticky=tk.W, pady=5)
        self.current_loss = ttk.Entry(self.frame, width=15)
        self.current_loss.grid(column=1, row=1, sticky=tk.E, pady=5)

        ttk.Label(self.frame, text="Risk Amount:").grid(column=0, row=2, sticky=tk.W, pady=5)
        self.risk_amount = ttk.Entry(self.frame, width=15)
        self.risk_amount.grid(column=1, row=2, sticky=tk.E, pady=5)

        self.calculate_button = ttk.Button(self.frame, text="Calculate", command=self.calculate)
        self.calculate_button.grid(column=0, row=3, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.frame, text="")
        self.result_label.grid(column=0, row=4, columnspan=2, pady=5)

    def calculate(self):
        try:
            current_lot_size = float(self.current_lot_size.get())
            current_loss = float(self.current_loss.get())
            risk_amount = float(self.risk_amount.get())

            new_lot_size = calculate_new_lot_size(current_lot_size, current_loss, risk_amount)
            self.result_label.config(text=f"New Lot Size: {new_lot_size:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields.")

def main():
    root = tk.Tk()
    LotSizeCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()