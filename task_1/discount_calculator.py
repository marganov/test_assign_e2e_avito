class DiscountCalculator:
    def __init__(self, points):
        if points < 0:
            raise ValueError("Invalid points value")
        self.points = points
        
    def get_discount(self):
        if 0 <= self.points <= 100:  # От 0 до 100 включительно -> 1%
            return 1
        elif 101 <= self.points <= 200:  # От 101 до 200 включительно -> 3%
            return 3
        elif 201 <= self.points <= 500:  # От 201 до 500 включительно -> 5%
            return 5
        else:  # 501 и выше -> 10%
            return 10
