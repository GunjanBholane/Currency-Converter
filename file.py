import tkinter as tk
from tkinter import *
import tkinter.messagebox
import webbrowser
from currency_converter import CurrencyConverter

root = tk.Tk()
root.title("Currency Conversion")

Tops = Frame(root, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
Tops.grid(row=0, column=1)

headlabel = tk.Label(Tops, font=('lato black', 25, 'bold'), text='Currency Converter ', bg='#FFFFFF', fg='black')
headlabel.grid(row=1, column=1, sticky=W)

variable1 = tk.StringVar(root)
variable2 = tk.StringVar(root)
variable1.set("Select Currency")
variable2.set("Select Currency")

CurrencyCountryMap = {
    "INR": "Indian Rupee",
    "USD": "United States Dollar",
    "CAD": "Canadian Dollar",
    "CNY": "Chinese Yuan",
    "DKK": "Danish Krone",
    "EUR": "Euro",
    "BRL": "Brazilian Real",
    "CHF": "Swiss Franc",
    "GBP": "British Pound Sterling",
    "SGD": "Singapore Dollar",
    "TRY": "Turkish Lira",
    "ZAR": "South African Rand",
    "AUD": "Australian Dollar",
    "MXN": "Mexican Peso",
    "NOK": "Norwegian Krone",
    "HKD": "Hong Kong Dollar",
    "THB": "Thai Baht",
    "MYR": "Malaysian Ringgit",
    "HUF": "Hungarian Forint",
    "BGN": "Bulgarian Lev",
    "RON": "Romanian Leu",
    "SEK": "Swedish Krona",
    "PLN": "Polish Zloty",
    "CZK": "Czech Koruna"
}

def RealTimeCurrencyConversion():
    c = CurrencyConverter()
    from_currency = variable1.get()
    to_currency = variable2.get()
    amount = Amount1_field.get()
    
    if amount == "":
        tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please enter a valid amount.")
    elif from_currency == "Select Currency" or to_currency == "Select Currency":
        tkinter.messagebox.showinfo("Error !!",
                                    "Currency Not Selected.\n Please select FROM and TO Currency from menu.")
    else:
        try:
            new_amt = c.convert(float(amount), from_currency, to_currency)
            new_amount = float("{:.4f}".format(new_amt))
            Amount2_field.delete(0, END)
            Amount2_field.insert(0, str(new_amount))
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error during conversion: {str(e)}")

def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)

def open_web_page():
    webbrowser.open(r'D:\xblog\pythonpro\CC\cc1.html')  # Using raw string literal

root.configure(background='#FFFFFF')
root.geometry("1000x500")

Label_1 = Label(root, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#FFFFFF", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Enter Amount  :  ", bg="#FFFFFF", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    From Currency  :  ", bg="#FFFFFF", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    To Currency  :  ", bg="#FFFFFF", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = tk.Label(root, font=('lato black', 15, 'bold'), text="\t    Converted Amount  :  ", bg="#FFFFFF", fg="black")
label1.grid(row=8, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#FFFFFF", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#FFFFFF", fg="black")
Label_1.grid(row=7, column=1, sticky=W)

FromCurrency_option = tk.OptionMenu(root, variable1, *CurrencyCountryMap.keys())
ToCurrency_option = tk.OptionMenu(root, variable2, *CurrencyCountryMap.keys())
FromCurrency_option.config(width=15)  # Fixed width for option menu
ToCurrency_option.config(width=15)  # Fixed width for option menu
FromCurrency_option.grid(row=3, column=2, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=2, ipadx=45, sticky=E)

Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=2, ipadx=45, sticky=E)

Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=2, ipadx=45, sticky=E)

link_label = Label(root, text="Country Names", fg="blue", cursor="hand2", bg="#FFFFFF")
link_label.grid(row=6, column=2)
link_label.bind("<Button-1>", lambda e: open_web_page())

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#FFFFFF", fg="black")
Label_1.grid(row=9, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 17, 'bold'), text="   Convert  ", padx=2, pady=2, bg="#015D82", fg="white",
                 command=RealTimeCurrencyConversion)
Label_9.grid(row=7, column=1)

Label_1 = Label(root, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#FFFFFF", fg="black")
Label_1.grid(row=11, column=0, sticky=W)

Label_9 = Button(root, font=('arial', 17, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="#015D82", fg="white",
                 command=clear_all)
Label_9.grid(row=12, column=1)

root.mainloop()
