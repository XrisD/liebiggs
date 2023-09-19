def roboGeheHoch():
    global y
    led.unplot(x, y)
    y += -1
    if y < 0:
        y = 4
    led.plot(x, y)

def on_button_a():
    roboGeheLinks()
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    roboGeheRechts()
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

def on_pin_touch_p0():
    roboGeheHoch()
input.on_pin_touch_event(TouchPin.P0, input.button_event_down(), on_pin_touch_p0)

def roboGeheRechts():
    global x
    led.unplot(x, y)
    x += 1
    if x > 4:
        x = 0
    led.plot(x, y)
def roboGeheLinks():
    global x
    led.unplot(x, y)
    x += -1
    if x < 0:
        x = 4
    led.plot(x, y)

def on_pin_touch_p3():
    roboGeheRunter()
input.on_pin_touch_event(TouchPin.P3, input.button_event_down(), on_pin_touch_p3)

def roboGeheRunter():
    global y
    led.unplot(x, y)
    y += 1
    if y > 4:
        y = 0
    led.plot(x, y)
y = 0
x = 0
basic.clear_screen()
x = 2
y = 2
led.plot(x, y)

def on_forever():
    pass
basic.forever(on_forever)
