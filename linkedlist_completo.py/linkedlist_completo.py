#!/usr/bin/python
# -*- coding: utf-8 -*


class OutOfBoundsException(Exception):
    pass


class ListaException(Exception):
    pass


class LinkedListNode(object):
    """
    Nó de uma lista ligada. Esta estrutura recebe um valor
    e o apontador para o próximo nó, que pode ser nulo
    """

    def __init__(self, value, next=None):
        """
        value = valor do nó atual
        next = apontador para próximo nó
        """
        self._value = value
        self._next = next

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


class LinkedList(object):
    def __init__(self):
        """
        Construtor de lista ligada. A lista sempre começa vazia
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

        node = LinkedListNode(value)

        if self._head:
            pointer = self._head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node
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

        node = LinkedListNode(value)

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
        elif firstNode:
            self._head = firstNode.next
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
    ll = LinkedList()

    assert (ll.head is None)
    assert (ll.tail is None)
    assert (ll.toList() == [])
    ll.append(1)
    assert (ll.head == 1)
    assert (ll.tail == 1)
    assert (len(ll) == 1)
    assert (ll.toList() == [1])
    ll.append(2)
    assert (ll.head == 1)
    assert (ll.tail == 2)
    assert (len(ll) == 2)
    assert (ll.toList() == [1, 2])
    ll.append(3)
    assert (ll.head == 1)
    assert (ll.tail == 3)
    assert (len(ll) == 3)
    assert (ll.toList() == [1, 2, 3])
    """precisei inserir um teste do getValue e de exceção aqui"""
    assert (ll.getValueAt(0) == 1)
    try:
        ll.getValueAt(4)
    except ListaException:
        assert True
    else:
        assert False
    ll.insert(0)
    assert (ll.head == 0)
    assert (ll.tail == 3)
    assert (len(ll) == 4)
    assert (ll.toList() == [0, 1, 2, 3])
    ll.insert(-1)
    assert (ll.toList() == [-1, 0, 1, 2, 3])
    v = ll.removeFirst()
    assert (v == -1)
    assert (ll.toList() == [0, 1, 2, 3])
    v = ll.removeFirst()
    assert (v == 0)
    assert (ll.toList() == [1, 2, 3])
    v = ll.removeFirst()
    assert (v == 1)
    assert (ll.toList() == [2, 3])
    v = ll.removeFirst()
    assert (v == 2)
    assert (ll.toList() == [3])
    v = ll.removeFirst()
    assert (v == 3)
    assert (ll.toList() == [])
    """precisei inserir um teste de exceção aqui"""
    try:
        ll.removeFirst()
    except ListaException:
        assert True
    else:
        assert False
    assert (len(ll) == 0)
    print("100%")
