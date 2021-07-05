class Node:
    def __init__(self,element=None):
        self.element=element
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,element):
        '''this function inserts the element at the beginning of the single linked list'''
        if self.head is None:
            self.head=Node(element)
        else:
            new_node=Node(element)
            new_node.next=self.head
            self.head=new_node

    def insert_at_ending(self,element):
        '''this function inserts the element at the end of the single linked list'''
        if self.head is None:
            self.head=Node(element)
        else:
            itr=self.head
            while itr.next:
                itr=itr.next
            new_node=Node(element)
            itr.next=new_node

    def print_elements(self):
        '''this functions prints all the elements present in the single linked list'''
        singlelinkedlist_string=''
        itr=self.head
        while itr:
            singlelinkedlist_string+=str(itr.element)+'->'
            itr=itr.next
        return singlelinkedlist_string

    def count_elements(self):
        '''this functions counts and returns the number of elements presnet in the single linked list'''
        count=1
        itr=self.head
        while itr.next:
            count+=1
            itr=itr.next
        return count
    
    def search_element(self,search_element):
        '''this function checks whether the element is present in the single linked list'''
        itr=self.head
        while itr:
            if itr.element==search_element:
                return f"{search_element} is present in the single linked list"
            itr=itr.next
        if itr is None:
            return f"{search_element} is not present in the single linked list"
    
    
    def delete_at_index(self,index):
        '''this function deletes a node at the ending of the single linked list'''
        if self.head is None:
            return f"single linked list is empty"
        elif  index<=0 or index> self.count_elements():
            raise Exception("pass the index with in the range 1 to length of list")
        else:
            count=1
            itr=self.head
            while itr.next:
                if count==index:
                    itr.next=itr.next.next
                count+=1   
                itr=itr.next
            

                
if __name__=='__main__':
    singlelinkedlist=SingleLinkedList()
    singlelinkedlist.insert_at_beginning(4)
    singlelinkedlist.insert_at_beginning(3)
    singlelinkedlist.insert_at_beginning(2)
    singlelinkedlist.insert_at_beginning(1)
    singlelinkedlist.insert_at_beginning(0)
    singlelinkedlist.insert_at_ending(5)
    singlelinkedlist.insert_at_ending(6)
    singlelinkedlist.insert_at_ending(7)
    singlelinkedlist.insert_at_ending(8)
    singlelinkedlist.insert_at_ending(9)
    print(singlelinkedlist.print_elements())
    print(f"the number of elements present in the linked list are {singlelinkedlist.count_elements()}")
    print(singlelinkedlist.search_element(58))
    print(singlelinkedlist.search_element(4))
    print(singlelinkedlist.search_element(-1))
    print(singlelinkedlist.search_element(-13))
    singlelinkedlist.delete_at_index(5)
    print(singlelinkedlist.print_elements())
    singlelinkedlist.delete_at_index(4)
    print(singlelinkedlist.print_elements())
    singlelinkedlist.delete_at_index(3)
    print(singlelinkedlist.print_elements())