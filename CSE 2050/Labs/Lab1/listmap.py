class Record:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.key} : {self.value}"

class ListMapping:
    def __init__(self):
        self._buckets = []
        self._len = 0

    def __len__(self):
        return self._len

    def __setitem__(self, k, v):
        rec = self._record(k)
        if rec is not None:
            rec.value = v
        else:
            self._buckets.append(Record(k, v))
            self._len += 1

    def __getitem__(self, k):
        rec = self._record(k)
        if rec is not None:
            return rec.value
        raise KeyError

    def __contains__(self, k):
        return self._record(k) is not None

    def _record(self, k):
        for rec in self._buckets:
            if rec.key == k:
                return rec
        return None

    def __repr__(self):
        return "{" + " , ".join(str(rec) for rec in self._buckets) + "}"


if __name__ == "__main__":
    m = ListMapping()
    m[1] = "one"
    m[2] = "two"
    print(m)
    m[2] = "TWO"
    print(m)