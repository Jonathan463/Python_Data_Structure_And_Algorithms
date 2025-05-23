from ListComprehension import list_comprehension
from sorting4 import sorting4
from PhoneNumber import phone_number
from SideKick import Hero
from collections import deque
from collections import deque

# from Permutation import perm
comprehension = list_comprehension()


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
E = 0
C = 1
S = 2
start_stable = [C, C, C, C, E, S, S, S, S]
goal_stable = [S, S, S, S, E, C, C, C, C]



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def print_hello():
    print("Hello world")
    s = "Hello Earth"
    i = 1
    i += 1
    print(i)
    print(type(i))

    mylist = [1, 2, 3, 4, 5]
    print(mylist[0])
    print(mylist[3])

    newlist = mylist[:]
    newlist.remove(3)
    print(newlist)
    print(mylist)

    for a in range(11):
        if a > 2:
            print(a)

    for x in range(13):
        if x % 2 == 0:
            print(x)

    mylist = [1, "jack", 5.0, 6, 9, 13]
    for a in mylist:
        print("0" + str(a))

    mylist = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
    for val in mylist:
        if val == 3 or val == 3.0:
            print(val)


def two_player(number):
    number_of_pick = int(input("Enter number to pick "))
    # result = nim_game_controller(number_of_stick,number_of_pick)
    return number_of_pick


def single_player():
    pass


def computer_player():
    pass


def optimal_player():
    pass


def game_move_manager(number):
    total_number_of_stick = int(input("How many number of stick do you want to start with "))
    method_choice = int(input("Which type of player do you want? "))
    if method_choice == 2:
        number_of_pick = two_player(number)
        nim_game_controller(total_number_of_stick)


def nim_game_controller(number):
    winner_name = ["player1 won ", "player2 won"]
    print("player 1 goes first followed by player 2")
    print("total number of stick is " + str(number))
    winner = False
    while (number > 0):
        number_of_stick = two_player(number)
        if number_of_stick <= 3 and number_of_stick > 0 and number_of_stick <= number:
            print("Player1 picked " + str(number_of_stick))
            winner = True
            number = number - number_of_stick
            print("We have " + str(number) + " stick remaining")
        number_of_stick = two_player(number)
        if number_of_stick <= 3 and number_of_stick > 0 and number_of_stick <= number:
            print("Player2 picked " + str(number_of_stick))
            winner = False
            number -= number_of_stick
            print("We have " + str(number) + " stick remaining")
    if winner == False:
        return winner_name[1]
    if winner == True:
        return winner_name[0]


def listManipulation():
    mylist = ["foo", 1, 2.3, [5, 6, 7]]
    firstValueInNestedList = mylist[3][0]
    length = len(mylist[3])
    for a in mylist[3]:
        print(a)
    # print(firstValueInNestedList)
    # print(length)


def listOperation():
    mylist1 = [1, 2, 3]
    mylist2 = [4, 5, 6]
    mylist3 = mylist1 + mylist2
    print(mylist3)


# def colours1():
#  yield "red"
#  yield "green"
#  yield "black"
# for c in colours1():
#   print(c)

def colours():
    for c in ["red", "green", "black"]:
        yield c


for c in colours():
    print(c)


def successors(stable):
    #print(f'Original stable {stable}')
    # find empty spot
    empty = stable.index(E)
    #print(f"index of empty is {empty}")
    # generate list of unfiltered candidate positions
    candidates = [empty - 2, empty - 1, empty + 1, empty + 2]

    # keep only those which are inside the stable
    candidates = [c for c in candidates if c >= 0 and c < len(stable)]
    #print(f'positive candidate list {candidates}')
    # Cows can always move right, Sheep always left, and from two fields
    # apart, they have to jump over an opposite animal
    candidates = [c for c in candidates if
                  stable[c: c + 2] == [C, E] or  # cow can move right
                  stable[c - 1:c + 1] == [E, S] or
                  stable[c: c + 3] == [C, S, E] or  # sheep can move left cow jumps over sheep
                  stable[c - 2:c + 1] == [E, C, S]]  # sheep jumps over cow
    #print(f'candidate index list that meet our rules {candidates}')
    #print(f'did the stable change {stable}')
    # make sure that all these entries are occupied
    # (not necessary for operation, just better style)
    assert not [c for c in candidates if stable[c] == E]
    for c in candidates:
        new_stable = stable[:]  # make a copy

        # move the candidate into empty pos
        new_stable[c], new_stable[empty] = new_stable[empty], new_stable[c]
        #print(f'c is {c} and new_stable is {new_stable} ************** did stable change? {new_stable == stable}')
        yield new_stable


def solution(stable):
    if stable == goal_stable:
        return [stable]
    # else, depth first
    for new_stable in successors(stable):
        sol = solution(new_stable)
        print("sol ->",sol)
        if sol:
            return [stable] + sol


for s in solution(start_stable):
    print(s)


def clearAList(list):
  while list:
      list[:] = list[1:]
      if list == []:
          return list


def tower_of_hanoi(n, Source, Helper, Goal):
    if n==1:
        print(f'move the disk 1 from {Source} to {Goal}')
        return
    tower_of_hanoi(n-1, Source, Goal, Helper)
    print(f'move n-1 from {Goal} to {Source}')
    tower_of_hanoi(n-1, Helper, Source, Goal)


def hanoi(n,start,end):
    if n == 1:
        print(start,'->',end)
    else:
        other = 6 - (start + end)
        hanoi(n-1,start, other)
        print(start,'->',end)
        hanoi(n-1,other,end)


def pm(start,end):
   print(start,'->',end)


def bfs(graph,start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end="")
            visited.add(node)
            queue.extend(graph[node])

graph ={
    'A':['B','C'],
    'B':['A', 'D', 'E'],
    'C':['A', 'F', 'G'],
    'D':['B'],
    'E':['B', 'H'],
    'F':['C'],
    'G':['C'],
    'H':['E']
}
graph2 = {
    'A': ['B', 'C'],
    'B': ['E'],
    'C': ['F'],
    'E': [],
    'F': []
}

def perm(lst):
    if len(lst) <= 1:
        yield lst
    else:
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for p in perm(rest):
                yield [lst[i]] + p



def successor(state):
    p,n = state
    for i in range(1,min(3,n)+1):
        yield (not p,n-i)

def tupleTest(tuple):
    tuple[0] == "jonathan"
    print(tuple)

def result(sticks=10):
    if sticks == 0:
      return "lost"
    if sticks >= 1 and sticks <= 3:
        return "win"
    else:
        return "ongoing"


state = {
    ('hero',1):'left',
('kick',1):'left',
('hero',2):'left',
('kick',2):'left',
('hero',3):'left',
('kick',3):'left',
    'boat':'left'
}

other_side = {'left':'right','right':'left'}

def move_hero_sidekick(state):
    # clone a dictionary
    state_copy = state.copy()
    #passenger,boat = state

    boat = [key for key in state_copy if type(key) != tuple]
    list_of_hero_sidekick = [key for key in state_copy if type(key) == tuple]
    for person in list_of_hero_sidekick:
        if person == ('hero',1):
            position_of_hero1 = state_copy[('hero',1)]
            state_copy[('hero',1)] = other_side[position_of_hero1]

        elif person == ('kick',1):
            position_of_sidekick = state_copy[('kick',1)]
            state_copy[('kick',1)] = other_side[position_of_sidekick]

    boat_position = state_copy[boat[0]]
    state_copy[boat[0]] = other_side[boat_position]
    print(state_copy)

def seperate(state):
    copy = state.copy()
    for entities in copy:
        if isinstance(entities,tuple):
            _,value = entities
            if copy['hero',value] != copy['kick',value]:
                return True

    return False










state = {
    ('hero',1):'left',
    ('kick',1):'left',
('hero',2):'left',
('kick',2):'left',
('hero',3):'left',
('kick',3):'left',
'boat':'left'
}


def move_right(state):
    #Create copy of state
    state_copy = state.copy()
    #state = {**state}

    # data structure representing position

    move_to_other_side = {'left':'right', 'right':'left'}

    list_hero = [key for key in state_copy if key == ('hero',1)]
    list_kick = [key for key in state_copy if key == ('kick',1)]
    list_boat = [key for key in state_copy if key == 'boat']

    #get item position
    position_hero = state_copy[list_hero[0]]
    position_kick = state_copy[list_kick[0]]
    position_boat = state_copy[list_boat[0]]

    #chnaging the position of hero,kick and boat

    state_copy[list_hero[0]] = 'right'
    state_copy[list_kick[0]] = 'right'
    state_copy[list_boat[0]] = 'right'
    return state_copy





def breath_fs(graph, start):
  visited = set()
  q = deque([start])
  visited.add(start)
  while q:
   v= q.popleft()
   print(v)
   for u in graph[v]:
     if u not in visited:
         visited.add (u)
         q.extend(u)


def taken(sticks):
  if sticks == 1:
    return 1
  for move in range(1, min(3,sticks)+1):
    if (sticks - move - 1) % 4 == 0 and (sticks - move) > 0:
      return move
  return 1


def winning(sticks):
    move = (sticks - 1)%4
    print(f"move1 {move} and original stick {sticks}")
    move = (sticks )%5
    print(f"move2 {move} and original sticks {sticks}")


from collections import deque


def count_empty_lists_bfs(lst):
    count = 0
    queue = deque([lst])  # Use a queue to process elements level by level

    while queue:
        current = queue.popleft()  # Remove and process the first element (FIFO)

        if isinstance(current, list):
            if not current:  # Check if it's an empty list
                count += 1
            else:
                queue.extend(current)  # Add sublists to queue for further processing

    return count




nested_list = [[[[]], []], [[]],[],[]]  # Example nested list


def count_lists_that_contains_list_dfs(lst):
    count = 0
    stack = lst # Use a stack to manage elements
    print("stack ",stack)

    while stack:
        current = stack.pop()  # Get the last element
        print("current ",current)
        if isinstance(current, list):
            if current:  # Check if it contains something
                count += 1
                stack.extend(current)  # Add sublists to stack for further processing

    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # print_hello()
    # single_player(10)
    # print(comprehension)
    # list = "2345469596"
    # sorted_list = sorting4(list)
    # formed_number = phone_number(list)
    # print(formed_number)
    # game_move_manager(10,two_player(7))
    # hero = Hero()
    # sidekick = hero.start()
    # print(hero.start())
    # print(listManipulation())
    # print(listOperation())
    # print(colours())
    # print(perm([1,2,3,4,5]))
    #print(solution([1, 1, 1, 1, 0, 2, 2, 2, 2]))
    #print(clearAList([1,2,3,4]))
    #tower_of_hanoi(4,'A','B','C')
    #hanoi(3,1,3)
    #bfs(graph,'A')
    #print(list(perm([1,2,3,4,5])))
    # tupleTest(("Dubem",1))
    # for succ in successor((False,3)):
    #     print(succ)
    #print(result(3))
    #move_hero_sidekick(state)
    #print(seperate(state))
    #print(move_right(state))
    #breath_fs(graph2, 'A')
    #print(taken(11))
    #print(winning(20))
    print(count_lists_that_contains_list_dfs(nested_list))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
