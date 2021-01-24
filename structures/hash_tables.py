class HashSet:
    def __init__(self, payload_factor: int = 0.75, increase_factor: int = 2, initial_buckets: int = 4) -> None:
        self.payload_factor = payload_factor
        self.increase_factor = increase_factor
        self.initial_buckets = initial_buckets
        self.size = 0

        self.buckets = self._build_buckets(self.initial_buckets)

    def add(self, value):
        if not self.contains(value):
            if self.size / len(self.buckets) >= self.payload_factor:
                self._increase_buckets_count(self.increase_factor * len(self.buckets))
            bucket_index = hash(value) % len(self.buckets)
            self.buckets[bucket_index].append(value)
            self.size += 1

    def contains(self, value):
        bucket_index = hash(value) % len(self.buckets)
        return value in self.buckets[bucket_index]

    def _build_buckets(self, buckets_count):
        return [[] for _ in range(buckets_count)]

    def _increase_buckets_count(self, target_buckets_count):
        new_buckets = self._build_buckets(target_buckets_count)
        for bucket in self.buckets:
            for value in bucket:
                bucket_index = hash(value) % len(new_buckets)
                new_buckets[bucket_index].append(value)
        self.buckets = new_buckets

    def buckets_str(self):
        return '\n'.join([f'{i:2}: {str(bucket)}' for i, bucket in enumerate(self.buckets)])

    def __str__(self) -> str:
        elements = ', '.join([str(element) for bucket in self.buckets for element in bucket])
        return f'{{{elements}}}'


if __name__ == '__main__':
    names = HashSet()
    names.add("Piotr")
    names.add("Ola")
    names.add("123")
    names.add("Adam")
    names.add("Ewa")
    names.add("Python")
    names.add("PC")
    names.add("PApple")
    names.add("PPiotr")
    names.add("POla")
    names.add("P123")
    names.add("PAdam")
    names.add("PEwa")
    names.add("Python")
    names.add("sPC")
    names.add("apple")

    print(names.buckets_str())
    print(names.contains("Piotr"))