def __colored(color: int, text: str) -> str:
    """ A decorator to color the text
    Args:
        color (int): 24 bits color code such as 0xffffff
        text (str): Text to color
    Returns:
        str: Colored Text
    Reference:
        https://www.codegrepper.com/code-examples/python/python+change+all+console+color
    """
    r, g, b = (color & 0xff0000) >> 16, (color & 0x00ff00) >> 8, color & 0x0000ff
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)


def __draw_level(width: int, img_width: int):
    """ Draw one level (4 lines leaves) of christmas tree.
    Args:
        width (int): Initial width of a level.
            This variable will grow and print each line of the level.
        img_width (int): Max width we can draw christmas tree.
            The christmas tree will align in the middle of the img_width.
    Returns:
        None: The result will print to standard output directly.
    """
    assert width % 2
    colors = [0x0b774f, 0x089945, 0x05bb3a, 0x02dd30]  # Color of each line of leaves in the level
    for grow, color in zip(range(0, 8, 2), colors):
        width += grow
        text = (width * '*').center(img_width)
        print(__colored(color, text))


def __draw_trunk(width: int, img_width: int):
    """ Draw trunk of christmas tree.
    Args:
        width (int): Trunk width. Trunk height is ceil(width/2)
        img_width (int): Max width we can draw christmas tree.
            The christmas tree will align in the middle of the img_width.
    Returns:
        None: The result will print to standard output directly.
    """
    assert width % 2
    color = 0x99582a
    for height in range((width + 1) // 2):
        text = (width * '#').center(img_width)
        print(__colored(color, text))


def draw_christmas_tree(level: int):
    """ Draw ASCII art Christmas tree with specific level.
    Args:
        level (int): Level of tree. Each level have four lines of leaves.
    Returns:
        None: The result will print to standard output directly.
    """
    img_width = 6 * level + 7
    for initial_width in range(1, 6 * level + 1, 6):
        __draw_level(initial_width, img_width)
    __draw_trunk(5 + level // 2 * 2, img_width)  # '// 2 * 2' to keep trunk width odd


if __name__ == '__main__':
    # show different size christmas tree
    for size in range(1, 10):
        draw_christmas_tree(size)