class Checker:

    def __init__(self):
        self.subtraction_values = [(1, 2), (1231, 111), (818, 111)]
        self.multiply_values = [(1, 3), (2, 4), (10, 0)]
        self.division_values = [(1, 4), (2, 5), (19, 1)]
        self.square_values = [1, 4, 11]
        self.points = 0

    def check_subtraction(self):
        try:
            from exercises import subtract_numbers
        except:
            print("ERROR: subtract function not implemented")
            return 0

        initial_points = self.points
        try:
            test = 1
            for value in self.division_values:
                if value[0] - value[1] == subtract_numbers(value[0],value[1]):
                    print("Test {} for subtraction function --> OK".format(test))
                    self.points += 1
                else:
                    print("Test {} for subtraction function --> NOT OK".format(test))
                    print("Bad result for values: {}".format(value))

                test += 1

            if initial_points == self.points:
                print("It seems you haven't scored any points in subtraction. Maybe check if you are returning any results?")
        except:
            print("ERROR: There is a problem with your subtraction function. "
                  "Check to see if it is defined correctly.")

    def check_multiply(self):
        try:
            from exercises import multiply_numbers
        except:
            print("ERROR: multiply function not implemented")
            return 0

        initial_points = self.points
        try:
            test = 1
            for value in self.division_values:
                if value[0] * value[1] == multiply_numbers(value[0],value[1]):
                    print("Test {} for multiply function --> OK".format(test))
                    self.points += 1
                else:
                    print("Test {} for multiply function --> NOT OK".format(test))
                    print("Bad result for values: {}".format(value))

                test += 1

            if initial_points == self.points:
                print("It seems you haven't scored any points in multiply. Maybe check if you are returning any results?")
        except:
            print("ERROR: There is a problem with your multiply function. "
                  "Check to see if it is defined correctly.")

    def check_division(self):
        try:
            from exercises import divide_numbers
        except:
            print("ERROR: division function not implemented")
            return 0

        initial_points = self.points
        try:
            test = 1
            for value in self.division_values:
                if value[0] / value[1] == divide_numbers(value[0],value[1]):
                    print("Test {} for division function --> OK".format(test))
                    self.points += 1
                else:
                    print("Test {} for division function --> NOT OK".format(test))
                    print("Bad result for values: {}".format(value))

                test += 1

            if initial_points == self.points:
                print("It seems you haven't scored any points in division. Maybe check if you are returning any results?")
        except:
            print("ERROR: There is a problem with your division function. "
                  "Check to see if it is defined correctly.")

    def check_square(self):
        try:
            from exercises import square_up
        except:
            print("ERROR: square up function not implemented")
            return 0

        initial_points = self.points
        try:
            test = 1
            for value in self.square_values:
                if value ** 2 == square_up(value):
                    print("Test {} for square function --> OK".format(test))
                    self.points += 1
                else:
                    print("Test {} for square function --> NOT OK.format(test)")
                    print("Bad result for value/s: {}".format(value))

                test += 1

            if initial_points == self.points:
                print("It seems you haven't scored any points in square up. Maybe check if you are returning any results?")
        except:
            print("ERROR: There is a problem with your multiply function. "
                  "Check to see if it is defined correctly.")

    def show_score(self):
        total_points = len(self.division_values) + len(self.multiply_values) + \
                       len(self.square_values) + len(self.subtraction_values)
        print("You scored {} out of {} possible points.".format(self.points, total_points))


    def check_all(self):
        self.check_subtraction()
        self.check_multiply()
        self.check_division()
        self.check_square()
        self.show_score()


if __name__ == '__main__':
    c = Checker()
    c.check_all()
