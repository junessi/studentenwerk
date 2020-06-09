def swap(data, a, b):
    t = data[a]
    data[a] = data[b]
    data[b] = t

def sink(data, i, n):
    while i < n:
        l = 2*i + 1
        r = 2*i + 2
        maxIndex = i

        if l < n and data[l] > data[maxIndex]:
            maxIndex = l

        if r < n and data[r] > data[maxIndex]:
            maxIndex = r

        if i == maxIndex:
            break

        swap(data, i, maxIndex)

        i = maxIndex

def build(data):
    i = len(data)/2 - 1
    while i >= 0:
        sink(data, i, len(data))

def sort(data):
    build(data)

    i = len(data) - 1
    while i > 0:
        swap(data, 0, i)
        sink(data, 0, i)
        i = i - 1
