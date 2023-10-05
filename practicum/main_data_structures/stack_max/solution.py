class StackMax:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) != 0:
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        if len(self.items) != 0:
            max_number = max(self.items)
            print(max_number)
        else:
            print('None')


if __name__ == '__main__':
    my_stack = StackMax()
    n_of_commands = int(input())
    for i in range(n_of_commands):
        command = input().split(' ')
        if command[0] == 'push':
            my_stack.push(int(command[1]))
        elif command[0] == 'pop':
            my_stack.pop()
        elif command[0] == 'get_max':
            my_stack.get_max()
