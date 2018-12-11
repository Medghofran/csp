import json
import re
from argparse import Namespace
from functions import *
from csp.csp import *


def load_csp(file_path):
    json_file = open(file_path)
    json_str = json_file.read()

    json_data = json.loads(json_str, object_hook=lambda d: Namespace(**d))

    # check if this problem description has a matrix size or else work as in a table
    if hasattr(json_data, 'mat_size'):
        json_data.mat_size = MatSize(1, len(json_data.variables))

    # check and convert into a table if a range is given as argument
    variables = init_range(json_data.variables)

    # check and convert into a table if a range is given as argument
    domains = init_range(json_data.domains)

    # initialize the list of constraints
    constraints = init_constraints(json_data.constraints)

    # create an instance of csp and affect it's variables
    problem_csp = Csp(variables=variables, domains=domains, constraints=constraints, mat_size=json_data.mat_size)

    return problem_csp


def init_range(array):
    first_value = str(array[0])
    range_var = first_value.split("..")
    if len(range_var) > 1:
        min_range = int(range_var[0])
        max_range = int(range_var[1])
        range_list = list(range(min_range, max_range))
        return range_list

    return array


# cycles through the constraints of the problem and parse them
def init_constraints(constraints):
    parsed_constraints = []

    for constraint in constraints:
        con = parse_expression(str(constraint))
        parsed_constraints.append(con)

    return parsed_constraints


# parses the constraint into a ready to evaluate form.
def parse_expression(expression_string):
    var_pattern = "\\$[a-zA-Z]+"
    variables = re.findall(pattern=var_pattern, string=expression_string)
    l = []

    con = expression_string
    if variables:
        for variable in variables:
            if variable not in l:
                l.append(variable)

        for v in l:
            con = con.replace(v, "{" + str(l.index(v)) + "}")

    return con

