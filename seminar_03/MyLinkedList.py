"""
Реализовать в классе MyLinkedList следующие методы
1. public int size() - получение размера списка, проитерироваться по всей
структуре
1.1 * Можно завести переменную size, поддерживать ее и использовать ее.
2. public boolean contains(int value) - проверка наличия элемента по значению
3. public int popLast() - удаление последнего элемента. Если список пустой -
то ошибка
4. * Переделать все int значения на дженерик T, чтобы можно было хранить
значения любых типов
5. * public MyLinkedList reversed() - создать НОВЫЙ список, порядок в котором
обратный текущему
"""


class MyLinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(str(node.value))
            node = node.next
        return ' -> '.join(values)

    def add(self, value):
        node = self.Node(value)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def remove(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                if current.next is None:
                    self.tail = previous
                else:
                    current.next.prev = previous
                self.length -= 1
                return True
            previous = current
            current = current.next
        return False

    def size(self):
        return self.length

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def popLast(self):
        if self.length == 0:
            raise Exception("List is empty")
        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next
        if previous is not None:
            previous.next = None
        else:
            self.head = None
        self.tail = previous
        self.length -= 1
        return current.value

    def reversed(self):
        new_list = MyLinkedList()
        current = self.tail
        while current is not None:
            new_list.add(current.value)
            current = current.prev
        return new_list
