class ClientNotFoundError(Exception):
    def __init__(self, name: str):
        self.client_name = name
        self.message = f"Client {name} Not Found."
        super().__init__(self.message)
