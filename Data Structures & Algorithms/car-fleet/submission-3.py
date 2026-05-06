class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        idea: find the time it takes for a car to ge to target and group on that?
        ex1:
        (target - pos)/ sp = time to get to pos
        sort by closest to target
        and then add to stack and pop if the new time is less or equal to
         '''
        pairs = [[p,s] for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []
        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()
        return len(stack)
        