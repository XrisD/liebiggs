function roboGeheHoch () {
    led.unplot(x, y)
    y += -1
    if (y < 0) {
        y = 4
    }
    led.plot(x, y)
}
input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    roboGeheLinks()
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    roboGeheRechts()
})
input.onPinTouchEvent(TouchPin.P0, input.buttonEventDown(), function () {
    roboGeheHoch()
})
function roboGeheRechts () {
    led.unplot(x, y)
    x += 1
    if (x > 4) {
        x = 0
    }
    led.plot(x, y)
}
function roboGeheLinks () {
    led.unplot(x, y)
    x += -1
    if (x < 0) {
        x = 4
    }
    led.plot(x, y)
}
input.onPinTouchEvent(TouchPin.P3, input.buttonEventDown(), function () {
    roboGeheRunter()
})
function roboGeheRunter () {
    led.unplot(x, y)
    y += 1
    if (y > 4) {
        y = 0
    }
    led.plot(x, y)
}
let y = 0
let x = 0
basic.clearScreen()
x = 2
y = 2
led.plot(x, y)
basic.forever(function () {
	
})
