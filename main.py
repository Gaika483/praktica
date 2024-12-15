from tkinter import *
import tkinter as tk
def inf_predpriyatiya ():
    print("процент  не выполненой работы")
    predpriyatiya = [
        {'название': 'Предприятие 1', 'план': 1000, 'реально': 900},
        {'название': 'Предприятие 2', 'план': 2000, 'реально': 1800},
        {'название': 'Предприятие 3', 'план': 1500, 'реально': 1200},
        {'название': 'Предприятие 4', 'план': 3000, 'реально': 2500},
        {'название': 'Предприятие 5', 'план': 1200, 'реально': 1300},
        {'название': 'Предприятие 6', 'план': 500, 'реально': 500},
        {'название': 'Предприятие 7', 'план': 800, 'реально': 600},
        {'название': 'Предприятие 8', 'план': 400, 'реально': 300},
        {'название': 'Предприятие 9', 'план': 2500, 'реально': 2450},
        {'название': 'Предприятие 10', 'план': 2000, 'реально': 1900},
    ]
    print(f"{'Предприятие':<20}{'Процент недовыполнения (%)'}")
    for pred in predpriyatiya:
        if pred['реально'] < pred['план']:
            nedovipolnenie = ((pred['план'] - pred['реально']) / pred['план']) * 100
            print(f"{pred['название']:<20}{nedovipolnenie:.2f}")
    print()
def massif_s_null ():
    print("замена цифр между нулями")
    massiv = [5, 0, 3, 4, 0, 7, 8, 0]
    indeks_0_1 = massiv.index(0)
    indeks_0_2 = massiv.index(0, indeks_0_1 + 1)
    for i in range(indeks_0_1 + 1, indeks_0_2):
        massiv[i] = 1
    print(massiv)
    print()
def postavki():
    print("поставщики и поставки")
    postavshiki = ['Поставщик 1', 'Поставщик 2', 'Поставщик 3']
    obem_postavok = [100, 200, 150]
    potrebiteli = ['Потребитель 1', 'Потребитель 2', 'Потребитель 3']
    obem_potrebleniya = [200, 150, 100]
    ravnye_obemy = []
    for i in range(len(postavshiki)):
        for j in range(len(potrebiteli)):
            if obem_postavok[i] == obem_potrebleniya[j]:
                ravnye_obemy.append((postavshiki[i], potrebiteli[j], obem_postavok[i]))
    print("Поставщик\tПотребитель\tОбъем")
    for postavshik, potrebitel, obem in ravnye_obemy:
        print(f"{postavshik}\t{potrebitel}\t{obem}")
    print()

root = Tk()
root.title("меню программ командной работы")
root.geometry("300x200")

main_menu = Menu()
btn_recursion = tk.Button(text="Предприятие", width=25, height=2, bg='#999999')
btn_recursion.pack(pady=10)

btn_matrix = tk.Button(text="заменна цифр между 0", width=25, height=2, bg='#999999')
btn_matrix.pack(pady=10)

btn_calculate = tk.Button(text="поставщики и потребители", width=25, height=2, bg='#999999')
btn_calculate.pack(pady=10)

btn_recursion.config(command=inf_predpriyatiya)
btn_matrix.config(command=massif_s_null)
btn_calculate.config(command=postavki)

root.config(menu=main_menu)
root.mainloop()