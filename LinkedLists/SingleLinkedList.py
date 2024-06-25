class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        return '->'.join(nodes)

    def get_length(self):
        length_of_list = 0
        current = self.head
        while current:
            length_of_list += 1
            current = current.next

        return length_of_list

    def prepend(self, data):
        new_node = Node(data)
        # add this new_node as a head
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self, data):
        if not self.head:
            return "Empty LinkedList"

        # if the head is the delete node
        if self.head.data == data:
            self.head = self.head.next

        current = self.head
        previous = None

        while current:
            if current.data == data:
                if not previous:
                    self.head = self.head.next
                else:
                    previous.next = current.next

                if current == self.tail:
                    self.tail = previous

            previous = current
            current = current.next

    def insert_before(self, data, before_data):
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        # insert a new node before the node which have a data of before_data
        if self.head.data == before_data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            previous = None

            while current:
                if current.data == before_data:
                    if not previous:
                        new_node.next = self.head
                        self.head = new_node
                    else:
                        new_node.next = current
                        previous.next = new_node

                previous = current
                current = current.next

    def insert_after(self, data, after_data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        elif self.head.data == after_data:
            new_node.next = self.head.next
            self.head.next = new_node
        elif self.tail.data == after_data:
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            previous = None

            while current:
                if current.data == after_data:
                    if not previous:
                        new_node.next = self.head.next
                        self.head.next = new_node
                    else:
                        new_node.next = current.next
                        current.next = new_node

                previous = current
                current = current.next


    def reverse_list(self):
        # reverse the list
        current = self.head
        prev = None
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
            
            

        

    def get_nth_from_end(self, n):
        lead_node = self.head
        follow_node = self.head
        
        for _ in range(n):
            if not lead_node:
                return -1
            lead_node = lead_node.next
        
        while lead_node:
            lead_node = lead_node.next
            follow_node = follow_node.next
        return follow_node.data
            
        
        
    def delete_dublicates(self):
        # delere dublicates from the list
        current = self.head
        
        while current:
            runner = current.next
            
            while runner:
                if (runner.data == current.data):
                    current.next = runner.next
                runner = runner.next
            current = current.next
            


    def search(self, n):
        # search for n
        if not self.head:
            return "Empty List"
        current = self.head
        while current:
            if n == current.data:
                return current
            current = current.next
        return -1


linkedList = LinkedList()

linkedList.prepend(10)
linkedList.prepend(12)
linkedList.prepend(14)
linkedList.append(20)
linkedList.delete(12)
linkedList.delete(10)
linkedList.append(100)
linkedList.insert_after(200, 100)
linkedList.insert_after(200, 100)
linkedList.insert_after(300, 14)
linkedList.insert_before(400, 300)
linkedList.delete_dublicates()
print(linkedList.search(300))

# print in structural way
print(linkedList.__str__())


print(linkedList.get_nth_from_end(3))
