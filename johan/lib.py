def partition_at_value(array, value):
    partition = []
    for x in array:
        if x != value:
            partition.append(x)
        else:
            if partition:
                yield partition
            partition = []
    if partition:
        yield partition
