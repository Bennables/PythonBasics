class eater:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        print("Hi there")

    def eat(self):
        print("eating")

