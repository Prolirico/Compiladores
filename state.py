class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.funcs = {}# se agrego
        self.parent = parent

    def get_var(self, name):
        while self:
            value = self.vars.get(name)
            if value is not None:
                return value
            else:
                self = self.parent
        return None

    def set_var(self, name, value):
        original_env = self
        while self:
            if name in self.vars:
                self.vars[name] = value
                return value
            self = self.parent
        original_env.vars[name] = value

    def get_func(self, name):#se agrego name y todo lo de la funcion
        while self:
            value = self.funcs.get(name)
            if value is not None:
                return value
            else:
                self = self.parent
        return None

    def set_func(self, name, value):#se agrega esta funcion
        self.funcs[name] = value

    def new_env(self):
        return Environment(parent=self)
