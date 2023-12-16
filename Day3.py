class MyHashSet:

    def __init__(self):

        self.size = 1000

        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):

        return key % self.size

    def add(self, key):

        if not self.contains(key):

            hash_key = self._hash(key)

            self.buckets[hash_key].append(key)

    

    def remove(self, key):

        hash_key = self._hash(key)

        bucket = self.buckets[hash_key]

        for i in range(len(bucket)):

            if bucket[i] == key:

                bucket.pop(i)

                return

    

    def contains(self, key):

        hash_key = self._hash(key)

        bucket = self.buckets[hash_key]

        for i in range(len(bucket)):

            if bucket[i] == key:

                return True

        return False

    
