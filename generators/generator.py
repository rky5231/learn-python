class RemoteControl:
    def __init__(self):
        self.channels = ["StarSports", "Sony", "Espn", "Max", "DD National"]
        self.index = -1

    def remote_control_next(self):
        while True:
            self.index += 1
            yield self.channels[self.index]



rc = RemoteControl()
print(rc.remote_control_next().__next__())
print(rc.remote_control_next().__next__())
print(rc.remote_control_next().__next__())
print(rc.remote_control_next().__next__())
print(rc.remote_control_next().__next__())
print(rc.remote_control_next().__next__())