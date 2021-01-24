class HashSet:
    def __init__(self, payload_factor: int = 0.75, increase_factor: int = 2, initial_buckets: int = 4) -> None:
        self.payload_factor = payload_factor
        self.increase_factor = increase_factor
        self.initial_buckets = initial_buckets
        self.size = 0

        self.buckets = self._build_initial_buckets()

    def _build_initial_buckets(self):
        return [[] for _ in range(self.initial_buckets)]


if __name__ == '__main__':
    names = HashSet()