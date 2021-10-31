#%%
# Intersection of two linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data
    
    
class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
        

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_at_beginning(self, node: str):
        prev_head = self.head
        self.head = Node(data=node)
        self.head.next = prev_head

    def add_at_end(self, node: str):
        if self.head is None:
            self.head = Node(data=node)
            return
        else: 
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
                    
            current_node.next = Node(data=node)

    def add_after(self, node: str, new_node: str):
        if self.head is None:
            raise Exception("List is empty")
        
        new_node = Node(data=new_node)
        
        for current_node in self:
            if current_node.data == node:
                new_node.next = current_node.next
                current_node.next = new_node
                return
        raise Exception("Node not found")
    
    def add_before(self, node: str, new_node: str):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == node:
            self.add_at_beginning(new_node)
            return

        new_node = Node(data=new_node)
        prev_node = self.head
        for current_node in self:
            if current_node.data == node:
                prev_node.next = new_node
                new_node.next = current_node
                return
            prev_node = current_node

        raise Exception("Node not found")
    
    def remove_node(self, node: str):
        if self.head is None:
            raise Exception("List is empty")

        #remove if node easily if start of the list
        if self.head.data == node:
            self.head = self.head.next # remove head
            return
        
        prev_node = self.head
        for current_node in self:
            if current_node.data == node:
                prev_node.next = current_node.next
                return
            prev_node = current_node
        
        raise Exception("Node not found")
    
# %%
def intersection_of_linked_lists(first, second):
    nodes = set()
    
    while first:
        nodes.add(first.data)
        first = first.next
    
    while second:
        if second.data in nodes:
            return second.data
        else:
            second = second.next
    
# %%
llist1 = LinkedList(['3', '4', '5', '6', '7', '8', '9'])
llist2 = LinkedList(['22', '34','6', '7', '8', '9'])
print(intersection_of_linked_lists(llist1.head, llist2.head))
# %%
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    print(f'second = {second}')
    first = max(array[0], array[1])
    print(f'first = {first}')
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        print(f'current max = {current}')
        second = first
        print(second)
        first = current
        print(first)
    return first

maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135])
# %%
