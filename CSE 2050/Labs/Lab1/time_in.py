import time
from listmap import ListMapping
from hashmap import HashMap

def time_insertions(map_class, num_insertions_list):
    for n in num_insertions_list:
        start = time.time()
        m = map_class()
        for k in range(n):
            m[k] = f"value{k}"
        end = time.time()
        print(f"time to insert {n} records (s): {end - start}")


if __name__ == "__main__":
    L = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000]
    print("Python Dictionary".center(80, "="))
    time_insertions(dict, L)
    print("="*80)
    print()

    print("List Map".center(80, "="))
    time_insertions(ListMapping, L)
    print("="*80)
    print()

    # print("Hash Map".center(80, "="))
    # time_insertions(HashMap, L)
    # print("="*80)
    # print()
