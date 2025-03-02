class DiscountCcalculator:
    def __init__(self, points):
        self.points = points
    
    def get_discount(self):
        if self.points < 100:
            return 1
        elif self.points < 200:
            return 3
        elif self.points < 500:
            return 5
        else:
            return 10