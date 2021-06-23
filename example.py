import switchadapt as sa

# This function is what you want to happen when a blink happens
def onBlink():
    print('hola')

# When the blink ends, this will run
def reset():
    print('Guten tag')

# Instantiating switch class
switch = sa.EyeSwitch(onBlink, reset)
# Run the switch (no code below this function will run until this function ends)
switch.run()
