import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# Задана таблиця значень функції корисності
utility = np.array([0.14, 0.55, 0.66, 0.73, 0.78, 0.83, 0.87, 0.93, 0.98])
money = np.array([-3000, -1000, 0, 1000, 2000, 3000, 4000, 6000, 8000])

def calculate_risk():
    start_capital = float(start_capital_entry.get())
    bet_heads = float(bet_heads_entry.get())
    bet_tails = float(bet_tails_entry.get())

    # Оцінка результатів гри
    result_heads = start_capital + bet_heads
    result_tails = start_capital + bet_tails

    # Знаходження відповідних значень корисності для результатів гри
    index_heads = np.argmin(np.abs(money - result_heads))
    index_tails = np.argmin(np.abs(money - result_tails))

    utility_heads = utility[index_heads]
    utility_tails = utility[index_tails]

    # Визначення типу функції корисності (розрахунок похідної)
    derivative = np.diff(utility) / np.diff(money)

    if np.all(derivative > 0):
        risk_label.config(text="Функція корисності налаштована на ризик.")
    else:
        risk_label.config(text="Функція корисності не налаштована на ризик або є лінійною.")

    utility_heads_label.config(text=f"Корисність при ставці на орла (-1000): {utility_heads}")
    utility_tails_label.config(text=f"Корисність при ставці на решку (+1500): {utility_tails}")

    # Побудова графіку функції корисності
    plt.figure(figsize=(8, 6))
    plt.plot(money, utility, marker='o', linestyle='-', color='b')
    plt.xlabel('Гроші')
    plt.ylabel('Корисність')
    plt.title('Функція корисності')
    plt.grid(True)
    plt.scatter([result_heads, result_tails], [utility_heads, utility_tails], color='red')
    plt.legend(['Функція корисності', 'Ставка на орла', 'Ставка на решку'])

    # Виведення графіка
    plt.show()

    # Виведення повідомлення про схильність до ризику
    plt.figure(figsize=(6, 4))
    plt.plot(money[1:], derivative, marker='o', linestyle='-', color='g')
    plt.axhline(0, color='gray', linestyle='--')
    plt.xlabel('Гроші')
    plt.ylabel('Похідна корисності')
    plt.title('Тип функції корисності')
    plt.grid(True)
    plt.show()

# Створення вікна
root = tk.Tk()
root.title('Аналіз ризику')

# Віджети для введення даних та кнопка обчислення
start_capital_label = tk.Label(root, text='Стартовий капітал:')
start_capital_label.grid(row=0, column=0)
start_capital_entry = tk.Entry(root)
start_capital_entry.grid(row=0, column=1)

bet_heads_label = tk.Label(root, text='Ставка на орла:')
bet_heads_label.grid(row=1, column=0)
bet_heads_entry = tk.Entry(root)
bet_heads_entry.grid(row=1, column=1)

bet_tails_label = tk.Label(root, text='Ставка на решку:')
bet_tails_label.grid(row=2, column=0)
bet_tails_entry = tk.Entry(root)
bet_tails_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text='Обчислити', command=calculate_risk)
calculate_button.grid(row=3, columnspan=2)

# Віджети для виведення результатів та ризику
risk_label = tk.Label(root, text="")
risk_label.grid(row=4, columnspan=2)

utility_heads_label = tk.Label(root, text="")
utility_heads_label.grid(row=5, columnspan=2)

utility_tails_label = tk.Label(root, text="")
utility_tails_label.grid(row=6, columnspan=2)

root.mainloop()
