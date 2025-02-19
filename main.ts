basic.forever(function on_forever() {
    basic.showLeds(`
        . . . # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . . . . .
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # . . .
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # . .
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # .
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . .
        . # # # #
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . .
        # . . . #
        . # # # #
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . . #
        # . . . #
        . # # # #
        `)
    basic.showLeds(`
        . # # # .
        # . . . .
        # . . # #
        # . . . #
        . # # # #
        `)
    basic.pause(100)
    basic.clearScreen()
    music.setVolume(15)
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
    basic.showString("gioGEMS")
})
