hoursFlaming = 2  # количество часов, которое горит бенгальская палочка
c1 = int(input('Введите количество новых бенгальских огней: '))

b1 = int(input('Сколько использованных бенгальских огней Игорю нужно для создания 2 новых?'))

result = int((hoursFlaming * c1) + int(2 * (c1 / int((b1 / 2))))) 
print(f'При оптимальном использовании бенгальских огней Игорь будет наблюдать огонек {result}')