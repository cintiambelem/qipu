#!/usr/bin/python
# -*- coding: utf-8 -*


class OutOfBoundsException(Exception):
    pass


class ListaException(Exception):
    pass


class DoublyLinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """

    def __init__(self, value, ancestor=None, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        ancestor = apontador para nó anterior
        """
        self._value = value
        self._next = next
        self._ancestor = ancestor

    @property
    def value(self):
        """
        Retorna o valor do nó atual
        """
        return self._value

    @property
    def next(self):
        """
        Retorna o apontador para o próximo nó
        """
        return self._next

    @next.setter
    def next(self, node):
        """
        Define o apontador para o próximo nó
        """
        self._next = node

    def hasNext(self):
        """
        Retorna True se existir um próximo nó, False caso contrário
        """
        return self._next is not None

    @property
    def ancestor(self):
        """
        Retorna o apontador para o nó anterior
        """
        return self._ancestor

    @ancestor.setter
    def ancestor(self, node):
        """
        Define o apontador para o nó anterior
        """
        self._ancestor = node

    def hasAncestor(self):
        """
        Retorna True se existir um nó anterior, False caso contrário
        """
        return self._ancestor is not None


class DoublyLinkedList(object):
    def __init__(self):
        """
        Construtor de lista duplamente ligada. A lista sempre começa vazia
        """
        self._head = None  # Apontador para o nó cabeça (primeiro)
        self._tail = None  # Apontador para o nó filho (ultimo)
        self._len = 0  # contador

    def __len__(self):
        return self._len

    @property
    def head(self):
        """
        Esta propriedade deve retornar o valor do primeiro nó da lista ligada
        """
        if self._head:
            return self._head.value
        else:
            return None

    @property
    def tail(self):
        """
        Esta propriedade deve retornar o valor do último nó da lista ligada
        """
        if self._tail:
            return self._tail.value
        else:
            return None

    def append(self, value):
        """
        Esta função deve inserir um novo nó no FINAL da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - append(0) - [1, 2, 3, 0]
        """

        node = DoublyLinkedListNode(value)

        if self._tail:
            node.ancestor = self._tail
            self._tail.next = node
            self._tail = node
        else:
            self._head = node
            self._tail = node
        self._len += 1

    def insert(self, value):
        """
        Esta função deve inserir um novo nó no INICIO da lista ligada com valor value.
        Após a execução desta função a lista ligada deve ter um elemento a mais.

        Exemplo: [1, 2, 3] - insert(0) - [0, 1, 2, 3]
        """

        node = DoublyLinkedListNode(value)

        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head = node
        self._len += 1

    def removeFirst(self):
        """
        Esta função deve remover o primeiro elemento da lista e retornar o seu valor.
        Apos a execução, a lista ligada deve ter um elemento a menos.
        """
        firstNode = self._head

        if firstNode is None:
            raise ListaException("Primeiro elemento vazio")
        elif firstNode.hasNext():
            self._head = firstNode.next
            self._head.ancestor = None
        else:
            self._head = None
            self._tail = None
        self._len -= 1
        return firstNode.value

    def getValueAt(self, index):
        """
        Esta função deve retornar o valor de um nó na posição definida por INDEX.
        Se o index for maior do que o tamanho da lista, retornar OutOfBoundsException
        """
        pointer = self._head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise ListaException("Lista vazia")
        return pointer.value

    def toList(self):
        """
        Esta função retornar uma representação em forma de vetor ([1, 2, 3....])
        da lista ligada
        """
        lista = []
        node = self._head
        while node:
            lista.append(node.value)
            node = node.next
        return lista


if __name__ == "__main__":
    """
    Gabarito de execução e testes. Se o seu código passar e chegar até o final,
    possivelmente você implementou tudo corretamente
    """
    dll = DoublyLinkedList()

    assert (dll.head is None)
    assert (dll.tail is None)
    assert (dll.toList() == [])
    dll.append(1)
    assert (dll.head == 1)
    assert (dll.tail == 1)
    assert (len(dll) == 1)
    assert (dll.toList() == [1])
    dll.append(2)
    assert (dll.head == 1)
    assert (dll.tail == 2)
    assert (len(dll) == 2)
    assert (dll.toList() == [1, 2])
    dll.append(3)
    assert (dll.head == 1)
    assert (dll.tail == 3)
    assert (len(dll) == 3)
    assert (dll.toList() == [1, 2, 3])
    assert (dll.getValueAt(0) == 1)
    try:
        dll.getValueAt(4)
    except ListaException:
        assert True
    else:
        assert False
    dll.insert(0)
    assert (dll.head == 0)
    assert (dll.tail == 3)
    assert (len(dll) == 4)
    assert (dll.toList() == [0, 1, 2, 3])
    dll.insert(-1)
    assert (dll.toList() == [-1, 0, 1, 2, 3])
    v = dll.removeFirst()
    assert (v == -1)
    assert (dll.toList() == [0, 1, 2, 3])
    v = dll.removeFirst()
    assert (v == 0)
    assert (dll.toList() == [1, 2, 3])
    v = dll.removeFirst()
    assert (v == 1)
    assert (dll.toList() == [2, 3])
    v = dll.removeFirst()
    assert (v == 2)
    assert (dll.toList() == [3])
    v = dll.removeFirst()
    assert (v == 3)
    assert (dll.toList() == [])
    try:
        dll.removeFirst()
    except ListaException:
        assert True
    else:
        assert False
    assert (len(dll) == 0)
    print("100%")
