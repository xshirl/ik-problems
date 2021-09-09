class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = []
        durations = []
        durations.append([releaseTimes[0], keysPressed[0]])
        for i in range(1, len(releaseTimes)):
            durations.append([releaseTimes[i] - releaseTimes[i-1], keysPressed[i]])
        durations.sort(key=lambda x: (x[0],x[1]))
        return durations[-1][1]
        
  class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowest_key = 'a'
        longest_duration = 0
        n = len(keysPressed)

        for i in range(n):
            pressedTime = releaseTimes[i - 1] if i > 0 else 0
            duration = releaseTimes[i] - pressedTime
            if duration == longest_duration:
                slowest_key = max(slowest_key, keysPressed[i])
            elif duration > longest_duration:
                slowest_key = keysPressed[i]
                longest_duration = duration

        return slowest_key

            
            