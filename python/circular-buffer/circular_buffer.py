class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.clear()

    def read(self):
        value = self.buffer[self.oldest]
        if value is not None:
            self.buffer[self.oldest] = None
            self.oldest = self.next_index(self.oldest)
            return value
        else:
            raise BufferEmptyException('buffer is empty')

    def write(self, data):
        if self.buffer[self.next] is None:
            self.buffer[self.next] = data
            self.next = self.next_index(self.next)
        else:
            raise BufferFullException('buffer is full')

    def overwrite(self, data):
        try:
            self.write(data)
        except BufferFullException:
            self.buffer[self.oldest] = data
            self.oldest = self.next_index(self.oldest)

    def clear(self):
        self.buffer = [None] * self.capacity
        self.next = 0
        self.oldest = 0

    def next_index(self, i):
        i += 1
        if i == self.capacity:
            i = 0
        return i