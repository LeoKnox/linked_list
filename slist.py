class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
    def add_to_back(self, val):
        new_node = Node(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self
    def remove_from_front(self):
        if self.head != None:
            self.head = self.head.next
        return self
    def remove_from_back(self):
        runner = self.head
        if (runner.next == None):
            self.head = None
        else:
            while (runner.next.next != None):
                runner = runner.next
            runner.next = None      
    def remove_val(self, val):
        runner = self.head
        while (runner.next.value != val):
            runner = runner.next
        runner.next = runner.next.next
    def insert_at(self, pos, val):
        loc = 1
        new_node = Node(val)
        if (pos == 0):
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
            return self
        runner = self.head
        while (loc != pos):
            loc +=1
            runner = runner.next
        new_node.next = runner.next
        runner.next = new_node
        
        
mylist = SList()
mylist.add_to_front('scotch')
mylist.add_to_front('bourbon')
mylist.add_to_back('tequila')
mylist.add_to_back('wine')
mylist.print_values()
print('----------------------')
#mylist.remove_from_front()
mylist.insert_at(2, 'vodka')
mylist.insert_at(0, 'rum')
mylist.remove_val('wine')
mylist.print_values()
