# ------------- Walid Semrani Assignment --------- #

class Node:
    def __init__(self, d):
        self.data = d       # Node data
        self.next = None    # Next of the Node


class LinkedList:
    def __init__(self):
        self.head = None    # Head of the list

    # IdenticalList() Returns 1 if linked lists a and b
    # are identical, else return 0
    def IdenticalList(self, list_1, list_2):
        a = list_1.head
        b = list_2.head
        while a != None and b != None:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        return a == None and b == None

    # the __str__ func will return the value of linked list elements
    def __str__(self):
        res = ""

        # initializing ptr to head
        ptr = self.head
        # traversing and adding it to res
        while ptr:
            res += str(ptr.data) + ", "
            ptr = ptr.next
        # removing trailing commas
        res = res.strip(", ")
        # chen checking if
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"

    # this function allows us to push elements in the list pointing to the
    # head and an int elements are pushed in the front of the list
    def push(self, data_in):

        data_in = Node(data_in)

        data_in.next = self.head

        self.head = data_in


# the main program starts here!!
if __name__ == "__main__":

    f = open("assignment01-1.txt", "r")
    i = 1
    j = 0
    cases = [int(x) for x in f]
    total_test = cases[0]
    # print the content of the file elements
    # print(cases)
    del cases [0] # delete the first element that refer two number of tests to work only with list elements and lengths
    # print(cases)  # print file elements after deleting number of tests
    while j < total_test:
        start_i = 1
        start_j = start_i + cases[0] + 1
        list1 = []
        list2 = []
        # add file elements into two different list in order to push them in linked lists
        for x in cases[start_i : start_j-1]:
            list1.append(x)

        for y in cases[start_j : start_j+cases[start_j]]:
            list2.append(y)
            if j == total_test-1:
                list2.append(cases[-1])
                # add the last elements of the last test list

        # create the two linked lists
        linked_list1 = LinkedList()
        linked_list2 = LinkedList()

        # push list elements into the two linked lists
        for a in list1:
            linked_list1.push(a)
        for b in list2:
            linked_list2.push(b)
        # print(cases)
        is_linked_list = LinkedList().IdenticalList(linked_list1, linked_list2)
        # print the content of the two linked lists
        # print(linked_list1,linked_list2)
        print(1 if is_linked_list else 0)
        del cases[0:start_j+cases[start_j]]
        j = j+1

























