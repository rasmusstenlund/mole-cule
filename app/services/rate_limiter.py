import time
import threading

class token_bucket:

    def __init__(self, max_tokens: float, refill_rate: float):

        self.max_tokens = max_tokens
        self.refill_rate = refill_rate
        self.tokens = max_tokens
        self.last_update = time.time()
        self.lock = threading.Lock()


    def _refill(self):
        time_now = time.time()

        time_elapsed = time_now - self.last_update

        self.last_update = time_now

        potential_tokens = self.tokens + (time_elapsed * self.refill_rate)

        self.tokens = min(self.max_tokens, potential_tokens)


    def consume(self, tokens:int) -> bool:
        
        with self.lock:
            self._refill()

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True

            else:
                return False
            
    def get_remaining(self):

        with self.lock:
            self._refill()
            return self.tokens
        
    def get_cooldown(self, tokens_needed: int) -> float:
        with self.lock:
            self._refill()
            if self.tokens >= tokens_needed:
                return 0.0
            
            return (self.tokens - tokens_needed) / self.refill_rate

class rate_limiter_store:

    def __init__(self, max_tokens: float, refill_rate: float):

        self.max_tokens = max_tokens
        self.refill_rate = refill_rate 
        self._buckets: dict[str, token_bucket] = {}
        self._lock = threading.Lock()

    def get_bucket(self, key: str) -> token_bucket:

        with self._lock:
            if key not in self._buckets:
                self._buckets[key] = token_bucket(
                    max_tokens = self.max_tokens,
                    refill_rate = self.refill_rate,
                )
            return self._buckets[key]

