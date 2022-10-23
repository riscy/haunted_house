"""You are outside a strange house."""
import random


def do_look():
    """Look around."""
    return (
        'You spot a key in the dust.',
        'scene_entrance_with_key',
    )


def do_enter():
    """Enter the house."""
    description = random.choice(
        [
            "You try the door, but it's locked.",
            "As you approach, you hear the door being locked.",
        ]
    )
    return (description, 'scene_entrance')
