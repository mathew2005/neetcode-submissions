class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # car can't pass car ahead of it (it can only catch up and drive at the same speed)
        # fleet (1 or more cars at same speed and position)
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        stack = []
        for (pos,speed) in cars:
            t = (target - pos) / speed
            stack.append(t)
            if len(stack) >= 2 and t <= stack[-2]:
                stack.pop()
        return len(stack)


            