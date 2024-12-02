import customtkinter
from tkinter import messagebox
from plyer import notification
import time

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("BMI Calculator")
root.geometry("500x300")
root.resizable(False, False)


def get_details():
    height_str = entry_1.get()
    weight_str = entry_2.get()

    try:
        height = float(height_str) / 100  # Convert to meters
        weight = float(weight_str)
        result = round(weight / (height ** 2), 2)
        label_4.configure(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Invalid input. Please enter valid numbers.")

#FRAME1
frame_1  = customtkinter.CTkFrame(master=root,height=300,width=200)
frame_1.pack(fill='both',expand=True)

#LABEL
label = customtkinter.CTkLabel(master=frame_1,text="BMI Calculator",font=("helvetica",30))
label.pack(padx=10,pady=15)

# LABEL1
label_1 = customtkinter.CTkLabel(master=frame_1,text="Height")
label_1.place(x=12, y=70)

# ENTRY1
entry_1 = customtkinter.CTkEntry(master=frame_1,width=300,placeholder_text="Your Height in centimeters")
entry_1.place(x=123, y=78)

# LABEL2
label_2 = customtkinter.CTkLabel(master=frame_1,text="Weight")
label_2.place(x=12, y=120)

# ENTRY2
entry_2 = customtkinter.CTkEntry(master=frame_1,width=300,placeholder_text="Your Weight in kilograms")
entry_2.place(x=123, y=120)

# BUTTON1
button_1 = customtkinter.CTkButton(master=frame_1,text="Calculate BMI", command=get_details,
                                   width=20)
button_1.place(x=200, y=180)

#LABEL4
label_4 = customtkinter.CTkLabel(master=frame_1,text="",font=("Helvetica",15))
label_4.place(x=10,y=250)
