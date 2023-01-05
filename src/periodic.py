import asyncio
import threading
import time
from contextlib import suppress


# https://stackoverflow.com/questions/37512182/how-can-i-periodically-execute-a-function-with-asyncio
class PeriodicAsync:
    def __init__(self, func, time):
        self.func = func
        self.time = time
        self.is_started = False
        self._task = None

    async def start(self):
        if not self.is_started:
            self.is_started = True
            # Start task to call func periodically:
            self._task = asyncio.ensure_future(self._run())

    async def stop(self):
        if self.is_started:
            self.is_started = False
            # Stop task and await it stopped:
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task

    async def _run(self):
        while True:
            self.func()
            await asyncio.sleep(self.time)


class PeriodicSync:
    def __init__(self, func, time):
        self.func = func
        self.time = time
        self.is_started = False
        self._thread = None

    def start(self):
        if not self.is_started:
            self.is_started = True
            self._thread = threading.Thread(target=self._run)
            self._thread.start()

    def stop(self):
        if self.is_started:
            self.is_started = False
            self._thread.join()

    def _run(self):
        while True:
            if not self.is_started:
                break

            self.func()
            time.sleep(self.time)
