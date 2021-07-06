class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.is_on = False
        self.apps = []

    def power(self):
        self.is_on = True

    def install(self, app, memory_needed):
        if self.memory >= memory_needed:
            if self.is_on:
                self.memory -= memory_needed
                self.apps.append(app)
                return f"Installing {app}"
            return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"
