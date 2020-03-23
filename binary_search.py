#Binary Search Algorithm. Return index if found, else return -1

class BinarySearch:

    def __init__(self, data_list):                                              #initialize the object by passing the list of elements
        self.data_list = data_list

    def binary_search(self, key):
        first = 0
        last = len(self.data_list) - 1
        
        while(first <= last):
            middle = (first + last) // 2                                        #Use floor division as index is a whole number
            print(first, last, middle, self.data_list[middle], key)
            if(self.data_list[middle] == key):
                return middle

            else:
                if (key < self.data_list[middle]):
                    last = middle-1
                else:
                    first = middle + 1

        return -1

# BinS = BinarySearch([11, 19, 27, 33, 42, 57, 63, 76, 81, 93, 99])
# print(BinS.binary_search(int(input('Enter the input: '))))