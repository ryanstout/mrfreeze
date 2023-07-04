# Shuffle an list and return the shuffled list
import hashlib
import os
import pickle
import random
from functools import wraps


def shuffle(l: list) -> list:
    return random.sample(l, len(l))


def memoize_to_disk(func):
    cache_dir = f"caches/{func.__name__}"
    os.makedirs(cache_dir, exist_ok=True)

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, kwargs))
        key_hash = hashlib.sha256(key).hexdigest()
        print("KEY HASH: ", key_hash)
        cache_path = os.path.join(cache_dir, key_hash)

        if os.path.exists(cache_path):
            with open(cache_path, "rb") as f:
                print(f"Loading cached result for {func.__name__}")
                return pickle.load(f)

        print("Run the function")
        result = func(*args, **kwargs)
        print("GOT RESULT: ", result)
        with open(cache_path, "wb") as f:
            pickle.dump(result, f)

        return result

    return wrapper
