"""You are outside a strange house."""


def do_enter():
    """Enter the house."""
    return ("You try the key on the door.  It fits...", 'scene_inside')


def do_look():
    """Look around."""
    return ("You don't see anything unusual.", 'scene_entrance_with_key')
