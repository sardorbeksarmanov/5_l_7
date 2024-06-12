# range(x) => (0, x -1) step = 1
# range(x, y) => (x, y-1) step = 1
# range(x, y, z) => (x, y - 1) step = z
import time


class Range:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.stop = start   # stop = 10
            self.start = -step  # start = -1
            self.step = step    # step = 1
        else:
            self.start = start - step
            self.stop = stop
            self.step = step

    def __iter__(self):
        print("call iter")
        return self

    def __next__(self):
        time.sleep(1)
        print("next iter")
        self.start += self.step
        if self.start >= self.stop:
            raise StopIteration
        return self.start

for i in Range(4, 25, 2.9):
    print(i)
