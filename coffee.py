class Coffee:
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not (3 <= len(name)):
            raise ValueError("Name must be at least 3 characters")
        self._name = name

    def name(self):
        return self._name
    
    