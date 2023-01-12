class Node:
    """Defines a node of a singly-linked list"""
    def __init__(self, data, next_node=None):
        """
        Initializes the class
        Args:
            data represents items on the list.
            next_node represents the temporary node.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for data.
        Raises TypeError if value is not integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for next_node.
        Raises TypeError if value is not Node or None.
        """
        if value is not None or type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """
        Initializes singly linked list
        Attributes:
            head: private
        """
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """
        String representation of singly linked list needed to print
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string
        # values = []
        # tmp = self.__head
        # while tmp is not None:
        #     values.append(str(tmp.data))
        #     tmp = tmp.next_node
        # return ('\n'.join(values))


# sll = SinglyLinkedList()
# sll.sorted_insert(2)
# sll.sorted_insert(5)
# sll.sorted_insert(3)
# sll.sorted_insert(10)
# sll.sorted_insert(1)
# sll.sorted_insert(-4)
# sll.sorted_insert(-3)
# sll.sorted_insert(4)
# sll.sorted_insert(5)
# sll.sorted_insert(12)
# sll.sorted_insert(3)
# print(sll)
