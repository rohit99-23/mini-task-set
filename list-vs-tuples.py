import sys
import timeit

# 1. Memory usage difference
list_data = [1, 2, 3, 4, 5]
tuple_data = (1, 2, 3, 4, 5)

print("=== Memory Usage (in bytes) ===")
print("List  :", sys.getsizeof(list_data))
print("Tuple :", sys.getsizeof(tuple_data))

# 2. Speed difference
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=10_000_00)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=10_000_00)

print("\n=== Creation Speed (smaller is faster) ===")
print(f"List  : {list_time:.6f} sec")
print(f"Tuple : {tuple_time:.6f} sec")

# 3. Mutability test
print("\n=== Mutability Test ===")
try:
    list_data[0] = 100
    print("List modified successfully:", list_data)
except TypeError as e:
    print("List error:", e)

try:
    tuple_data[0] = 100
    print("Tuple modified successfully:", tuple_data)
except TypeError as e:
    print("Tuple error:", e)

# 4. Hashability test
print("\n=== Hashability Test ===")
try:
    hash(tuple_data)  # Works if elements are hashable
    print("Tuple is hashable ")
except TypeError as e:
    print("Tuple error:", e)

try:
    hash(list_data)  # Always fails
    print("List is hashable ")
except TypeError as e:
    print("List error:", e)
