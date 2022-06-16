
if __name__ == '__main__':
    input()
    max_weight = int(input())
    if max_weight != 0:
        weight_list = input().strip().split(' ')
        weight_list = [int(weight) for weight in weight_list]
        cost_list = input().strip().split(' ')
        cost_list = [int(cost) for cost in cost_list]
        combined_list = list(zip(weight_list, cost_list))
        combined_list = sorted(combined_list, key=lambda x: x[1]/x[0], reverse=True)
        mem_table = [[(0, []) for x in range(max_weight+2)]]
        for item_index in range(1, len(combined_list)+1):
            line = [(0, [])]
            item = combined_list[item_index-1]
            for weight in range(1, max_weight+2):
                new_possible_price = item[1] + mem_table[item_index-1][weight - item[0]][0] if weight - item[0] > 0 else 0
                new_possible_item_list = mem_table[item_index-1][weight - item[0]][1].copy()
                new_possible_item_list.append(item)
                if new_possible_price > mem_table[item_index-1][weight][0]:
                    line.append((new_possible_price, new_possible_item_list))
                else:
                    line.append(mem_table[item_index-1][weight])
            mem_table.append(line)
        result = mem_table[len(combined_list)][max_weight+1]
        print(result[0])
        print(sum(item[0] for item in result[1]))
        print(len(result[1]))
        print(' '.join(str(item[0]) for item in result[1]))
        print(' '.join(str(item[1]) for item in result[1]))
    else:
        print(0)
        print(0)
        print(0)
        print('')
        print('')