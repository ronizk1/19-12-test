
def myzip(it1, it2):
    # Get iterators for the input collections
    iter1 = iter(it1)
    iter2 = iter(it2)

    # Continue until either iterator is exhausted
    while True:
        try:
            # Get the next element from each iterator
            elem1 = next(iter1)
            elem2 = next(iter2)

            # Yield a tuple containing elements from both iterators
            yield (elem1, elem2)

        except StopIteration:
            # If either iterator is exhausted, break the loop
            break