import get_final_game_state as fg

def get_all_examples():
    ex1 = example1()
    ex2 = example2()
    ex3 = example3()
    ex4 = example4()
    return [ex1, ex2, ex3, ex4]

def example1():
    board = fg.get_empty_board()
    fg.play_stone(board, (3,3), "B")
    fg.play_stone(board, (3,2), "W")
    fg.play_stone(board, (4,3), "W")
    fg.play_stone(board, (2,3), "W")
    fg.play_stone(board, (3,4), "W")
    return board

def example2():
    board = fg.get_empty_board()
    fg.play_stone(board, (3,3), "B")
    fg.play_stone(board, (3,4), "B")
    fg.play_stone(board, (3,2), "W")
    fg.play_stone(board, (4,3), "W")
    fg.play_stone(board, (2,3), "W")
    fg.play_stone(board, (3,5), "W")
    fg.play_stone(board, (2,4), "W")
    fg.play_stone(board, (4,4), "W")
    return board

def example3():
    board = fg.get_empty_board()
    fg.play_stone(board, (5,4), "B")
    fg.play_stone(board, (5,5), "B")
    fg.play_stone(board, (6,5), "B")
    fg.play_stone(board, (4,4), "W")
    fg.play_stone(board, (4,5), "W")
    fg.play_stone(board, (4,4), "W")
    fg.play_stone(board, (5,6), "W")
    fg.play_stone(board, (6,6), "W")
    fg.play_stone(board, (7,5), "W")
    fg.play_stone(board, (6,4), "W")
    fg.play_stone(board, (5,3), "W")
    return board

def example4():
    board = fg.get_empty_board()
    fg.play_stone(board, (4,4), "B")
    fg.play_stone(board, (5,3), "B")
    fg.play_stone(board, (5,5), "B")
    fg.play_stone(board, (6,4), "B")
    fg.play_stone(board, (6,3), "W")
    fg.play_stone(board, (7,4), "W")
    fg.play_stone(board, (6,5), "W")
    return board
