# a class that will define the board size for the problem.
class MatSize:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns


# a class that will represent the problem that wil be solved.
class Csp:
    def __init__(self, domains, constraints, variables, mat_size):
        self.variables = variables
        self.constraints = constraints
        self.domains = domains
        self.mat_size = mat_size

