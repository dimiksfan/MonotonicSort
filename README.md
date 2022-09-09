# Сортировка вставками
```

def MonotonicSort(lst):
    for i in range(1, (len(lst))):
         tmp = lst[i]
         while (i > 0) and (tmp <= lst[i - 1]):
             lst[i] = lst[i-1]
             i -= 1
         else:
            lst[i] = tmp
    return(lst)

```
#### Функция состоит из двух циклов: 
   1. For - Внешний цикл функции, котроый начинает перебеирать элементы из lst c 1-ого элента, поскольку 0 элемент не с чем сравнивать. И взятый из списка элеменет записывается в переменную tmp.
   2. While - Внутренний цикл функции выполняет два условия:
   2.1. Номер элемента должен быть больше 0
   2.2. Взятый элемент должен быть меньше или равен предыдущего.
   Если условия выполнены, то элемент поменяет свой индекс на -1, то есть поменяется с предшетствующим. 
   В противном случае, взятый элемент вернется на место.

# Работа сортировки вставками с большими исходными данными.

```
|Количество элементов|Время сортировки|
|--------------------|----------------|
|1000                |0,13            |
|10000               |13,77           |
|20000               |54,73           |
```
