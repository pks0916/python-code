
class Record:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.key} : {self.value}"

    def __hash__(self):
        return hash(self.key)


class HashMap:
    def __init__(self):
        self._num_buckets = 8
        self._buckets = [[] for i in range(self._num_buckets)]
        self._len = 0

    def __len__(self):
        return self._len

    def _bucket(self, k):
        bucket_index = hash(k) % self._num_buckets
        bucket = self._buckets[bucket_index]
        return bucket

    def __setitem__(self, k, v):
        # find which bucket in which to put the k:v pair
        bucket = self._bucket(k)
        # check if key is in the bucket
        for record in bucket:
            if record.key == k:   # found record with matching key
                record.value = v  # update record value
                return
        # if key not found, create new record and increment length
        bucket.append(Record(k, v))
        self._len += 1
        # check load factor to see if we need to rehash. Rehash if LF >= 2
        # load_factor = self._len / self._num_buckets
        # if load_factor >= 2:
        #     self._rehash(2 * self._num_buckets)

    def __getitem__(self, k):
        # find which bucket in which to put the k:v pair
        bucket = self._bucket(k)
        # check for record with matching key
        for record in bucket:
            if record.key == k:
                return record.value
        # if no record with key found, raise KeyError
        raise KeyError

    def __contains__(self, k):
        # find which bucket in which to put the k:v pair
        bucket = self._bucket(k)
        # check for record with matching key. If found, return True
        for record in bucket:
            if record.key == k:
                return True
        # if no record with key found, return False
        return False

    def remove(self, k):
        # find which bucket should contain the k:v pair
        bucket = self._bucket(k)
        # find record with matching key
        record_to_delete = None
        for record in bucket:
            if record.key == k:
                record_to_delete = record
        # if no record with key k was found, raise KeyError
        if record_to_delete is None:
            raise KeyError
        # otherwise remove record and decrement length
        bucket.remove(record_to_delete)
        self._len -= 1
        # check load factor to see if we need to rehash 
        # load_factor = self._len / self._num_buckets
        # if load_factor < 0.5 and self._num_buckets > 8:
        #     self._rehash(self._num_buckets // 2)

    def __delitem__(self, k):
        self.remove(k)

    def _rehash(self, size):
        # initialize new bucket list
        new_buckets = [[] for i in range(size)]
        # reinsert all records into new bucket list
        for bucket in self._buckets:
            for record in bucket:
                new_bucket_index = hash(record) % size
                new_buckets[new_bucket_index].append(record)
        # assign member variables
        self._buckets = new_buckets
        self._num_buckets = size

    def __repr__(self):
        """
        Return string representation of internal structure of the hash table.
        Useful for programmers for development and debugging.
        """
        return "\n".join(f"{b} : {b_contents}" for b, b_contents in enumerate(self._buckets))

    def __str__(self):
        """
        Return string represention of records in map.
        User-friendly output that usually hides implementation details.
        """
        return "{" + " , ".join(str(rec) for b in self._buckets for rec in b) + "}"


if __name__ == "__main__":
    hm = HashMap()
    for i in range(8):
        hm[i] = f"value{i}"
    print("="*80)
    print(repr(hm))
