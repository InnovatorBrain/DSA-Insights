class Node:
    def __init__(self, Data=None, Next=None):
        self.Data = Data
        self.Next = Next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, Data):
        node = Node(Data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print(f"The Linked List is empty")
            return
        itr = self.head
        itr_str = ""
        while itr:
            itr_str += str(itr.Data) + "--"
            itr = itr.Next
        print(itr_str)

    def insert_at_end(self, Data):
        if self.head is None:
            self.head = Node(Data, None)
            return

        itr = self.head

        while itr.Next:
            itr = itr.Next
        
        itr.Next = Node(Data, None)
    def insert_values(self, data_list):
        self.head = None
        
        for data in data_list:
            self.insert_at_end(data)




if __name__ == "__main__":
    SinglyLinkedList = LinkedList()
    SinglyLinkedList.insert_at_begining(25)
    SinglyLinkedList.insert_at_end(50)
    SinglyLinkedList.insert_at_begining(85)
    SinglyLinkedList.insert_values([2,5,8,10,15,20,25,30,35])
    SinglyLinkedList.print()
