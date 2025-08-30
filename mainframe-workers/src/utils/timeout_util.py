import signal


class Timeout:
    def __init__(self, seconds: int):
        self.seconds = seconds
        self.is_timeout = False

    def handle_timeout(self, signum, frame):
        self.is_timeout = True
        raise TimeoutError(f"Function execution time exceeded {self.seconds} seconds")

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type, value, traceback):
        signal.alarm(0)
