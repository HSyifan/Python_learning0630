# 展示所有牌型（考虑到用户自己输入比较麻烦，展示出来便于拷贝）
def show_cards():
    all_cards = ["♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦J", "♦Q", "♦K", "♦1", "♦2",
                 "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♥1", "♥2",
                 "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K", "♣1", "♣2",
                 "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "♠1", "♠2",
                 "🌙", "☀"]
    
    all_cards = all_cards[::-1]

    for i in range(54):
        print(all_cards.pop(), end=' ')
        if (i+1) % 13 == 0:
            print()
    print()
    

# 2 张拍的情况：对牌
def is_pair(cards):
    if cards[0] == cards[1]:
        return True
    else:
        return False


# 2 张牌的情况：火箭
def is_rocket(cards):
    if 14 in cards and 15 in cards:
        return True
    else:
        return False


# 3 张牌的情况：三张牌相同
def is_three(cards):
    if len(set(cards)) == 1:
        return True
    else:
        return False


# 4 张牌的情况：炸弹
def is_bomb(cards):
    if len(set(cards)) == 1:
        return True
    else:
        return False


# 4 张牌的情况：三带一
def is_three_one(cards):
    for each in cards:
        if cards.count(each) == 3:
            return True
    else:
        return False


# 5 张牌的情况：三带二
def is_three_two(cards):
    for each in cards:
        if cards.count(each) == 3 and len(set(cards)) == 2:
            return True
    else:
        return False


# 6 张牌的情况：四带二
def is_four_two(cards):
    # 四带二分为带一对和带两张单牌
    for each in cards:
        if cards.count(each) == 4 and (len(set(cards)) == 2 or len(set(cards)) == 3):
            return True
    else:
        return False


# 5+ 张牌的情况：顺子
def is_continue(cards):
    # 注意：'2'和大小王不能参与
    length = len(cards)
    if 13 in cards or 14 in cards or 15 in cards or len(set(cards)) != length:
        return False
    else:
        for i in range(length-1):
            if cards[i] + 1 != cards[i+1]:
                return False
        else:
            return True


# 6+ 张牌的情况（必须为偶数）：双顺
def is_con_pair(cards):
    # 注意：'2'和大小王不能参与
    # 先判断是否两两成对，比如334455
    length = len(cards)
    cards.sort()
    for i in range(0, length-1, 2):
        if cards[i] != cards[i+1]:
            return False
    else:
        # 如果两两成对，去重后检测是否为顺子
        return is_continue(cards[::2])


# 6+ 张牌的情况（必须为三的倍数）：三顺
def is_aircraft(cards):
    # 注意：'2'和大小王不能参与
    # 先判断是否每三张牌均相同，比如333444
    length = len(cards)
    cards.sort()
    for i in range(0, length-2, 3):
        if (cards[i] != cards[i+1]) or (cards[i] != cards[i+2]) or (cards[i+1] != cards[i+2]):
            return False
    else:
        # 如果每三张牌均相同，去重后检测是否为顺子
        return is_continue(cards[::3])


# 8+ 张牌的情况：飞机带翅膀
def is_aircraft_wing(cards):
    # 注意：'2'和大小王不能参与
    # 先将飞机放到t1中
    # 再将翅膀放到t2中
    t1 = []
    t2 = []
    for each in cards:
        if cards.count(each) == 3:
            t1.append(each)
        else:
            t2.append(each)

    # 先判断飞机是否合法
    # 再判断剩余的牌是否与飞机配对
    if is_aircraft(t1) and len(t1) / 3 == len(set(t2)):
        return True
    else:
        return False


# 获取用户输入的扑克牌
def get_input():
    cards = input("请出牌（空格间隔，退出请输入Q）：")
    if cards == 'Q':
        return 0
    else:
        cards = cards.split() # "♠1 ♠2 ♠3 ♠4 ♠5" -> ['♠1', '♠2', '♠3', '♠4', '♠5']
        return cards


# 将扑克牌映射成代表权限的数字
def change_input(cards):
    result = []
    target = {'3':1, '4':2, '5':3, '6':4, '7':5, '8':6, '9':7, '10':8, 'J':9, 'Q':10, 'K':11, '1':12, '2':13}
    for each in cards:
        num = target.get(each[1:])
        if num:
            result.append(num)
        else:
            result.append(14 if each == '🌙' else 15)

    return result


# 检查组合是否符合出牌规则
def check(cards):
    # 检查2张牌的情况
    if len(cards) == 2:
        if is_pair(cards):
            print("符合规则：对牌")
        elif is_rocket(cards):
            print("符合规则：火箭")
        else:
            print("不符合规则！")
            
    # 检查3张牌的情况       
    elif len(cards) == 3:
        if is_three(cards):
            print("符合规则：三张牌相同")
        else:
            print("不符合规则！")
            
    # 检查4张牌的情况
    elif len(cards) == 4:
        if is_bomb(cards):
            print("符合规则：炸弹")
        elif is_three_one(cards):
            print("符合规则：三带一")
        else:
            print("不符合规则！")

    # 检查5+张牌的情况
    elif len(cards) >= 5:
        # 大于等于5张牌先检查是不是单顺，不是再检查其他情况
        if is_continue(cards):
            print("符合规则：单顺")
        else:
            # 检查5张牌的情况
            if len(cards) == 5:
                if is_three_two(cards):
                    print("符合规则：三带二")
                else:
                    print("不符合规则！")

            # 检查6张牌的情况
            if len(cards) == 6:
                if is_four_two(cards):
                    print("符合规则：四带二")
                elif is_con_pair(cards):
                    print("符合规则：双顺")
                elif is_aircraft(cards):
                    print("符合规则：三顺（飞机）")
                else:
                    print("不符合规则！")

            # 检查8+张牌的情况
            if len(cards) >= 8:
                if is_aircraft_wing(cards):
                    print("符合规则：飞机带翅膀")
                elif is_con_pair(cards):
                    print("符合规则：双顺")
                elif is_aircraft(cards):
                    print("符合规则：三顺（飞机）")
                else:
                    print("不符合规则！")


# 程序主流程
show_cards()
cards = get_input()
while cards:
    cards = change_input(cards)
    check(cards)
    cards = get_input()
