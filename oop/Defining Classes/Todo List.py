class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if new_name == self.name:
            return "Name cannot be the same."
        self.name = new_name
        return new_name

    def change_due_date(self, new_due_date):
        if new_due_date == self.due_date:
            return "Date cannot be the same."
        self.due_date = new_due_date
        return new_due_date

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if comment_number in range(len(self.comments)):
            self.comments[comment_number] = new_comment
            return ', '.join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            return f"Task {task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        if task_name in self.tasks:
            task_name.completed = True
            return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        result = 0
        for i in self.tasks:
            if i.completed:
                result += 1
                self.tasks.remove(i)
        return f"Cleared {result}"

    def view_section(self):
        result = f"Section {self.name}:\n"
        for i in self.tasks:
            result += f'{i.details()}\n'
        return result
