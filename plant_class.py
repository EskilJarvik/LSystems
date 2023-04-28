class plants:
    def __init__ (self, name, age, string):
        self.name = name
        self.age = age
        self.string = string

    def grow(self, ruleset):
        cur_string = self.string
        new_string = ""

        for c in cur_string:
            if c in ruleset:
                new_string += ruleset[c]

        self.string = new_string
        return self