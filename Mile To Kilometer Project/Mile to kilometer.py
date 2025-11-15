from tkinter import *

def miles_to_km():
    ans = round(int(input.get()) * 1.60934, 2)
    main_value.config(text=f"{ans}")
    # calc_input *= 1.60934
    # print(calc_input)
    # return round(calc_input, 2)

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=100, height=100)
window.config(padx=30, pady=30)

input = Entry(width=10)
user_input = input.get()
input.grid(column=1, row=0)

miles = Label(text=" Miles")
miles.grid(column=2, row=0)

is_equal_to = Label(text=" is equal to")
is_equal_to.grid(column=0, row=1)

main_value = Label(text="0")
main_value.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
window.mainloop()