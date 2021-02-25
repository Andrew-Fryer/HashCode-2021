import car


class Street:
    def __init__(self, queue, time_l, light, time_green):
        self.queue = queue
        self.time = time_l
        self.light = light
        self.time_green = time_green

    def add_to_queue(self, car):
        self.queue.append(car)

    def set_time_green(self, time):
        self.time_green = time_green

    def turn_light_green(self):
        cars_through_light = []
        for i in range(self.time_green):
            cars_through_light.append(self.queue.pop(0))
        return cars_through_light
