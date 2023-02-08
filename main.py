from tkinter import *

# Configurações da janela principal
window = Tk()
window.title('Calculadora de IMC')
window.geometry('295x230')
window.config(bg='black')
# Cores
cor1 = '#ffffff'  # branca
cor2 = 'black'  # preta
cor3 = '#DB4437'  # Vermelha

# Calculos e Lógica do app


def calculate():
    weight = float(e_weight.get())
    height = float(e_height.get())
    imc = round(weight / (height ** 2), 2)

    if imc < 18.5:
        l_result_text['text'] = 'Seu IMC é: Abaixo do peso'
    elif imc >= 18.5 and imc <= 24.9:
        l_result_text['text'] = 'Seu IMC é: Normal'
    elif imc >= 25 and imc <= 29.9:
        l_result_text['text'] = 'Seu IMC é: Sobrepeso'
    elif imc >= 30 and imc <= 39.9:
        l_result_text['text'] = 'Seu IMC é: Sobrepeso'
    else:
        l_result_text['text'] = 'Seu IMC é: Obsedidade Grave'

    l_result['text'] = imc


# Criando os Frames
frame_up = Frame(window, width=295, height=50, bg=cor2,
                 padx=0, pady=0, relief='flat')
frame_up.grid(row=0, column=0, sticky=NSEW)

frame_low = Frame(window, width=295, height=180,
                  bg=cor2, padx=0, pady=0, relief='flat')
frame_low.grid(row=1, column=0, sticky=NSEW)

# Configurando o Frame de cima
app_name = Label(frame_up, width=23, height=1, padx=0,
                 text='Calculadora de IMC', font=('Ivy 16 bold'), fg=cor3, relief='flat', anchor='center', bg=cor2)
app_name.place(x=0, y=0)

app_name = Label(frame_up, width=400, height=1, padx=0,
                 text='', font=('Ivy 1 '), fg=cor3, relief='flat', anchor='center', bg=cor3)
app_name.place(x=0, y=35)

# Configurando o Frame de baixo

# Configurando o Label e a entrada do peso
l_weight = Label(frame_low, height=1, padx=0,
                 text='Insira seu peso', font=('Ivy 10 bold'), fg=cor1, relief='flat', anchor='center', bg=cor2)
l_weight.grid(row=0, column=0, sticky=NSEW, padx=3, pady=10)
e_weight = Entry(frame_low, width=5, font=('Ivy 10 bold'),
                 relief='solid', justify='center')
e_weight.grid(row=0, column=1, sticky=NSEW, padx=3, pady=10)

# Configurando o Label e a entrada da altura
e_height = Label(frame_low, height=1, padx=0,
                 text='Insira sua altura', font=('Ivy 10 bold'), fg=cor1, relief='flat', anchor='center', bg=cor2)
e_height.grid(row=1, column=0, sticky=NSEW, padx=3, pady=10)
e_height = Entry(frame_low, width=5, font=('Ivy 10 bold'),
                 relief='solid', justify='center')
e_height.grid(row=1, column=1, sticky=NSEW, padx=3, pady=10)

# Configurando o Label do resultado
l_result = Label(frame_low, width=5, height=1, padx=6, pady=12,
                 text='', font=('Ivy 24 bold'), fg=cor1, relief='flat', anchor='center', bg=cor3)
l_result.place(x=170, y=10)

l_result_text = Label(frame_low, width=37, height=1, padx=0, pady=12,
                      text='', font=('Ivy 10 bold'), fg=cor1, relief='flat', anchor='center', bg=cor2)
l_result_text.place(x=0, y=85)

# Configurando o botão para efetuar o calculo
b_calculate = Button(frame_low, command=calculate, width=34, height=1, overrelief=SOLID,
                     text='Calcular', font=('Ivy 10 bold'), fg=cor1, relief='raised', anchor='center', bg=cor3)
b_calculate.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)

window.mainloop()
