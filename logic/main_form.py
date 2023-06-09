import PySimpleGUI as sg
from logic.cfail_handler import Handler


'''
    При запуске этого скрипта:
        F()=> читаем и записываем в словарь сохраненные параметры и данные
        F()=> создаем форму и подставляем значения из словаря

    (V) Создаем форму
    ( ) 
'''


class MainForm:
    def __init__(self):
        hendler = Handler
        self.rider = hendler._reade_json
        self.writer = hendler._write_json
        pass

    def show(self):
        # Создаем поля для ввода и кнопки
        layout = [
            [sg.Text('Введите имя:'), sg.InputText(key='Mname')],
            [sg.Text('Введите свой возраст:'), sg.InputText(key='Mage')]
        ]
        btn = [
            [sg.Submit('Подать данные'),
             sg.Button('Выход!!!')]
        ]
        # создаем окно
        group = [[layout], [btn]]
        window = sg.Window("Test1").Layout(group)
        vvod={'Name': ['Mname'],
              'Age': ['Mage']
              }

        # Обработка данных
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Выход!!!':
                break
            if event == 'Подать данные':
                self.writer(values(vvod))
                print("Данные внесены!")
                break
        window.close()

