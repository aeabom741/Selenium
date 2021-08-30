class prime:

    def __init__(self,a):
        self.a = int(a)

    def is_prime(self):
        if self.a == 0:
            return False
        elif self.a % 2 == 1:
            return True
        else:
            return False