class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.max_stack:
            self.max_stack.append(x)
        else:
            self.max_stack.append(max(x, self.max_stack[-1]))

    def pop(self) -> str | None:
        if not self.stack:
            return "error"
        self.stack.pop()
        self.max_stack.pop()
        return None

    def get_max(self) -> int | str | None:
        if not self.stack:
            return "None"
        return self.max_stack[-1] #через max_stack чтобы не реализовывать функциона питона через... функционал питона
