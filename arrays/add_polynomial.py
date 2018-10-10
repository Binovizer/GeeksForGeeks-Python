class node:
    def __init__(self, coeff, pwr):
        self.coeff = coeff
        self.next = None
        self.power = pwr


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, coeff, pwr):
        if self.head is None:
            self.head = node(coeff, pwr)
        else:
            new_node = node(coeff, pwr)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node


def create_list(arr, n):
    lis = LinkedList()
    k = 0
    for i in range(n):
        lis.insert(arr[k], arr[k + 1])
        k += 2
    return lis.head


def add_polynomial(poly1, poly2):
    string = ''
    arr = [0] * 1000
    while poly1 is not None:
        arr[poly1.power - 1] += poly1.coef
        poly1 = poly1.next
    while poly2 is not None:
        arr[poly2.power - 1] += poly2.coef
        poly2 = poly2.next
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != 0:
            string += "{0}x^{1} + ".format(arr[i], i + 1)
    print(string.strip()[:-2])


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly1 = create_list(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly2 = create_list(arr, n)
        add_polynomial(poly1, poly2)