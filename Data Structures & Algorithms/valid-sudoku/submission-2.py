class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols, rows, boxes = [], [], []

        for i in range(9):
            cols.append(set())
            rows.append(set())
            boxes.append(set())

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)

                if val in cols[j]:
                    return False
                else:
                    cols[j].add(val)

                box_index = (i // 3) * 3 + (j // 3)

                if val in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].add(val)

        return True