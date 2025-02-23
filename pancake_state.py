class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        self.list_state = state_str.split(',')

        # Converting the string numbers to integers
        self.list_state = [int(num) for num in self.list_state]

    # returns an array of tuples of neighbor states and the cost to reach them: [(pancake_state1, cost1),
    # (pancake _state2, cost2)...]
    def get_neighbors(self):
        rtn_list = []
        for i in range(0, len(self.list_state)-1):
            pre = self.list_state[:i]
            post = self.list_state[i:][::-1]
            rev_list = pre + post
            state_str = ",".join(map(str, rev_list))
            rtn_pancake = pancake_state(state_str)
            rtn_list.append((rtn_pancake, sum(post)))
        return rtn_list

    # you can change the body of the function if you want
    def __hash__(self):
        return hash(self.state_str)

    # you can change the body of the function if you want
    def __eq__(self, other):
        return self.state_str == other.state_str

    def get_state_str(self):
        return self.state_str

    def get_list_state(self):
        return self.list_state

    def __repr__(self):
        return self.state_str
