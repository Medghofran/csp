from utils.parse import *


# a basic backtracking algorithm that does not take in charge the heuristics that can drastically reduce the search time
def backtrack_search(csp, assignment):
    if len(assignment) == len(csp.variables):
        return assignment
    varx = select_unassigned_variable(csp, assignment)
    domain_values = get_unordered_domain(varx, assignment, csp)

    for value in domain_values:
        print ("assignment :")
        log_state(assignments=assignment)
        print(consistent(value, assignment, csp))
        print ("running consistency test")
        if consistent(value, assignment, csp):
            print ("value is consistent")
            assign(assignment, value)
            print ("assignment :")
            log_state(assignments=assignment)
            res = backtrack_search(csp, assignment)
            if res:
                return res

        unassign(assignment, value)

    return False


# select the first variable from the list that does not yet been assigned.
def select_unassigned_variable(csp, assignment):
    unassigned_variables = [x for x in csp.variables if x not in assignment]
    print("variable is : " + str(unassigned_variables[0]))
    return unassigned_variables[0]


# omits the order domains values and returns the domains as is
def get_unordered_domain(varx, assignment, csp):
    return [v for v in csp.domains if v != varx]


# validate the consistency of the value according to the assignments and the constraints
# contained within the csp instance
def consistent(value, assignment, csp):
    for old_value in assignment:
        print("Old value :" + str(old_value))
        print("new value :" + str(value))
        for constraint in csp.constraints:
            evaluative = constraint.format(value, old_value)
            print("evaluating constraint : " + evaluative)
            r = eval(evaluative)
            print("constraint evaluated with result " + str(r))
            if not r:
                return False
    return True


# adds the given value to the assignment collection
def assign(assignment, value):
    assignment.append(value)


# removes a value from the given assignment
def unassign(assignment, value):
    print("trying to remove : " + str(value))
    print(assignment)

    if value in assignment:
        assignment.remove(value)


def log_state(assignments):
    for a in assignments:
        print a
        print ' '


csp = load_csp("../input/csp.txt")


ass = []
print(ass)

print("===> running backtrack search")
result = backtrack_search(csp, ass)
print(result)
