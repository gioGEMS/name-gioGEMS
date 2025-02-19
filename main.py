def on_forever():
    basic.show_leds("""
        . . . # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # . . .
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # . .
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # .
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # #
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . .
        # . . . #
        . # # # #
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . . #
        # . . . #
        . # # # #
        """)
    basic.show_leds("""
        . # # # .
        # . . . .
        # . . # #
        # . . . #
        . # # # #
        """)
    basic.pause(100)
    basic.clear_screen()
    music.set_volume(15)
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("gioGEMS")
basic.forever(on_forever)
