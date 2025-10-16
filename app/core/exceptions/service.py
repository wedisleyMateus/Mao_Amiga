class ServiceBaseError(Exception):
    def __init__(self, service_name: str, message_suffix: str):
        self.service_name = service_name
        self.message_suffix = message_suffix
        super().__init__(self.message_suffix)

class ServiceNotFoundError(ServiceBaseError):
    def __init__(self, service_name: str):
        super().__init__(service_name, f'Service {service_name} not found')


class ServiceAlreadyExistsError(ServiceBaseError):
    def __init__(self, service_name: str):
        super().__init__(service_name, f'Service {service_name} already exists')


class ServiceListEmptyError(Exception):
    def __init__(self):
        self.message = "Service List is Empty."
        super().__init__(self.message)