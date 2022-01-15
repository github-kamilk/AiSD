import operator


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

    # def __str__(self):
    #     out = ""
    #     for cur in self.items:
    #         out += str(cur) + "|"
    #     return out


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

    def insert_left_tree(self, tree):
        self.left_child = tree

    def insert_right_tree(self, tree):
        self.right_child = tree

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, obj):
        self.key = obj

    def get_root_value(self):
        return self.key

    def __str__(self):
        return self.key


# def preorder(tree):
#     if tree:
#         #print(tree.get_root_value())
#         preorder_tree.append(tree.get_root_value())
#         preorder(tree.get_left_child())
#         preorder(tree.get_right_child())
#         return tree.get_root_value()

#
# def postorder(tree):
#     if tree:
#         postorder(tree.get_left_child())
#         postorder(tree.get_right_child())
#         print(tree.get_root_value())


def postorder_eval(tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    if tree:
        res1 = postorder_eval(tree.get_left_child())
        res2 = postorder_eval(tree.get_right_child())
        if res1 and res2:
            return opers[tree.get_root_value()](res1, res2)
        else:
            return tree.get_root_value()


def print_function(tree):
    result = []
    if tree == None:
        return result
    result.append('(')
    if tree.key in ['sin', 'cos', 'ln', 'exp']:
        result.append(tree.key)
        result.extend(print_function(tree.left_child))
    else:
        if tree.left_child != None:
            result.extend(print_function(tree.left_child))
        result.append(tree.key)
        if tree.right_child != None:
            result.extend(print_function(tree.right_child))
    result.append(')')
    return result


def parse_function(function):
    function = function.replace(" ", "")
    parsed_function = []
    while function != '':
        if function[:3] in ['sin', 'cos', 'exp']:
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
        elif i not in ['+', '-', '*', '/', '^', 'sin', 'cos', 'ln', 'exp', ')']:
            current_tree.set_root_value(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i in ['+', '-', '*', '/', '^']:
            if current_tree.get_root_value() == '':
                current_tree.set_root_value(i)
                current_tree.insert_right('')
                p_stack.push(current_tree)
                current_tree = current_tree.get_right_child()
            else:
                helper_tree = Binary_tree(i)
                helper_tree.left_child = current_tree
                helper_tree.insert_right('')
                function_tree = helper_tree
                current_tree = function_tree
                p_stack.push(current_tree)
                current_tree = current_tree.get_right_child()
        elif i in ['sin', 'cos', 'exp', 'ln']:
            if current_tree.get_root_value() == '':
                current_tree.set_root_value(i)
                current_tree.insert_left('')
                p_stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            else:
                pass
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    return function_tree


def cut_parsed_list(parsed_list):
    not_end_symbols = ['+', '-', '*', '/', '^', 'sin', 'cos', 'ln', 'exp']

    for i in range(len(parsed_list)):
        if parsed_list[i] not in not_end_symbols and parsed_list[i + 1] not in not_end_symbols:
            parsed_list = parsed_list[:i + 2]
            break

    return parsed_list


def build_tree_from_parsed(parsed_list):
    p_stack = Stack()
    function_tree = Binary_tree('')
    p_stack.push(function_tree)
    current_tree = function_tree
    for i in parsed_list:
        if i in ['+', '-', '*', '/', '^', 'sin', 'cos', 'ln', 'exp']:
            if current_tree.get_root_value() == '':
                current_tree.set_root_value(i)
                current_tree.insert_left('')
                current_tree.insert_right('')
                p_stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            else:
                current_tree = current_tree.get_right_child()
                current_tree.set_root_value(i)
                current_tree.insert_left('')
                current_tree.insert_right('')
                p_stack.push(current_tree)
                current_tree = current_tree.get_left_child()
        elif i == '':
            pass
        else:
            if current_tree.get_root_value() == '':
                current_tree.set_root_value(i)
                current_tree = p_stack.pop()
            else:
                current_tree = current_tree.get_right_child()
                current_tree.set_root_value(i)
    return function_tree


def differential_tree(tree):
    preorder_tree = []

    def preorder(tree):
        if tree:
            preorder_tree.append(tree.get_root_value())
            preorder(tree.get_left_child())
            preorder(tree.get_right_child())
            return tree.get_root_value()

    preorder(tree)
    p_stack = Stack()
    diff_tree = Binary_tree('')
    p_stack.push(diff_tree)
    current_tree = diff_tree

    j = 0
    while j < len(preorder_tree):
        i = preorder_tree[j]
        if i == '':
            j += 1
        elif i in ['+', '-']:
            if current_tree.get_root_value() == '':
                current_tree.set_root_value(i)
                current_tree.insert_left('')
                current_tree.insert_right('')
                p_stack.push(current_tree)
                current_tree = current_tree.get_left_child()
                j += 1
            else:
                print("Wanted set + or - but taken")
                j += 1
        elif i in ['cos', 'sin']:
            current_tree.set_root_value("*")
            paste_tree = build_tree_from_parsed(cut_parsed_list(preorder_tree[j:]))

            current_tree.insert_left_tree(paste_tree)
            p_stack.push(current_tree)

            current_tree = current_tree.get_left_child()
            if i == 'sin':
                current_tree.set_root_value('cos')
            elif i == 'cos':
                current_tree.set_root_value('-sin')

            current_tree = p_stack.pop()
            diff = differential_tree(paste_tree.get_right_child())
            current_tree.insert_right_tree(diff)
            parent = p_stack.pop()
            if not p_stack.is_empty():
                while parent.get_right_child().get_root_value() != '' and not p_stack.is_empty():
                    parent = p_stack.pop()
            current_tree = parent.get_right_child()
            j += len(cut_parsed_list(preorder_tree[j:]))

        elif i == 'x':
            # print(type(current_tree.get_left_child()))
            current_tree.set_root_value("1")
            # if not p_stack.is_empty():
            #     parent = p_stack.pop()
            #     while parent.get_right_child().get_root_value() != '' and not p_stack.is_empty():
            #         parent = p_stack.pop()
            # current_tree = parent.get_right_child()
            j += 1
        elif i == '*':
            if current_tree.get_root_value() == '':
                current_tree.set_root_value('+')
                current_tree.insert_left('*')
                current_tree.insert_right('*')
                p_stack.push(current_tree)

                current_tree = current_tree.get_left_child()
                paste_tree = build_tree_from_parsed(cut_parsed_list(preorder_tree[j:]))
                left_diff = differential_tree(paste_tree.get_left_child())
                current_tree.insert_left_tree(left_diff)
                current_tree.insert_right_tree(paste_tree.get_right_child())

                current_tree = p_stack.pop()
                current_tree = current_tree.get_right_child()
                current_tree.insert_left_tree(paste_tree.get_left_child())
                right_diff = differential_tree(paste_tree.get_right_child())
                current_tree.insert_right_tree(right_diff)

                parent = p_stack.pop()
                if not p_stack.is_empty():
                    while parent.get_right_child().get_root_value() != '' and not p_stack.is_empty():
                        parent = p_stack.pop()
                current_tree = parent.get_right_child()
                print(current_tree.get_root_value())

                j += len(cut_parsed_list(preorder_tree[j:]))
            else:
                print("Wanted set * but taken")
                j += len(cut_parsed_list(preorder_tree[j:]))
        elif i.isnumeric():
            current_tree.set_root_value('0')
            j += 1
        else:
            j += 1
    return diff_tree


if __name__ == "__main__":
    #function = '(5*x)+1'
    function = '(sin(x))'
    #function = '(sin(x)+(2*x))'
    # function = '(9*(x^3))+(8*(x^2))+(7*(2*x))+(6*x)'
    # function = '5*(x^5)'
    # function = 'sin(x+2)-3'
    # function = 'sin((x^3)+2)'
    # function = '(9*(x^3))+(8*(x^2))+(7*(2*x))+(6*x)'
    p_f = parse_function(function)
    print(p_f)
    fun_tree = build_tree(p_f)
    # preorder(fun_tree)
    print(''.join(print_function(fun_tree)))
    diff_tree = differential_tree(fun_tree)
    print(''.join(print_function(diff_tree)))
    # print(print_function(build_tree_from_parsed(['sin', '', 'x'])))
    # print(print_function(build_tree(['sin','(','x','+','5',')'])))

    # print(postorder_eval(fun_tree))
