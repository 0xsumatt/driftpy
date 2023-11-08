from abc import ABC, abstractmethod
import asyncio

class Polling(ABC):
    def __init__(self, frequency: float):
        self._is_subscribed = False
        self.frequency = frequency

    @abstractmethod
    async def poll_data(self):
        """Retrieve data from the source."""
        pass

    async def subscribe(self):
        """Starts the polling process with the user-defined frequency."""
        if self._is_subscribed:
            return

        self._is_subscribed = True
        try:
            while self._is_subscribed:
                await self.poll_data()
                await asyncio.sleep(self.frequency)
        finally:
            self._is_subscribed = False

    async def unsubscribe(self):
        """Stops the polling process."""
        self._is_subscribed = False
