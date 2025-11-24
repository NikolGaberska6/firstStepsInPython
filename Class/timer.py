import time
class Timer:
    def __init__(self):
        self.seconds = 0

    def start(self):
        for i in range(5):
            self.seconds +=1
            print(self.seconds)
            time.sleep(1)

    def reset(self):
        self.seconds = 0

Timer().start()
Timer().reset()
