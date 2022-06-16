import sys

if __name__ == '__main__':
    sys.stdin.readline()
    max_weight = int(sys.stdin.readline())
    if max_weight != 0:
        weight_list = sys.stdin.readline().strip().split(' ')
        weight_list = map(int, weight_list)
        cost_list = sys.stdin.readline().strip().split(' ')
        cost_list = map(int, cost_list)
        combined_list = list(zip(weight_list, cost_list))
        mem_table = [[(0, []) for x in range(max_weight+2)]]
        previous_line = mem_table[0]
        for item_index, item in enumerate(combined_list):
            line = [(0, [])]
            line.extend(previous_line[1:item[0]+1])
            for weight in range(item[0]+1, max_weight+2):
                empty_weight_cell = previous_line[weight - item[0]]
                new_possible_price = item[1] + empty_weight_cell[0]
                if new_possible_price > previous_line[weight][0]:
                    new_possible_item_list = empty_weight_cell[1][:]
                    new_possible_item_list.append(item)
                    line.append((new_possible_price, new_possible_item_list))
                else:
                    line.append(previous_line[weight])
            mem_table.append(line)
            previous_line = line
        result = mem_table[len(combined_list)][max_weight+1]
        weights, costs = zip(*result[1])
        sys.stdout.write(str(result[0])+'\n')
        sys.stdout.write(str(sum(weights))+'\n')
        sys.stdout.write(str(len(result[1]))+'\n')
        sys.stdout.write(' '.join(map(str, weights))+'\n')
        sys.stdout.write(' '.join(map(str, costs))+'\n')
    else:
        sys.stdout.write('0\n')
        sys.stdout.write('0\n')
        sys.stdout.write('0\n')
        sys.stdout.write('\n')
        sys.stdout.write('\n')
