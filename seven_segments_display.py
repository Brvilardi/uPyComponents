from machine import Pin


class SevenSegmentsDisplay:
    """
    Seven segments display class. This was tested with a common cathode display (5611BH and 5011BS), but it should work with a common anode display as well.

    It requires 8 pins to work (all of them should be Pin.OUT), one for each segment and one for the decimal point. If it is a common cathode you should pass common_anode=False to the constructor.
    """


    segments_matrix = {
        #   a,       b,      c,      d,      e,      f,      g,      dp
        0: [True, True, True, True, True, True, False, True],
        1: [False, True, True, False, False, False, False, True],
        2: [True, True, False, True, True, False, True, True],
        3: [True, True, True, True, False, False, True, True],
        4: [False, True, True, False, False, True, True, True],
        5: [True, False, True, True, False, True, True, True],
        6: [True, False, True, True, True, True, True, True],
        7: [True, True, True, False, False, False, False, True],
        8: [True, True, True, True, True, True, True, True],
        9: [True, True, True, True, False, True, True, True]

    }

    def __init__(self, a: Pin, b: Pin, c: Pin, d: Pin, e: Pin, f: Pin, g: Pin, dp: Pin, common_anode: bool = True):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.dp = dp

        if not common_anode:
            for i in self.segments_matrix:
                self.segments_matrix[i] = list(map(lambda x: not x, self.segments_matrix[i]))

        self.write(0)

    def write(self, number: int):
        """
        Write a number to the display
        :param number: Number to write to the display (int)
        :return:
        """
        if 9 < number < 0:
            raise ValueError("Number must be between 0 and 9")

        self.a.value(self.segments_matrix[number][0])
        self.b.value(self.segments_matrix[number][1])
        self.c.value(self.segments_matrix[number][2])
        self.d.value(self.segments_matrix[number][3])
        self.e.value(self.segments_matrix[number][4])
        self.f.value(self.segments_matrix[number][5])
        self.g.value(self.segments_matrix[number][6])
        self.dp.value(self.segments_matrix[number][7])

