class RemoteControl:
    def __init__(self):
        self.channels = ["StarSports", "Sony", "Espn", "Max", "DD National"]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]


remote = RemoteControl()
channel = iter(remote)
print(channel.__next__())
print(channel.__next__())
print(channel.__next__())
print(channel.__next__())
print(channel.__next__())
print(channel.__next__())



