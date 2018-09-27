class Node(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None

head = Node()
head.next = Node(20)
head.next.next = Node(30)

def traversal(head):
    curNode = head  # 临时用指针
    while curNode is not None:
        print(curNode.item)
        curNode = curNode.next

traversal(head)

