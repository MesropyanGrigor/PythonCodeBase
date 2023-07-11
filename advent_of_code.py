import os
def day_2():
    print()
    import os

    cwd = os.path.dirname(__file__)

    input_file = os.path.join(cwd, "input_2.txt")
    print(input_file)

    assert os.path.isfile(input_file)
    content_game = []

    with open(input_file, 'r') as _file:
        content_game = _file.read().split("\n")

    #print(content_game)
    t1 = {
        "A" : "Rock", "B" : "Paper", "C" : "Scissors"
    }

    t2 = {
        "X" : "Rock", "Y" : "Paper", "Z" : "Scissors"
    }
    t3 = {
        "Rock": 1, "Paper" : 2, "Scissors": 3,
    }
    t4 = {"X":{"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"},
          "Z":{"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}}
    score = 0
    for line in content_game:
        if not line.strip():
            continue
        a, b = line.split()
        b_val = None
        if b == "Y":
            b_val = t1[a]
        else:
            b_val = t4[b][t1[a]]
        print(a, ' . ', b)
        val = 0
        if (t1[a], b_val) in (("Rock", "Paper"),("Paper", "Scissors"), ("Scissors", "Rock")):
            val = 6
        elif t1[a] == b_val:
            val = 3
        
        score += (val + t3[b_val])
    
    print(score)

    #score = 0
    #for line in content_game:
    #    if not line.strip():
    #        continue
    #    a, b = line.split()
    #    print(a, ' . ', b)
    #    val = 0
    #    if (t1[a], t2[b]) in (("Rock", "Paper"),("Paper", "Scissors"), ("Scissors", "Rock")):
    #        val = 6
    #    elif t1[a] == t2[b]:
    #        val = 3
    #    
    #    score += (val + t3[t2[b]])
    
    #print(score)
        



#day_2()


def day_3():
    import os

    cwd = os.path.dirname(__file__)

    input_file = os.path.join(cwd, "input.txt")
    print(input_file)

    assert os.path.isfile(input_file)

    content_rucksack = []

    with open(input_file, 'r') as _file:
        content_rucksack = _file.read().split()

    lower_case_val = 96

    upper_case_val = 38

    priority = 0

    for line in content_rucksack:
        l = len(line)//2
        #print(l)
        letter_set = set(line[0:l]) & set(line[l:])
        letter = letter_set.pop()
        print(letter, letter.isupper())
        priority += ord(letter) - upper_case_val if letter.isupper() else ord(letter) - lower_case_val
    print(f"Priority: {priority}")

    priority = 0

    for index in range(0, len(content_rucksack), 3):
        letter = (set(content_rucksack[index]) & set(content_rucksack[index+1]) & set(content_rucksack[index+2])).pop()
        print(letter)
        priority += ord(letter) - upper_case_val if letter.isupper() else ord(letter) - lower_case_val
        
    print(f"Priority: {priority}")



    #print(ord('a'), " .  ", ord('A'), 65- 27)

#day_3()

def day_8():
    cwd = os.path.dirname(__file__)

    input_file = os.path.join(cwd, "input_8.txt")
    print(input_file)

    trees = []

    with open(input_file, 'r') as _file:
        trees = _file.read().split()

    #trees = ["30373","25512","65332","33549","35390"]

    print(len(trees), "     ", len(trees[0]))

    count_of_visibility = 2*len(trees[0]) + 2*(len(trees[0]) - 2)

    print(count_of_visibility)

    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            node = trees[i][j]
            left_max = max(trees[i][:j])
            right_max = max(trees[i][j+1:])
            top_max = max([trees[k][j] for k in range(0, i)])
            bottom_max = max([trees[k][j] for k in range(i+1, len(trees))])
            if node > left_max or node > right_max or node > bottom_max or node > top_max:
                count_of_visibility += 1
    
    print(count_of_visibility)

def read_file(name):
    cwd = os.path.dirname(__file__)

    input_file = os.path.join(cwd, name)
    print(input_file)

    data = []

    with open(input_file, 'r') as _file:
        data = _file.read().split("\n")

    return data

def day_8_2_part():
    cwd = os.path.dirname(__file__)

    input_file = os.path.join(cwd, "input_8.txt")
    print(input_file)

    trees = []

    with open(input_file, 'r') as _file:
        trees = _file.read().split()

   # trees = ["30373","25512","65332","33549","35390"]

    print(len(trees), "     ", len(trees[0]))

    #count_of_visibility = 2*len(trees[0]) + 2*(len(trees[0]) - 2)



    #print(count_of_visibility)

    def find_trees(trees, pivot, p=0):
        if p:
            print(trees)
        filtered_trees = []
        #trees_orders = trees if not reverse else reversed(trees)
        for tree in trees:
            #breakpoint()
            if pivot > tree:
                filtered_trees.append(tree)
            else:
                filtered_trees.append(tree)
                break
        return filtered_trees

    weigth_array = []
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            node = trees[i][j]
            #if node == '5':
            #    breakpoint()
            left_max = find_trees(list(reversed(trees[i][:j])), node)
            right_max = find_trees(trees[i][j+1:], node)
            #breakpoint()
            top_max = find_trees(list(reversed([trees[k][j] for k in range(0, i)])), node)
            bottom_max = find_trees([trees[k][j] for k in range(i+1, len(trees))], node)
            print(node, ",", len(left_max)*len(right_max)*len(top_max)*len(bottom_max), end="|")
            weigth_array.append(len(left_max)*len(right_max)*len(top_max)*len(bottom_max))
            #weigth_array.append((len(left_max)*len(right_max)*len(top_max)*len(bottom_max), (node, i, j, (len(left_max),len(right_max),len(top_max),len(bottom_max)))))
        print()
    
    print(weigth_array)
    print("max=",max(weigth_array))



#day_8_2_part()

def day_1():

    data = read_file("input_1.txt")
    print(data)
    calories = []
    total = 0
    for calory in data:
        
        if not calory:
            calories.append(total) 
            total = 0
            continue
        total += int(calory)

    print(sum(sorted(calories)[-3:]))

#day_1()


def day_4():
    data = read_file("input_4.txt")
    print(data)

    count = 0
    count_1 = 0
    data1 = ["2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"]
    for index in range(len(data)):
        line = data[index]
        pair_1, pair_2 = line.split(',')
        p1, p2 = pair_1.split('-')
        pp1, pp2 = pair_2.split('-')
        #if int(p1) >= int(pp1) and int(p2) <= int(pp2) or int(p1) <= int(pp1) and int(p2) >= int(pp2):
        #    count += 1
        if int(pp2) >= int(p1) >= int(pp1) or int(pp1) <= int(p2) <= int(pp2) or int(p1) <= int(pp1) <= int(p2) or int(p2) >= int(pp2)>= int(p1):
            count_1 += 1
        #for _ in range(len(data)):
        #    if _ == index:
        #        continue
        #    pair_1_, pair_2_ = data[_].split(',')
        #    p1_, p2_ = pair_1_.split('-')
        #    pp1_, pp2_ = pair_2_.split('-')
        #    if int(p1) >= int(p1_) and int(p2) <= int(p2_) and int(pp1) >= int(pp1_) and int(pp2) <= int(pp2_):
        #        count += 1

    print(count_1)

#day_4()

def day_5():
    crates = {
        1 : ['W','R','F'],
        2 : ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
        3 : ['P', 'M', 'Z', 'N', 'L'],
        4 : ['J', 'C', 'H', 'R'],
        5 : ['C', 'P', 'G', 'H', 'Q', 'T', 'B'],
        6 : ['G', 'C', 'W', 'L', 'F', 'Z'],
        7 : ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'],
        8 : ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
        9 : ['J', 'W', 'H', 'G', 'R', 'S', 'V'],
    }

    data = read_file("input_5.txt")
    for line in data:
        if not line.startswith('move'):
            continue
        sp_line = line.split()
        size = int(sp_line[1])
        index_1 = int(sp_line[3])
        index_2 = int(sp_line[5])
        print(f"move {size} from {index_1} to {index_2}")
        #### part 1
        #for i in range(size):
            #if crates[index_1]:
        #    crates[index_2].append(crates[index_1].pop())

        ### part 2
        crates[index_2].extend(crates[index_1][-1*size:])
        del crates[index_1][-1*size:] 

    print(crates)
    answer = ""
    for i in range(9):
        answer += crates[i+1][-1:][0] 
        print(crates[i+1][-1:])
    print(answer)
    #print(data)

#day_5()


def day_6():
    data = read_file("input_6.txt")[0]
    j = 14
    #data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    #data = "nppdvjthqldpwncqszvftbrmjlhg"
    #data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    for i in range(0, len(data) - 4, 1):
        chars = data[i:i+14]
        print(chars)
        if len(set(chars)) < 14:
            j+=1
        else:
            break

    print(data, "   ", j)


#day_6()

def day_7():
    data = read_file("input_7.txt")
    data1 = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split('\n')
    dirs2size = {}
    dirs2dirs = {}
    total_dirs2size = {}
    #
    # print(data)
    size = 100000
    current_dir = None
    paths = []
    for line in data:
        line_sp = line.split()
        if not line_sp:
            continue
        #print(line_sp)
        if line.startswith('$ cd') and not line.startswith("$ cd .."):
            current_dir = line_sp[-1]
            dirs2size[current_dir] = 0
            dirs2dirs[current_dir] = []
            paths.append(current_dir)
        elif line.startswith('dir'):
            dir_name = line_sp[1]
            dirs2dirs[current_dir].append(dir_name)
        elif line_sp[0].isdigit():   
            dirs2size[current_dir] += int(line_sp[0])
        elif line.startswith("$ cd .."):
            paths.pop()
            current_dir = paths[-1]


    print(dirs2dirs)
    print(dirs2size)

    def count_size(dirs, dirs2size, dirs2dirs):
        size = 0
        for dir in dirs:

            size += dirs2size.get(dir, 0)
            size+=count_size(dirs2dirs.get(dir, []), dirs2size, dirs2dirs)
        return size

    for key, val in dirs2dirs.items():
        total_dirs2size[key] = dirs2size.get(key, 0) +  count_size(val, dirs2size, dirs2dirs)

    print(total_dirs2size)

    total = 0
    ot = 0
    for key, val in total_dirs2size.items():
        if val <= size:
           # print(val)
            total += val
            
        if key != '/':
            ot += val
        
    

    #print(ot, ' .       ', total_dirs2size['/'])

    print(total)


def day_7_1():
    #inputs = read_file("input_7.txt")
    inputs = []
    for i in open("/Users/grigor/Desktop/input_7.txt", "r").read().split("\n"):
        i = i.replace("$ ", "")    
        if i[0:2] != "ls" and i[0:3] != "dir":
            inputs.append(i)
    stack = []
    sizes = {}
    for i in range(len(inputs)):
        line = inputs[i]    
        if line[0:2] == "cd" and ".." in line:
            stack.pop()    
        elif line[0:2] == "cd":
            stack.append(i)        
            sizes[i] = 0    
        else:        
            if not line:
                continue
            size = int(line.split(" ")[0])        
            for s in stack:            
                sizes[s] += size

    part1_answer = sum([sizes[i] for i in sizes if sizes[i] <= 100000])
    print("Part 1 answer: ", part1_answer)

    unused = 70000000 - sizes[0]
    unused_needed = 30000000 - unused
    potential_deletes = [sizes[i] for i in sizes if sizes[i] >= unused_needed]
    part2_answer = min(potential_deletes)
    print("Part 2 answer: ", part2_answer)


day_7_1()