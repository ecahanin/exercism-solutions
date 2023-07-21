class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None
    records.sort(key=lambda x: x.record_id)
    if records[0].parent_id != 0 or records[0].record_id != 0:
        raise ValueError('must have root node')
    if records[-1].record_id != len(records) - 1:
        raise ValueError('Tree must be continuous')
    root = Node(records[0].record_id)
    nodes = [root]
    for record in records[1:]:
        if record.record_id <= record.parent_id:
            raise ValueError("not a valid record")
        node = Node(record.record_id)
        nodes.append(node)
        nodes[record.parent_id].children.append(node)
    return root