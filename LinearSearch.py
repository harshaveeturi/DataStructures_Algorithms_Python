class LinearSearch(object):
    '''this class implements the linear search algorithm in a given list'''
    def __init__(self):
        #simple constructor
        pass
    
    def search(self,search_key,list_of_elements):
        '''
        this function check whether the search element is present in the list or not
        implemneted the algorithm based on zero indexing in python3
        '''
        for i in range(len(list_of_elements)):
            if list_of_elements[i]==search_key:
                return f"{search_key} is the search key found at index {i} and is present in the list"
        if i==len(list_of_elements)-1:
            return f"{search_key} is the search key not found in the list"

if __name__=="__main__":
    linear_search=LinearSearch()
    list_of_elements=[5,3,4,2,1,6,8,9]
    search_key=7
    print(linear_search.search(search_key,list_of_elements))
    search_key=9
    print(linear_search.search(search_key,list_of_elements))