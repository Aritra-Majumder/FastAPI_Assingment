from multiprocessing import Pool
import logging

def add_lists(lists):
    return [sum(sublist) for sublist in lists]

def add_numbers_batch(payload):
    try:
        with Pool() as pool:
            results = pool.map(add_lists, [payload])
        return results[0]
    except Exception as e:
        logging.error(f"Error in multiprocessing: {e}")
        raise
