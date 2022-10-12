class DataClass:
    def __init__(self, array):
        self.array = array
    def _min(self):
        if len(self.array) == 1 and self.array[0] == '':
            return "array is empty"
        else:
            min_element = int(self.array[0])
            for i in range(1, len(self.array)):
                if min_element > int(self.array[i]):
                    min_element = int(self.array[i])
            return min_element
    def _max(self):
        if len(self.array) == 1 and self.array[0] == '':
            return "array is empty"
        else:
            max_element = int(self.array[0])
            for i in range(1, len(self.array)):
                if max_element < int(self.array[i]):
                    max_element = int(self.array[i])
            return max_element
    def _sum(self):
        if len(self.array) == 1 and self.array[0] == '':
            return "array is empty"
        else:
            sum_of_elements = 0
            for i in range(len(self.array)):
                sum_of_elements += int(self.array[i])
            return sum_of_elements
    def _mult(self):
        mult_of_elements = 1
        if len(self.array) == 1 and self.array[0] == '':
            return "array is empty"
        else:
            for i in range(len(self.array)):
                mult_of_elements *= int(self.array[i])
            return mult_of_elements