class BinarySearch:
    def __init__(self):
        pass

    def search(self,search_element,list_of_elements):
        ''' this function implements the binary search and return if the element is found in the list of elements or not'''
        low=0
        high=len(list_of_elements)-1
        while low<=high:
            mid=(low+high)//2 #integer divison
            if list_of_elements[mid]==search_element:
                return f"{search_element} is found at index {mid} in the list of elements"
            elif list_of_elements[mid]<search_element:
                low=mid+1
            elif list_of_elements[mid]>search_element:
                high=mid-1
        if low>high or high==-1:
            return f"{search_element} {low} and {high} is not present in the list of elements"

if __name__ == "__main__":
    binarysearch=BinarySearch()
    # in order to implement binary search we need to have the data to be sorted otherwise the whole logic wont work
    print(binarysearch.search(13,[2,3,6,9,11,13,15]))
    print(binarysearch.search(17,[2,3,6,9,11,13,15]))
    print(binarysearch.search(2,[2,3,6,9,11,13,15]))
    print(binarysearch.search(15,[2,3,6,9,11,13,15]))
    print(binarysearch.search(9,[2,3,6,9,11,13,15]))
    print(binarysearch.search(91,[2,3,6,9,11,13,15]))
    print(binarysearch.search(-9,[2,3,6,9,11,13,15]))