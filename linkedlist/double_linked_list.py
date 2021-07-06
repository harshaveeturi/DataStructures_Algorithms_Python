class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,element):
        '''this function inserts the element at the beginning of the double linked list '''
        if self.head is None:
            self.head=Node(element)
        else:
            new_node=Node(element)
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    
    def insert_at_ending(self,element):
        '''this function inserts the element at the ending of the double linked list '''
        if self.head is None:
            self.head=Node(element)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            new_node=Node(element)
            itr.next=new_node
            new_node.prev=itr

    def count_elements(self):
        '''this function counts the number of elements presnet in the double linked list'''
        if self.head is None:
            raise Exception("Double Linked List is empty and there are no elements present")
        else:
            count=0
            itr=self.head
            while itr:
                count+=1
                itr=itr.next
            return count
    
    def print_forward(self):
        '''this function print the elements in the forward direction using next pointer'''
        if self.head is None:
            print("No elements present in the double linked list")
        else:
            forward_doublelinkedlist_string=''
            itr=self.head
            while itr:
                forward_doublelinkedlist_string+=str(itr.data)+'->'
                itr=itr.next
            return forward_doublelinkedlist_string

    def print_backward(self):
        '''this function prints the elements in the reverse direction using prev pointer'''
        if self.head is None:
            print("No elements present in the double linked list")
        else:
            backward_doublelinkedlist_string=''
            itr=self.head
            while itr.next:
                itr=itr.next
            while itr:
                backward_doublelinkedlist_string+=str(itr.data)+'<-'
                itr=itr.prev
            return backward_doublelinkedlist_string

    def search_element(self,search_element):
        '''this function looks for the search element present in the double linked list'''
        if self.head is None:
            print("No elements are presnet in the double linked list")
        else:
            itr=self.head
            flag=0
            while itr.next:
                if itr.data==search_element:
                    flag=1
                    break
                itr=itr.next
            if flag==1:
                print(f"{search_element} present in the double linked list")
            else:
                print(f"{search_element} not present in the double linked list")

    def delete_at_index(self,index):
        '''this function deletes a node at the ending of the double linked list'''
        if self.head is None:
            print("No elements are present in the double linked list")
        elif index<=0 or index>self.count_elements():
            print(f"please provide index in the range of 1 to {self.count_elements()}")
            return            
        elif index==1:
            self.head=self.head.next
            self.head.prev=None
        else:
            itr=self.head
            count=1
            while itr:
                if count==index:
                   itr.prev.next=itr.next
                   itr.next.prev=itr.prev
                count+=1
                itr=itr.next

    def insert_at_index(self,index,data):
        '''this function inserts the data at the particular location in the double linked list'''
        if self.head is None:
            print("No elements are present in the double linked list")  

        elif index<=0 or index>self.count_elements():
            print(f"please provide index in the range of 1 to {self.count_elements()}")
            return       
        elif index==1:
            new_node=Node(data)
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
            count=1
            itr=self.head
            while itr:
                if count==index:
                    new_node=Node(data)
                    itr.prev.next=new_node
                    new_node.next=itr
                    new_node.prev=itr.prev
                    itr.prev=new_node
                count+=1
                itr=itr.next
                
    def insert_values(self,list_of_elements):
        '''this function clears all the elements present in the double linked list and creates a new one'''
        self.head=None
        for element in list_of_elements:
            self.insert_at_ending(element)

    def insert_after_value(self, data_after, data_to_insert):
        '''this function inserts an element after an provided element'''
        if self.head is None:
            raise Exception("there are no elements in the double linked list")
        else:
            itr=self.head
            while itr:
                if itr.data==data_after:
                    new_node=Node(data_to_insert)
                    new_node.prev=itr
                    new_node.next=itr.next
                    itr.next.prev=new_node
                    itr.next=new_node
                itr=itr.next

    def remove_by_value(self,element):
        '''this function searches and removes an element in the double linked list'''
        if self.head is None:
            raise Exception("there are no elements in the double linked list")
        else:
            itr=self.head
            while itr.next:
                if itr.data==element:
                        #print("testing case1",itr.data)             
                        itr.prev.next=itr.next
                        itr.next.prev=itr.prev
                itr=itr.next
                
if __name__=="__main__":
    doublelinkedlist=DoubleLinkedList()
    doublelinkedlist.insert_at_beginning('red')
    doublelinkedlist.insert_at_beginning('blue')
    doublelinkedlist.insert_at_beginning('green')
    doublelinkedlist.insert_at_ending('yellow')
    doublelinkedlist.insert_at_ending('orange')
    doublelinkedlist.insert_at_ending('white')
    print("="*50)
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)
    print(doublelinkedlist.count_elements())
    print("="*50)
    doublelinkedlist.delete_at_index(2)
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)
    doublelinkedlist.delete_at_index(4)
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)
    doublelinkedlist.delete_at_index(5)
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)
    doublelinkedlist.delete_at_index(-1)
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    doublelinkedlist.delete_at_index(1)
    print("="*50)
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)
    doublelinkedlist.insert_at_index(1,'black')
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)
    doublelinkedlist.insert_at_index(2,'orange')
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)
    doublelinkedlist.insert_after_value('orange','green')
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)
    doublelinkedlist.remove_by_value("green")
    print(doublelinkedlist.print_forward())
    print("="*50)
    print(doublelinkedlist.print_backward())
    print("="*50)