import PySimpleGUI as sg
import os
from threading import Thread
sg.theme('reddit')

# Interface Gráfica
layout_principal = [
    [sg.Text('Calculadora de IMC')],
    [sg.Text('Digite seu peso em kg'), sg.Input(key='peso')],
    [sg.Text('Digite sua altura em metros'), sg.Input(key='altura')],
    [sg.Button('Calcular IMC', key='imc_calculator')],
    [sg.Text('', key='result_number')],
    [sg.Text('', key='result_text')]
]


window = sg.Window(title='Calculadora de IMC', layout=layout_principal)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'imc_calculator':
        peso = int(values['peso'])
        altura = float(values['altura'])
        imc = peso/(altura**2)
        window['result_number'].update("%.2f" % imc)
        if imc < 17:
            window['result_text'].update(
                'Muito abaixo do peso', text_color='red')
        elif imc <= 18.5:
            window['result_text'].update('Abaixo do peso', text_color='orange')
        elif imc <= 24.9:
            window['result_text'].update('Peso normal', text_color='green')
        elif imc <= 29.9:
            window['result_text'].update('Acima do peso', text_color='orange')
        elif imc < 34.9:
            window['result_text'].update('Obesidade I', text_color='red')
        elif imc < 39.9:
            window['result_text'].update(
                'Obesidade II(severa)', text_color='red')
        else:
            window['result_text'].update(
                'Obesidade III(mórbida)', text_color='red')
