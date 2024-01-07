from ortools.linear_solver import pywraplp

def LinearProgramming(): 
    # Create the linear solver with the GLOP backend. 
    solver = pywraplp.Solver.CreateSolver("GLOP")

    # Create the variables A, B, C, D and E with 
    # lower bound of 150, 100, 200, 400 and 350 respectively
    a = solver.NumVar(150, solver.infinity(), "a")
    b = solver.NumVar(100, solver.infinity(), "b")
    c = solver.NumVar(200, solver.infinity(), "c")
    d = solver.NumVar(400, solver.infinity(), "d")
    e = solver.NumVar(350, solver.infinity(), "e")

    print("Number of variables = ", solver.NumVariables())

    # Adding Cabling station constraints, 0.5A+1.5B+1.5C+D+0.5E≤1500
    solver.Add(0.5*a + 1.5*b + 1.5*c + d + 0.5*e <= 1500)

    # Adding Painting station constraints, A+0.5B+C+0.5D+1.5E≤2850
    solver.Add(a + 0.5*b + c + 0.5*d + 1.5*e <= 2850)

    # Adding Drilling station constraints, 3A+B+2C+3D+0.5E≤2350
    solver.Add(3*a + b + 2*c + 3*d + 0.5*e <= 2350)

    # Adding Assembly station constraints, 2A+4B+C+2D+1.5E≤2600
    solver.Add(2*a + 4*b + c + 2*d + 1.5*e <= 2600)

    # Adding Testing station constraints, 0.5A+B+0.5C+0.5D+2E≤1200
    solver.Add(0.5*a + b + 0.5*c + 0.5*d + 2*e <= 1200)

    # # Adding minimum production level for A, A≥150
    # solver.Add(a >= 150)

    # # Adding minimum production level for B, B≥100
    # solver.Add(b >= 100)

    # # Adding minimum production level for C, C≥200
    # solver.Add(c >= 200)

    # # Adding minimum production level for D, D≥400
    # solver.Add(d >= 400)

    # # Adding minimum production level for E, E≥350
    # solver.Add(e >= 350)

    print('Number of constraints =', solver.NumConstraints())

    # Objective function: 3000x + 1500y.
    solver.Maximize(90*a + 120*b + 150*c + 110*d + 130*e)

    # Invoke the solver and display the results.
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print('Solution:')
        print('Objective value =', solver.Objective().Value())
        print('a = ', a.solution_value())
        print('b = ', b.solution_value())
        print('c = ', c.solution_value())
        print('d = ', d.solution_value())
        print('e = ', e.solution_value())
    else:
        print('The problem does not have an optimal solution.')

    print('\nAdvanced usage:')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iterations' % solver.iterations())

if __name__ == "__main__": 
    LinearProgramming()