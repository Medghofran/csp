def get_line(array, i, j, cols, rows):
    line_start = cols * i
    line_end = line_start + rows
    return array[line_start:line_end]


def get_column(array, i, j, cols, rows):
    indices = []
    for k in range(0, cols):
        indices.append(k * rows + j)

    return [array[i] for i in indices]


def diag(array, i, j, cols, rows):
    indices = []
    for k in range(1, rows):
        index = i + rows * k + 1
        if index < len(array):
            indices.append(index)
    return [array[i] for i in indices]


def line(i, rows):
    return i / rows


def column(j, cols):
    return j % cols
