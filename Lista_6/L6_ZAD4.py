class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Binary_tree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = Binary_tree(new_node)
        else:
            t = Binary_tree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = Binary_tree(new_node)
        else:
            t = Binary_tree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key


def preorder(tree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def parse_function(function):
    function = function.replace(" ", "")
    parsed_function = []
    while function != '':
        if function[:3] in ['sin', 'cos', 'exp', 'log']:
            parsed_function.append(function[:3])
            function = function[3:]
        elif function[:2] == 'ln':
            parsed_function.append('ln')
            function = function[2:]
        elif function[0].isnumeric():
            i = 1
            f_len = len(function)
            if f_len != 1:
                while function[i].isnumeric() and i < f_len:
                    i += 1
                parsed_function.append(function[:i])
                function = function[i:]
            else:
                parsed_function.append(function[0])
                function = function[1:]
        else:
            parsed_function.append(function[0])
            function = function[1:]
    return parsed_function


def build_tree(parsed_function):
    p_stack = Stack()
    function_tree = Binary_tree('')
    p_stack.push(function_tree)
    current_tree = function_tree
    for i in parsed_function:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+', '-', '*', '/', ')']:
            current_tree.set_root_value(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_value(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return function_tree


function = '( ( 10 + 5 ) * 3 )'
p_f = parse_function(function)
print(p_f)
fun_tree = build_tree(p_f)
preorder(fun_tree)
