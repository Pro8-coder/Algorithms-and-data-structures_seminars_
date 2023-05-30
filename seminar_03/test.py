from MyLinkedList import MyLinkedList

# Создание пустого списка:
my_list = MyLinkedList()
print(my_list)
# Добавление элементов в список:
my_list.add(1)
my_list.add(2)
my_list.add(3)
print(my_list)
# Получение размера списка:
size = my_list.size()
print(size)
# Проверка наличия элемента в списке:
contains = my_list.contains(2)
print(contains)
# Получение элемента по индексу:
element = my_list.get(1)
print(element)
# Создание нового списка с обратным порядком элементов:
new_list = my_list.reversed()
print(new_list, my_list)
print(id(new_list), id(my_list))
# Удаление элемента по значению:
my_list.remove(2)
print(my_list)
# Удаление последнего элемента:
my_list.popLast()
print(my_list)
