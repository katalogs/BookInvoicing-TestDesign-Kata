class IdGenerator:
    _current_id = 0

    @classmethod
    def next_id(cls) -> int:
        cls._current_id += 1
        return cls._current_id
