class integer_closed_interval:
    def __init__(self, lower, upper) -> None:
        self.lower = lower
        self.upper = upper
        if self.lower > self.upper:
            raise Exception

    def return_string(self):
        return f"[{self.lower},{self.upper}]"

    def invalid(self, std_range, inp_range):
        if std_range[0] > std_range[1] or inp_range[0] > inp_range[1]:
            return 0
    def compare_with_closed_interval(self, inp_range):
        if self.lower == inp_range[0] and self.upper == inp_range[1]:
            return 2
        elif self.lower <= inp_range[0] and inp_range[1] <= self.upper:
            return 3
        else:
            return 1
class input_digit():
    pass