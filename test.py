import script
import linkedlist

def node_tests():
    print("Testing class Node")
    # Testing constructor
    init_node = linkedlist.Node(1)
    assert init_node.val == 1, "value should be 1"
    assert init_node.next == None, "next should be None"

    # Testing set_next
    next_node = linkedlist.Node(2)
    init_node.set_next(next_node)
    assert init_node.next == next_node, "next should be next_node"

    # Testing get_next
    assert init_node.get_next() == next_node, "get_next should return next_node"

    # Testing set_val
    next_node.set_val(3)
    assert next_node.val == 3, "value should be set to 3"

    # Testing get_val
    assert next_node.get_val() == 3, "get_val should return 3"

    # Testing has_next
    assert init_node.has_next() == True, "init_node should have a succesor"
    assert next_node.has_next() == False, "next_node should not have a succesor"

    print("This module has passed its tests")

def linkedlist_tests():
    print("Testing class LinkedList")
    # Testing constructor
    init_list = linkedlist.LinkedList()
    assert init_list.root == None
    assert init_list.size == 0

    # Testing get_size(self)
    assert init_list.get_size() == 0



    print("This module has passed its tests")

def piece_tests():
    print("Testing class Piece")
    # Testing constructor
    init_piece = script.Piece(0,0)
    assert init_piece.x == 0, "x coordinate should be 0"
    assert init_piece.y == 0, "y coordinate should be 0"

    # Testing to_string
    assert init_piece.to_str() == "[(0,0)]", "string representation incorrect"

    print("This module has passed its tests")

def snake_tests():
    print("Testing class Snake")
    # Testing constructor
    init_snake = script.Snake(4,400,400)
    assert init_snake.root.get_val().x == 400, "x coordinate should be 0"
    assert init_snake.root.get_val().y == 400, "y cooridnate should be 0"
    assert init_snake.length == 4, "length should be 4"


    # Testing move
    #moved_snake = script.Snake(4,400,400)
    #moved_snake.build()
    #moved_snake.move()
    #assert moved_snake.x == (400 + moved_snake.pieces[0].vel), "snake hasn't moved properly"

    print("This module has passed its tests")

def main():
    node_tests()
    linkedlist_tests()
    piece_tests()
    snake_tests()
    print("All tests passed!")


if __name__ == "__main__":
    main()
