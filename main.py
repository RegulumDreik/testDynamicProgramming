def combine_weight_cost(weight_list, cost_list):
    combined_list = [
        (cost/weight, (weight, cost))
        for weight, cost in zip(weight_list, cost_list)
    ]
    return sorted(combined_list, key=lambda x: x[0], reverse=True)


def find_optimal(info_list, max_weight):
    for index in range(len(info_list)):
        if info_list[index][1][0] <= max_weight:
            return index


def pack_backpack_greedy(info_list, max_weight):
    flag = True
    backpack = []
    while max_weight > 0 and flag:
        optimal_index = find_optimal(info_list, max_weight)
        if optimal_index is None:
            flag = False
            continue
        optimal_item = info_list.pop(optimal_index)
        backpack.append(optimal_item[1])
        max_weight = max_weight - optimal_item[1][0]
    return backpack


if __name__ == '__main__':
    input()
    max_weight = int(input())
    weight_list = input().strip().split(' ')
    weight_list = [int(weight) for weight in weight_list]
    cost_list = input().strip().split(' ')
    cost_list = [int(cost) for cost in cost_list]
    combined_list = combine_weight_cost(weight_list, cost_list)
    result_backpack = pack_backpack_greedy(combine_weight_cost(weight_list, cost_list), max_weight)
    backpack_costs = [item[1] for item in result_backpack]
    backpack_weights = [item[0] for item in result_backpack]
    print(sum(backpack_costs))
    print(sum(backpack_weights))
    print(len(result_backpack))
    print(' '.join(str(item) for item in backpack_weights))
    print(' '.join(str(item) for item in backpack_costs))
