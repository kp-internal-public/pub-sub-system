class Message:
    def __init__(self, id, data) -> None:
        self.id = id
        self.data = data

    def __repr__(self) -> str:
        return f"id: {self.id}, data: {self.data}"
