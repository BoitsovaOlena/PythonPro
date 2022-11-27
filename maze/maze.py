"""
Дан лабіринт (Матрица NxM) дана точка входу до лабиринту. Стіна - # коридор - . Наприклад:

##########
.........#
######.###
#......###
#.####.###
#........#
##.#######
##.##.####
##......##
#######.##

enter = [1,0]
exit = ???
Зробити програму, яка буде шукати вихід з лабіринту, печатає його координати.
Майте на увазі що я буду підставляти свої лабіринти цей - ЛИШЕ ПРИКЛАД.
"""


class IsPoint:
    """
    The class is used to create objects that can only be a list of two ints.
    """
    @classmethod
    def verify_item(cls, item):
        if type(item) != list:
            raise TypeError('Value must be list')
        if len(item) != 2:
            raise ValueError('Value must be list of two ints')
        if type(item[0]) != int or type(item[1]) != int:
            raise TypeError('Value must be list of two ints')

    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_item(value)
        setattr(instance, self.name, value)

class IsListOfLists:
    """
    The class is used to create objects that can only be a list of lists.
    """
    @classmethod
    def verify_item(cls, my_list):
        if not isinstance(my_list, list):
            raise TypeError
        for item in my_list:
            if not isinstance(item, list):
                raise TypeError

    def __set_name__(self, owner, name: str):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_item(value)
        setattr(instance, self.name, value)


class Maze:
    matrix = IsListOfLists()
    enter = IsPoint()
    exit = IsPoint()
    vizited_list = IsListOfLists()

    def __init__(self, matrix, enter):
        self.matrix = matrix
        self.enter = enter
        self.vizited_list = [enter]

    def add_vizited(self, point: list) -> None:
        for item in self.vizited_list:
            if item[0] == point[0] and item[1] == point[1]:
                return
        self.vizited_list.append(point)

    def vizited(self, point: list):
        for item in self.vizited_list:
            if item[0] == point[0] and item[1] == point[1]:
                return True
        return False

    def go_right(self, start_row, start_col):
        """
        Searches for an exit from left to right.
        :return:
        :rtype: None
        """
        index = 0
        row = self.matrix[start_row]
        row_up = self.matrix[start_row - 1] if start_row != 0 else None
        row_down = self.matrix[start_row + 1] if start_row < len(self.matrix) - 1 else None
        for column in row[start_col:]:
            self.add_vizited([start_row, (index + start_col)])
            conditions = (
                start_col == index == 0,
                index == len(row[start_col:]) - 1,
                start_row == 0,
                start_row == len(self.matrix) - 1
            )
            if column == '.' and ((index + start_col) != self.enter[1] or start_row != self.enter[0]) and any(conditions):
                self.exit = [start_row, (index + start_col)]
                return

            is_visited_rigth = self.vizited([start_row, index + start_col + 1])
            is_visited_left = self.vizited([start_row, index + start_col - 1])
            is_visited_up = self.vizited([start_row - 1, index + start_col])

            if row_up and row_up[index + start_col] == '.':
                if is_visited_up and row[index + start_col + 1] == '.' and is_visited_rigth is False:
                    index += 1
                    continue
                if is_visited_up and row[index + start_col - 1] == '.' and is_visited_left is False:
                    self.go_left(start_row, index + start_col)
                    return
                self.go_right(start_row - 1, index + start_col)
                return
            elif row[index + start_col + 1] == '.':
                if is_visited_rigth and row[index + start_col - 1] == '.' and is_visited_left is False:
                    self.go_left(start_row, index + start_col - 1)
                    return
                if is_visited_rigth and row_up and row_up[index + start_col] == '.' and is_visited_up is False:
                    self.go_right(start_row - 1, index + start_col)
                    return
                index += 1
                continue
            else:
                self.go_left(start_row, index + start_col)
                return

    def go_left(self, start_row, start_col):
        """
        Searches for an exit from right to left .
        :return:
        :rtype: None
        """
        index = start_col
        row = self.matrix[start_row]
        row_up = self.matrix[start_row - 1] if start_row != 0 else None
        row_down = self.matrix[start_row + 1] if start_row < len(self.matrix) - 1 else None
        while index > -1:
            self.add_vizited([start_row, index])
            column = row[:start_col+1][index]
            conditions = (
                index == 0,
                index == start_col == len(row[:start_col]) - 1,
                start_row == 0,
                start_row == len(self.matrix) - 1
            )
            if column == '.' and (index != self.enter[1] or start_row != self.enter[0]) and any(conditions):
                self.exit = [start_row, index]
                return
            is_visited_rigth = self.vizited([start_row, index + 1])
            is_visited_left = self.vizited([start_row, index - 1])
            is_visited_down = self.vizited([start_row + 1, index])

            if row_down and row_down[index] == '.':
                if is_visited_down and row[index - 1] == '.' and is_visited_left is False:
                    index -= 1
                    continue
                if is_visited_down and row[index + 1] == '.' and is_visited_rigth is False:
                    self.go_right(start_row, index)
                    return
                self.go_left(start_row + 1, index)
                return
            elif row[index - 1] == '.':
                if is_visited_left and row[index + 1] == '.' and is_visited_rigth is False:
                    self.go_right(start_row, index)
                    return
                if is_visited_left and row_down and row_down[index] == '.' and is_visited_down is False:
                    print('if 4 3')
                    self.go_left(start_row + 1, index)
                    return
                index -= 1
                continue
            else:
                self.go_right(start_row, index)
                return

    def find_exit(self):
        """

        :return:
        :rtype: None
        """
        self.go_right(self.enter[0], self.enter[1])


