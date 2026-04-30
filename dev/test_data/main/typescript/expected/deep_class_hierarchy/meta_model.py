from icontract import DBC


@abstract
@serialization(with_model_type=True)
class Node(DBC):
    identifier: str

    def __init__(self, identifier: str) -> None:
        self.identifier = identifier


class Branch(Node, DBC):
    description: str

    def __init__(self, identifier: str, description: str) -> None:
        Node.__init__(self, identifier)
        self.description = description


class Leaf(Branch, DBC):
    value: int

    def __init__(
        self,
        identifier: str,
        description: str,
        value: int,
    ) -> None:
        Branch.__init__(self, identifier, description)
        self.value = value


class Blossom(Leaf, DBC):
    details: str

    def __init__(
        self,
        identifier: str,
        description: str,
        value: int,
        details: str,
    ) -> None:
        Leaf.__init__(self, identifier, description, value)
        self.details = details


class Container(DBC):
    node: Node

    def __init__(self, node: Node) -> None:
        self.node = node


__version__ = "dummy"
__xml_namespace__ = "https://dummy.com"
