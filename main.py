def on_forever():
    music.set_volume(15)
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_string("gioGEMS")
basic.forever(on_forever)
