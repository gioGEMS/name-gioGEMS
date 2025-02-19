def on_forever():
    basic.show_string("gioGEMS")
    music.play(music.string_playable("C C5 C E C A C G ", 220),
        music.PlaybackMode.LOOPING_IN_BACKGROUND)
    music.set_volume(10)
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
