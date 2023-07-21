
def measure(bucket_one, bucket_two, goal, start_bucket):

    def get_options(node):
        options = [(bucket_one, node[1]), (node[0], bucket_two), (0, node[1]), (node[0], 0)]
        spacein2 = bucket_two - node[1]
        if spacein2 >= node[0]:
            options.append((0, node[1] + node[0]))
        else:
            options.append((node[0] - spacein2, bucket_two))
        spacein1 = bucket_one - node[0]
        if spacein1 >= node[1]:
            options.append((node[0] + node[1], 0))
        else:
            options.append((bucket_one, node[1] - spacein1))
        return [option for option in options if not visited(option) and legal(option)]


    def legal(node):
        return node not in illegal_nodes


    def visited(node):
        return node in all_nodes


    def check_step(step):
        for node in step:
            is_goal = check_if_goal(node)
            if is_goal:
                return is_goal
        return False


    def check_if_goal(node):
        if node[0] == goal:
            return len(steps), "one", node[1]
        elif node[1] == goal:
            return len(steps), "two", node[0]
        else:
            return False


    all_nodes = set()
    steps = []
    illegal_nodes = set()

    if start_bucket == 'one':
        steps.append({(bucket_one, 0)})
        illegal_nodes.add((0,bucket_two))
    elif start_bucket == 'two':
        steps.append({(0, bucket_two)})
        illegal_nodes.add((bucket_one, 0))
    
    while True:
        result = check_step(steps[-1])
        if result:
            return result
        step = set()
        for node in steps[-1]:
            for option in get_options(node):
                step.add(option)
        steps.append(step)
