class Node:
    def __init__(self,element):
        self.element=element
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self,push_element):
        '''this function pushes the elements in to the stack'''
        if self.top is None:
            self.top=Node(push_element)
        else:
            new_node=Node(push_element)
            new_node.next=self.top
            self.top=new_node

    def pop(self):
        '''this function gets the top element from the stack'''
        pop_element=None
        if self.top is not None:
             pop_element=self.top.element
             self.top=self.top.next
             return f"popping out {pop_element}"
        else:
            raise Exception("Stack is empty..")
            return 
    
    def print_elements(self):
        '''this function print the elements in the stack'''
        itr=self.top
        while itr:
            print(itr.element)
            itr=itr.next

    def count_elements(self):
        '''this function return the number of elements present in the stack'''
        count=0
        itr=self.top
        while itr:
            count+=1
            itr=itr.next
        return f"the number of elements in the stack are {count}"

    def search_element(self,search_key):
        '''this function checks whether the search key present in the stack or not'''
        itr=self.top
        while itr:
            if itr.element==search_key:
                return f"{search_key} search key found in the stack"
            itr=itr.next
        if itr is None:
            return f"{search_key} search key not found in the stack"

if __name__ == "__main__":
    stack=Stack()
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print(stack.count_elements())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print("elements in the stack are :")
    stack.print_elements()
    print(stack.count_elements())
    print(stack.search_element(4))
    print(stack.search_element(5))
    print(stack.search_element(58))