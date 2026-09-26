class TimeMap:

    def __init__(self):
        self.values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values:
            self.values[key] = []
        paired = (value, timestamp)
        self.values[key].append(paired)

    def get(self, key: str, timestamp: int) -> str:
        target = timestamp
        vals = self.values.get(key, [])
        result = ""
        low = 0
        high = len(vals) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if vals[mid][1] > target:
                high = mid - 1
            else:
                result = vals[mid][0]
                low = mid + 1
        return result