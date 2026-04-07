NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph:
    def __init__(self, data=[]):
        self.nodes = []
        self.edges = []
        self.attrs = {}

        # Validate that data is a List
        if isinstance(data, list):
            try:
                for domain_object in data:
                    self.add_domain_object(domain_object)
            except TypeError as te:  # Catch possible errors thrown below
                raise TypeError(f"{te}")
            except ValueError as ve:  # Catch possible error thrown below
                raise ValueError(f"{ve}")
        else:
            raise TypeError("Graph data malformed")

    def add_domain_object(self, domain_object):
        try:
            # Well formed items have the form
            # (TYPE, item1, item2, [item3])
            if len(domain_object) < 3:
                raise TypeError("Graph item incomplete")

            type = domain_object[0]
            if type not in range(3):
                raise ValueError("Unknown item")
            # Insert different types of items
            if type == NODE:
                self._add_node(domain_object)
            elif type == EDGE:
                self._add_edge(domain_object)
            elif type == ATTR:
                self._add_attr(domain_object)
        except TypeError as te:
            raise TypeError(f"{te}")
        except ValueError as e:
            raise ValueError(f"{e}")

    def _add_node(self, node):
        try:
            _, name, attrs = node
            self.nodes.append(Node(name, attrs))
        except:
            raise ValueError("Node is malformed")

    def _add_edge(self, edge):
        try:
            _, src, dst, attrs = edge
            self.edges.append(Edge(src, dst, attrs))
        except:
            raise ValueError("Edge is malformed")

    def _add_attr(self, attr):
        try:
            _, name, value = attr
            self.attrs[name] = value
        except:
            raise ValueError("Attribute is malformed")
