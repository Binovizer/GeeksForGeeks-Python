class Node:
    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def __repr__(self):
        return '<Node data: {},  left: {}, right: {}>'.format(self._data, self._left, self._right)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @data.deleter
    def data(self):
        del self._data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        self._left = left

    @left.deleter
    def left(self):
        del self._left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @right.deleter
    def right(self):
        del self._right
