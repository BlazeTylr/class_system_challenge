class Todo:

    def __init__(self, task=False):
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True
