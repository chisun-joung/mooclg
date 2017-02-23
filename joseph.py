
import collections


class LinkedNode(object):
    def __init__(self, value):
        self.next = None
        self.value = value

class CircularLinkedList(collections.abc.Iterable):


    def __init__(self):
        self.last = None

    def append(self, value):
        new_node = LinkedNode(value)
        self._insert_after(self.last, new_node)
        self.last = new_node

    def _insert_after(self, node, new_node):
        if not node:
            new_node.next = new_node
        else:
            new_node.next = node.next
            node.next = new_node

    def insert(self, value, index=0):
        new_node = LinkedNode(value)
        for i, node in enumerate(self._iter_nodes()):
            if i == index:
                self._insert_after(node, new_node)
        else:
            raise IndexError(index)
        if not self.last:
            self.last = new_node

    def pop(self, index=0):
        if not self.last:
            raise IndexError(index)
        if index == 0:
            node = self.last.next
            if node is self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
            return node.value
        for i, node in enumerate(self._iter_nodes(), 1):
            if i == index:
                if node is self.last:
                    raise IndexError
                old_node = node.next
                node.next = node.next.next
                if self.last is old_node:
                    self.last = node
                return old_node.value
        else:
            raise IndexError(index)

    def _iter_nodes(self):
        node = self.last
        if not node:
            return
        while True:
            node = node.next
            yield node
            if node is self.last:
                return

    def __iter__(self):
        for node in self._iter_nodes():
            yield node.value

    def __repr__(self):
        return '[{}]'.format(', '.join(repr(n) for n in self))



circular_list = CircularLinkedList()

mans, step, groups = -1, -1, -1

def circular_push_back(n):
    circular_list.append(n)

def circular_erase(index):
    return circular_list.pop(index)

def circular_show():
    print("{0}".format(repr(circular_list)))

def in_proc():
    global mans, step, groups
    mans , step, groups = -1, -1, -1
    value = input("Enter of mans and step, group: ")
    try:
        value = [int(i) for i in value.split(sep=' ')]
        if value[0] >= value[2] > 0 and value[1] > 0:
            mans, step, groups = value[0], value[1], value[2]
            for i in range(mans):
                circular_push_back(i)
        else:
            value[0] = -1
    except (ValueError, IndexError):
        if len(value) == 1 and value[0] == 0:
            value[0] = 0
        else:
            print("Error")
            value = [-1]
    return value[0]

def out_proc(extract_list):
    circular_show()
    print(extract_list)

def extraction():
    global mans, step
    length = mans
    count = 1
    ret = []
    ret.append(circular_erase(0))
    length -= 1
    while count < mans:
        ret.append(circular_erase(((step-1)*count)%length))
        count += 1
        length -= 1
    return ret

def main():
    loop = True
    while loop:
        ret = in_proc()
        if ret == 0:
            loop = False
            print("====END====")
            continue
        if ret < 0:
            print("Invalid value")
            continue
        out_proc(extraction())

if __name__ == "__main__":
    main()