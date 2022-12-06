import tkinter
import customtkinter
import math

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title('Calculator/Converter')
app.geometry('600x550')
app.resizable(False, False)

def calculate(operation):
    global formula
    num = txt_entry_dollar.get() #считываем c ввода доллара
    
    try:
        if operation == 'C':
            formula = '0'
        elif operation == 'del':
            formula = formula[0:-1]
        elif operation == 'X^2':
            formula = str((eval(formula)) ** 2)
        elif operation == '√':
            formula = (str(math.sqrt(eval(formula))))
        elif operation == 'Dollar':
            formula = str((eval(formula))/61.8)
        elif operation == 'X^3':
            formula = str((eval(formula)) ** 3) 
        elif operation == '=':
            formula = str(eval(formula))
        else:
            if formula == '0':
                formula = ''
            formula += operation
        label_text.configure(text=formula)

    except (ZeroDivisionError, Exception):
         formula = '0'
         label_text.configure(text=formula)

#Cоздаем лэйбл и поле ввода доллара
lbl_converter_dollar = tkinter.Label(app, text="курс доллара или евро", font=('Roboto', 15),  bg='gray10', fg='white')  
lbl_converter_dollar.place(x=17, y=115)

txt_entry_dollar = tkinter.Entry(app, width=4, bg ='gray40', font=('Roboto', 18), justify = 'center')
txt_entry_dollar.pack(anchor='nw', padx=240, pady= 117 )

lbl_converter_dollar_to_rub = tkinter.Label(app, text="рублей(тут ввод с клавиатуры)", font=('Roboto', 15),  bg='gray10', fg='white')  
lbl_converter_dollar_to_rub.place(x=300, y=115)



# Создание окна для вывода вычислений
formula = '0'
label_text = tkinter.Label(text=formula,  font=('Roboto', 50, 'bold'), bg='gray10', fg='white', anchor="e")
label_text.place(x=17, y=30)

# Use CTkButton instead of tkinter Button
buttons = ['C', 'del', '√', '*', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '.', '0', '00', '=']
x = 18
y = 140
for button in buttons:
    get_lbl = lambda x=button: calculate(x)
    button = customtkinter.CTkButton( master=app,text=button,font=('Roboto', 25), command=get_lbl)
    button.place(x=x, y=y, width=135, height=89)
    x += 117
    if x > 400:
        x = 18
        y += 81
        
buttons_new = ['(', ')', 'X^2', 'X^3','Dollar']
x = 486
y = 140
for button in buttons_new:
    get_lbl = lambda x=button: calculate(x)
    button = customtkinter.CTkButton( master=app,text=button,font=('Roboto', 25), command=get_lbl)
    button.place(x=x, y=y, width=115, height=89)
    
    x += 117
    if x > 500:
        x = 486
        y += 81

app.mainloop()
