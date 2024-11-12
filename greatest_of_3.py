from python_graphs import control_flow, control_flow_graphviz


def greatest_of_3(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > z) and (y > x):
        return y
    else:
        return z


graph = control_flow.get_control_flow_graph(greatest_of_3)
agraph = control_flow_graphviz.to_graphviz(graph)

agraph.layout(prog="dot")
agraph.draw("output.svg", format="svg")
