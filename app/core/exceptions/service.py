class ServiceNotFoundError(Exception):
    def __init__(self, name: str):
        self.service_name = name
        self.message = f"Service {name} Not Found."
        super().__init__(self.message)


class ServiceAlreadyExistsError(Exception):
    def __init__(self, name: str):
        self.service_name = name
        self.message = f"Service {name} already exists."
        super().__init__(self.message)


class ServiceListEmptyError(Exception):
    def __init__(self):
        self.message = "Service List is Empty."
        super().__init__(self.message)