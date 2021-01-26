# *************************************************************************** #
# Python class display four major sorting algorithms and their methodology    #
# *************************************************************************** #
import pygame
import time
import threading
import utility

# Set constants
SURFACE_SIZE = 900
GRAPH_SIZE = SURFACE_SIZE/3
OPERATION_KEYS = [pygame.K_SPACE, pygame.K_ESCAPE,
                  pygame.K_RETURN, pygame.K_BACKSPACE]


class Visual_sorting_algorithms:
    """ This class displays four graphs of major sorting algorithms using the
    pygame GUI. The graphs should work in relative time (using multi-threading)
    and be comparable between each algorithm.
    Usage: Press R to reset and generate a new set of arrays
    Input parameter: n - defines the length of the arrays being sorted
    Contains follow member methods:
        run(): Main control loop to start threads and draw, control and input
               of the processeses
        draw(): Draws the titles, counters and graphs
    """

    def __init__(self, n):

        # initialise
        pygame.init()

        # set window settings
        logo = pygame.image.load("src/logo148x148.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Visualise sorting algorithms")

        # set colours
        self.BACKGROUND = pygame.Color(220, 220, 220, 0)

        # set screen surface
        self.surface = pygame.display.set_mode((SURFACE_SIZE, SURFACE_SIZE))

        # set select box co-ords
        self.graph_coords = [[GRAPH_SIZE/3, GRAPH_SIZE/3],  # top left
                             [GRAPH_SIZE * 5/3, GRAPH_SIZE/3],  # top right
                             [GRAPH_SIZE/3, GRAPH_SIZE * 5/3],  # bot left
                             [GRAPH_SIZE * 5/3, GRAPH_SIZE * 5/3]]  # bot right

        # set array_length
        self.array_length = n

        # define value arrays
        self.random_array = utility.createRandList(self.array_length)
        self.sorted_array = utility.createSortedList(self.array_length)
        self.rev_sorted_array = utility.createRevSortedList(self.array_length)

        # define graph storing array
        self.graphs = []

        # define sorting algorithms
        self.algorithms = ['bubbleSort', 'quickSort', 'heapSort', 'mergeSort']

    def run(self):

        while(1):
            # output sort timing data to console
            utility.createSortTimeData(self.algorithms,
                                       [self.random_array[:],
                                        self.sorted_array[:],
                                        self.rev_sorted_array[:]])
            # create graph classes
            self.graphs = [graph(self.surface, self.random_array[:],
                                 self.graph_coords[i], algorithm)
                           for i, algorithm in enumerate(self.algorithms)]
            # start graph threads
            for grph in self.graphs:
                grph.start()

            restart = True
            while(restart):
                self.draw()
                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            restart = False
                            break

                        if event.key in OPERATION_KEYS:
                            pygame.quit()
                            quit()

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            self.random_array = utility.createRandList(self.array_length)
            self.sorted_array = utility.createSortedList(self.array_length)
            self.rev_sorted_array = utility.createRevSortedList(self.array_length)

    def draw(self):
        self.surface.fill(self.BACKGROUND)

        for i, graph in enumerate(self.graphs):
            graph.draw()

        pygame.display.update()


class graph(threading.Thread):
    """ This class creates a graph of major sorting algorithms using the pygame
    GUI. Each class runs in a separate thread to run independent.
    Contains follow member methods:
        run(): Main loop to run sorting algorithm
        draw(): main draw function (graph, title and counter)
        draw_title(): draws the graph title
        draw_counter(): draws the algorithm array swaps counter
        switch_threah(): Increments swap counter and initiates thread switch
                         through time.sleep()
        bubbleSort(): Implements iterative bubble sort algorithm
        quickSort(): Implements iterative quick sort algorithm
        heapSort(): Implements iterative heap sort algorithm
        heapify(): Builds max heap from array
        mergeSort(): Implements iterative merge sort algorithm
    """
    def __init__(self, surface, values, coords, algorithm):
        threading.Thread.__init__(self)

        self.surface = surface
        self.array = values

        # set absolute coords
        self.coords = coords
        self.title_coords = [coords[0] + GRAPH_SIZE/2, coords[1]-GRAPH_SIZE/15]
        self.counter_coords = [coords[0] + GRAPH_SIZE/2, coords[1]]

        # define algorithms
        self.algorithm = algorithm
        self.algo_methods = {
            'bubbleSort': self.bubbleSort,
            'quickSort': self.quickSort,
            'heapSort': self.heapSort,
            'mergeSort': self.mergeSort,
        }

        # set colours
        self.BLACK = pygame.Color(0, 0, 0, 0)
        self.RED = pygame.Color(220, 20, 20, 0)
        self.GREEN = pygame.Color(50, 180, 50, 0)

        # set fonts
        self.title_font = pygame.font.SysFont("calibri", 30)
        self.counter_font = pygame.font.SysFont("calibri", 15)

        # set variables
        self.sorted = 0
        self.counter = 0
        self.swap_A = None
        self.swap_B = None

    def run(self):
        self.algo_methods[self.algorithm]()  # call sort function
        self.switch_thread()
        self.sorted = 1
        self.draw()

    def draw(self):
        self.draw_title()
        self.draw_counter()

        colour = self.BLACK
        if self.sorted == 1:
            colour = self.GREEN

        for i, value in enumerate(self.array):  # draw each line in box
            x = self.coords[0] + (GRAPH_SIZE * (i / len(self.array)))
            y1 = self.coords[1] + GRAPH_SIZE
            y2 = self.coords[1] + GRAPH_SIZE - (GRAPH_SIZE * value/100)

            if i == self.swap_A or i == self.swap_B:
                pygame.draw.line(self.surface, self.RED,
                                 (x, y1), (x, y2), width=2)
            else:
                pygame.draw.line(self.surface, colour,
                                 (x, y1), (x, y2), width=2)

    def draw_title(self):
        text = str(self.algorithm)
        (text_width, text_height) = self.title_font.size(text)
        self.surface.blit(self.title_font.render(text, 1, self.BLACK),
                          (self.title_coords[0] - text_width/2,
                          self.title_coords[1] - text_height))

    def draw_counter(self):
        text = f"Array swaps: {str(self.counter)}"
        (text_width, text_height) = self.counter_font.size(text)
        self.surface.blit(self.counter_font.render(text, 1, self.BLACK),
                          (self.counter_coords[0] - text_width/2,
                          self.counter_coords[1] - text_height))

    def switch_thread(self, index_A=None, index_B=None):
        self.counter += 1
        self.swap_A = index_A
        self.swap_B = index_B
        time.sleep(0.01)  # initiates thread switch

    # ------------ ITERATIVE SORTING ALGORITHM IMPLEMENTATIONS ----------------

    # iterative merge sort implementation
    def bubbleSort(self):
        for j in range(len(self.array)):
            swap_count = 0
            for i in range(len(self.array) - j - 1):
                if self.array[i] > self.array[i + 1]:
                    self.array[i + 1], self.array[i] = self.array[i], self.array[i + 1]
                    self.switch_thread(i, i+1)
                    swap_count = 1

            # if iterate without swap, then sorted
            if swap_count == 0:
                break

        return self.array

    # iterative quick sort implementation
    def quickSort(self):

        low = 0
        high = len(self.array) - 1
        queue = [(low, high)]

        while(len(queue)):

            low, high = queue.pop(0)

            if low < high:

                pivot = self.array[(low + high) // 2]
                i = low - 1
                j = high + 1

                for n in range(0, high - low):
                    i += 1
                    while(self.array[i] < pivot):
                        i += 1

                    j -= 1
                    while(self.array[j] > pivot):
                        j -= 1

                    if i >= j:
                        break

                    self.array[i], self.array[j] = self.array[j], self.array[i]
                    self.switch_thread(i, j)

                queue.append((low, j))
                queue.append((j + 1, high))

        return self.array

    # iterative heap sort implementation
    def heapSort(self):

        # heapify build max tree
        for i in range(len(self.array)//2 - 1, -1, -1):
            parent = i

            self.heapify(self.array, len(self.array), parent)

        # remove max value from heap array and rebuild max tree
        for i in range(len(self.array) - 1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.switch_thread(0, i)

            parent = 0
            self.heapify(self.array, i, parent)

        return self.array

    # iterative heapify function
    def heapify(self, array, n, parent):

        while(True):
            largest = parent
            left_child = 2 * parent + 1
            right_child = 2 * parent + 2

            # check if left child is greater than parent
            if left_child < n and array[left_child] > array[largest]:
                largest = left_child
            # check if right child is greater than parent
            if right_child < n and array[right_child] > array[largest]:
                largest = right_child

            if largest == parent:
                return

            array[parent], array[largest] = array[largest], array[parent]
            self.switch_thread(parent, largest)

            parent = largest

    # iterative merge sort implementation
    def mergeSort(self):

        # initial full array queue
        queue = [(0, len(self.array))]
        index = 0

        # generate queue of sub-array indexes
        while(True):
            left, right = queue[index]
            middle = (right + left) // 2
            index += 1

            if (right - left <= 1):
                break
            queue.append((left, middle))
            queue.append((middle, right))

        # run from LIFO queue to merge sub-arrays
        while(len(queue)):

            left, right = queue.pop(-1)
            middle = (right + left) // 2

            index = left
            left_array = self.array[left:middle]
            right_array = self.array[middle:right]

            while len(left_array) > 0 and len(right_array) > 0:
                if left_array[0] < right_array[0]:
                    self.array[index] = left_array.pop(0)
                else:
                    self.array[index] = right_array.pop(0)
                self.switch_thread(index)
                index += 1

            # add anything remaining in arrays
            while len(left_array) > 0:
                self.array[index] = left_array.pop(0)
                self.switch_thread(index)
                index += 1

            while len(right_array) > 0:
                self.array[index] = right_array.pop(0)
                self.switch_thread(index)
                index += 1

        return self.array
