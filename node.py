class Node:

    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        if new_data > 0:
            self._data = new_data
        else:
            raise ValueError

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, new_next_node):
        self._next_node = new_next_node
