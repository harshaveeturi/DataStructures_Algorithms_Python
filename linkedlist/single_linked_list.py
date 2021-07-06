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
        if self.head is None:
            return "Single Linked list is empty to print any elements!!"
        singlelinkedlist_string=''
        itr=self.head
        while itr:
            singlelinkedlist_string+=str(itr.element)+'->'
            itr=itr.next
        return singlelinkedlist_string

    def count_elements(self):
        '''this functions counts and returns the number of elements presnet in the single linked list'''
        if self.head is not None:
            count=1
            itr=self.head
            while itr.next:
                count+=1
            itr=itr.next
            return count
        else:
            return 0
    
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
            
    def insert_after_value(self, data_after, data_to_insert):
        '''this function inserts an element after an provided element'''
        if self.head is None:
            raise Exception("there is only one element in the single linked list")
        else:
            itr=self.head
            while itr.next:
                if itr.element==data_after:
                    new_node=Node(data_to_insert)
                    new_node.next=itr.next
                    itr.next=new_node
                itr=itr.next


    def insert_values(self,list_of_elements):
        '''this function clears all the elements present in the list and creates a new list of elements in the single linked list'''
        self.head=None
        for element in list_of_elements:
            self.insert_at_ending(element)


    def remove_by_value(self,search_element):
        '''this function looks for a particular element and removes the element from the single linked list '''
        if self.head is None:
            return "Linked list is empty to remove an element"

        elif self.head.element==search_element:
            self.head=self.head.next
        else:
            itr=self.head
            while itr.next:
                if itr.next.element==search_element and itr is not None:
                    itr.next=itr.next.next
                    break
                itr=itr.next
        


if __name__=='__main__':
    singlelinkedlist=SingleLinkedList()
    singlelinkedlist.insert_values(["banana","mango","grapes","orange"])
    singlelinkedlist.insert_after_value("banana","apple")
    print(singlelinkedlist.print_elements())
    singlelinkedlist.remove_by_value("apple")
    print(singlelinkedlist.print_elements())
    singlelinkedlist.remove_by_value("orange")
    print(singlelinkedlist.print_elements())
    singlelinkedlist.remove_by_value("figs")
    print(singlelinkedlist.print_elements())
    singlelinkedlist.remove_by_value("banana")
    print(singlelinkedlist.print_elements())
    singlelinkedlist.remove_by_value("mango")
    print(singlelinkedlist.print_elements())
    singlelinkedlist.remove_by_value("grapes")
    print(singlelinkedlist.print_elements())