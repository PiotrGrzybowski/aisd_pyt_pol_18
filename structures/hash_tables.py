class HashSet:
    def __init__(self, payload_factor: int = 0.75, increase_factor: int = 2, initial_buckets: int = 4) -> None:
        self.payload_factor = payload_factor
        self.increase_factor = increase_factor
        self.initial_buckets = initial_buckets
        self.size = 0

        self.buckets = self._build_initial_buckets()

    def add(self, value):
        hash_value = hash(value)
        bucket_index = hash_value % (len(self.buckets))
        self.buckets[bucket_index].append(value)
        self.size += 1

    def _build_initial_buckets(self):
        return [[] for _ in range(self.initial_buckets)]

    def buckets_str(self):
        return '\n'.join([f'{i:2}: {str(bucket)}' for i, bucket in enumerate(self.buckets)])

    def __str__(self) -> str:
        elements = ', '.join([str(element) for bucket in self.buckets for element in bucket])
        return f'{{{elements}}}'

if __name__ == '__main__':
    names = HashSet()
