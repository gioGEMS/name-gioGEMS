basic.forever(function on_forever() {
    basic.showString("gioGEMS")
    music.play(music.stringPlayable("C C5 C E C A C G ", 220), music.PlaybackMode.LoopingInBackground)
    music.setVolume(10)
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
})
