# Python program for implementation of Bubble Sort
class Bubble:
    """Initializer of class takes series parameter and returns Class Object"""

    def __init__(self, arr):
        self.sorted = arr.copy()
        self.bubbleSort()

    def bubbleSort(self):
        n = len(self.sorted)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if self.sorted[j] > self.sorted[j + 1]:
                    self.sorted[j], self.sorted[j + 1] = self.sorted[j + 1], self.sorted[j]

    @property
    def result(self):
        return self.sorted


if __name__ == "__main__":

    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    b = Bubble(arr)

    print("original array is:")
    print(arr)
    print("Sorted array is:")
    print(b.result),
