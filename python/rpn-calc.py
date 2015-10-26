__author__ = 'William Stevens'
"""
    Written by: William A Stevens V, 10/22/2015
    Free to distribute and modify as long as this header remains.
    This code is provided as is, without warranty of any kind.
"""


class StackError(Exception):
    pass


class Node:
    """
        Representation of a single element of a stack.
        Contains information and a pointer to the next node.
    """
    def __init__(self,data=None, next=None):
        self.data = data
        if next is None or isinstance(next,Node):
            self.next = next
        else:
            raise ValueError("next should be of type Node or None")

    def __str__(self):
        return self.data


class Stack:
    """
        Provides the functionality of a stack using a linked list.
        Push a node on to the stack, pop a node off, peek at the next element.
    """
    _top = None

    def push(self,data):
        element = Node(data,self._top)
        self._top = element

    def pop(self):
        """
            Removes the top node off of the stack.
            Throws a StackError if there are no more elements on the stack.
            :return: data of node that was removed from stack :
        """
        result = self._top
        if self._top is not None:
            self._top = self._top.next
        else:
            raise StackError("Can't pop an empty stack.")
        return result.data

    def peek(self):
        """
            Returns the top node of the stack without removing it.
            :return: data of top node in stack or none if empty stack. :
        """
        return self._top.data

    def size(self):
        """
            Returns the size of the stack with 0 size being an empty stack.
        """
        size = 0
        el = self._top
        while el is not None:
            el = el.next
            size += 1
        return size

    def __str__(self):
        """
            Returns each node in the stack as a space seperated list.
        """
        el = self._top
        result = ""
        while(el is not None):
            result = str(el.data)+" " + result
            el = el.next
        return result

def main():
    """
        Reads lines from stdin as space seperated expressions in RPN Notaion.
        Stores results in stack, then prints the stack.
    """
    print("RPN Calculator")
    st = Stack()
    # Readline Loop
    while True:
        # Parse Line
        cmd_str = input("$ ").strip()
        cmd_str = cmd_str.split()
        # Evaluation Loop
        for token in cmd_str:
            try:
                if token is '+':
                    result = st.pop() + st.pop()
                    st.push(result)
                elif token is '-':
                    result = (-st.pop()) + st.pop()
                    st.push(result)
                elif token is '*':
                    result = st.pop() * st.pop()
                    st.push(result)
                elif token is '/':
                    result = (1 / st.pop()) * st.pop()
                    st.push(result)
                else:
                    st.push(float(token))
            except ValueError: # Catch a token that isn't defined.
                print("Invalid token",token)
            except StackError as e: # Catch a situation when popping on an empty stack.
                # NOTE: Tokens popped off of the stack during evaluation are lost!
                print('ERROR: Not enough items in stack.')
        print(st.size(), "in stack")
        print(st)
        
if __name__ == "__main__":
    main()