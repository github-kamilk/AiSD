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


def find_openers_closers(text):
    openers_closers = []

    index = 0

    while index < len(text):
        if text[index] == "<":
            if text[index + 1] == "/":  # for '</...>' - end of non-singleton
                i = 1
                while text[index + 1 + i] != ">":
                    i += 1
                openers_closers.append(text[index:index + i + 2])
                index += 2 + i
            elif text[index + 1:index + 4] == "!--":  # for '<!--' - begin of comment
                openers_closers.append("<!--")
                index += 4
            else:  # for '<....' - begin singleton or non-singleton
                i = 1
                while text[index + i] != " " and text[index + i] != ">":
                    i += 1
                openers_closers.append(text[index:index + i])
                index += i

        # find closers
        elif text[index:index + 2] == "/>":  # for sigletons
            openers_closers.append("/>")
            index += 2
        elif text[index] == ">":  # for singletons or non-singletons
            openers_closers.append(">")
            index += 1
        elif text[index:index + 3] == "-->":
            openers_closers.append("-->")
            index += 3
        else:
            index += 1
    return add_endings(openers_closers)


def add_endings(tags_list):
    """Add '>' or '/>' ending to tags"""
    openers_closers = []
    tags_list.append('')

    for i in range(len(tags_list) - 1):  # Add '>' or '/>' ending to tags
        if tags_list[i + 1] == ">" and i + 1 < len(tags_list):
            openers_closers.append(tags_list[i] + ">")
        elif tags_list[i + 1] == "/>" and i + 1 < len(tags_list):
            openers_closers.append(tags_list[i] + "/>")
        elif tags_list[i] != '>' and tags_list[i] != '/>':
            openers_closers.append(tags_list[i])
        else:
            pass
    #print(openers_closers)
    return openers_closers

def checking_HTML_correctness(filename):
    file_obj = open(filename, 'r')
    text = file_obj.read()
    singletons = ["area", "base", "br", "col", "command", "embed", "hr", "img", "input", "keygen", "link", "meta",
                  "param", "source", "track", "wbr", "!DOCTYPE"]

    openers_closers = find_openers_closers(text)
    #print(openers_closers)

    s = Stack()
    balanced = True
    index = 0

    while index < len(openers_closers) and balanced:
        symbol = openers_closers[index]
        if symbol[1:-1] in singletons or symbol[1:-2] in singletons:
            pass
        elif symbol[:2] != '</' and symbol != "-->":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            elif s.peek() == '<!--' and symbol == '-->':
                s.pop()
            else:
                top = s.pop()
                if not top[1:] == symbol[2:]:
                    balanced = False
        #print(s.items)
        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False
