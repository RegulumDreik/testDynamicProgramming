def combine_weight_cost(
    weight_list: list[int],
    cost_list: list[int],
) -> list[tuple[float, tuple[int, int]]]:
    combined_list = [
        (cost/weight, (weight, cost))
        for weight, cost in zip(weight_list, cost_list)
    ]
    return sorted(combined_list, key=lambda x: x[0], reverse=True)


def find_optimal(info_list: list[tuple[float, tuple[int, int]]], max_weight: int) -> int | None:
    for index in range(len(info_list)):
        if info_list[index][1][0] <= max_weight:
            return index


def pack_backpack_greedy(
    info_list: list,
    max_weight: int,
) -> tuple[int, int, int, list[int], list[int]]:
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
    backpack_costs = [item[1] for item in backpack]
    backpack_weights = [item[0] for item in backpack]
    return sum(backpack_costs), sum(backpack_weights), len(backpack), backpack_weights, backpack_costs

if __name__ == '__main__':
    input()
    max_weight = int(input())
    weight_list = input().split(' ')
    weight_list = [int(weight) for weight in weight_list]
    cost_list = input().split(' ')
    cost_list = [int(cost) for cost in cost_list]
    combined_list = combine_weight_cost(weight_list, cost_list)
    result = pack_backpack_greedy(combined_list, max_weight)
    print(result[0])
    print(result[1])
    print(result[2])
    print(' '.join(str(item) for item in result[3]))
    print(' '.join(str(item) for item in result[4]))
