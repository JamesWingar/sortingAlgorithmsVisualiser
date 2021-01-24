# *************************************************************************** #
# Python class display four major sorting algorithms and their methodology    #
# *************************************************************************** #
import pygame

# Set constants
SURFACE_SIZE = 675
GRAPH_SIZE = SURFACE_SIZE/3
OPERATION_KEYS = [pygame.K_SPACE, pygame.K_ESCAPE,
                  pygame.K_RETURN, pygame.K_BACKSPACE]


class Visual_sorting_algorithms:
    """ This class displays four graphs of major sorting algorithms using the
    pygame GUI. The graphs should work in realtime (using multi-threading) and
    be comparable between each algorithm.
    Usage:
    Input parameter:
    Contains follow member methods:
        run(): Main loop to run the Draw and Input of the program
    """

    def __init__(self, random_values):
        # initialise
        pygame.init()

        # set window settings
        logo = pygame.image.load("src/logo148x148.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Visualise sorting algorithms")

        # set colours
        self.BACKGROUND = pygame.Color(220, 220, 220)
        self.BLACK = pygame.Color(0, 0, 0, 0)
        self.RED = pygame.Color(220, 20, 20, 0)
        self.GREEN = pygame.Color(50, 200, 50, 0)
        self.GREY = pygame.Color(120, 120, 120, 0)

        # set random value list
        self.random_values = random_values

        # set fonts
        self.title_font = pygame.font.SysFont("calibri", 50)

        # set select box co-ords
        self.graph_coords = [[GRAPH_SIZE/3, GRAPH_SIZE/3],  # top left
                             [GRAPH_SIZE * 5/3, GRAPH_SIZE/3],  # top right
                             [GRAPH_SIZE/3, GRAPH_SIZE * 5/3],  # bot left
                             [GRAPH_SIZE * 5/3, GRAPH_SIZE * 5/3]]  # bot right

        self.graph_title_coords = [[self.graph_coords[0][0] + GRAPH_SIZE/2, self.graph_coords[0][1] - GRAPH_SIZE/4],
                                   [self.graph_coords[1][0] + GRAPH_SIZE/2, self.graph_coords[1][1] - GRAPH_SIZE/4],
                                   [self.graph_coords[2][0] + GRAPH_SIZE/2, self.graph_coords[2][1] - GRAPH_SIZE/4],
                                   [self.graph_coords[3][0] + GRAPH_SIZE/2, self.graph_coords[3][1] - GRAPH_SIZE/4]]

        # created graph classes
        self.graphs = [[]]

        # set screen surface
        self.surface = pygame.display.set_mode((SURFACE_SIZE, SURFACE_SIZE))

    def run(self):
        while(self.check_sorted()):
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.draw()

        close = True
        while(close):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key in OPERATION_KEYS:
                        close = False

        return self.current_sudoku

    def draw(self):
        for graph in range(len(self.graphs)):
            self.draw_graph(graph)
        return

    def draw_graph(self):
        for graph in range(len(self.graphs)):
            graph.update()
        return

    def check_sorted(self):
        return


class graph:
    """ This class creates a graph with the associated  four graphs of major sorting algorithms using the
    pygame GUI. The graphs should work in realtime (using multi-threading) and
    be comparable between each algorithm.
    Usage:
    Input parameter:
    Contains follow member methods:
        run(): Main loop to run the Draw and Input of the program
    """
    def __init__(self, values, coords, algorithm):
        self.array = values
        self.current_array = values[:]

        self.sorted = False

        self.coords = coords
        self.algorithm = algorithm

    def run():
        # call sort function
        # call draw function
        return

    def draw(self):
        # draw each line in box
        return

    def is_sorted(self, array):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return False
        return True
