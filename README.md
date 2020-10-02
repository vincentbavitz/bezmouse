# BezMouse

BezMouse is a lightweight tool written in Python to simulate human-like mouse movements with [Bézier curves](https://en.wikipedia.org/wiki/B%C3%A9zier_curve).
Some applications might include:
  - aimbots (prevent bans)
  - MMORPG bots (avoid macro detection)
  - controlled macros

BezMouse was originally written for a RuneScape color bot and has never triggered macro detection in over 400 hours of continuous use.

## Noteworthy Functions
 **move_to_img** - this function takes the name of an input image (excluding file extension) and moves the mouse to a random pixel on that image if it is found on the screen. Commands for xdotool are saved to a temporary bash file in the ramdisk ./tmp called 'mouse.sh'. It is then executed as a bash script to give best performance.
**Note**: This function is very slow because it must identify the image across your screen. It is highly recommended to find the coordinates of the image in a separate thread and feed this into the move() function.

 **connected_bez** - connects all the (x, y) coordinates in a list of coordinates with a string of interconnected Bézier curves. A parameter *deviation* is required which controls how straight the lines drawn by the cursor are. Zero deviation gives straight lines.
Accuracy is a percentage of the displacement of the mouse from point A to B, which is given as maximum [Bézier control point](https://en.wikipedia.org/wiki/B%C3%A9zier_curve#Terminology) deviation. Naturally, deviation of 10 (10%) gives maximum control point deviation of 10% of magnitude of displacement of mouse from point A to B, and a minimum of 5% (deviation / 2).
Here is an example of *connected_bez* as a trace of the mouse as it passes 26 points in order, where *deviation* is set to 30.

![connected_bez_example](https://image.ibb.co/gcDXGk/example.png)

**move**
Each of the **move_*** functions are abstractions from the **move** function which handles the math of the Bézier curves such to produce realistic overshoots as well as variable speed and momentum. The following graphic was made using the **draw = True** argument and demonstrates the overshoot and variable speed.
![overshoot_example](https://image.ibb.co/ie8M95/example_2_overshoot.png)


## Dependencies
  - [Linux](https://en.wikipedia.org/wiki/Linux) (generates bash scripts)
  - [Python >=3](https://python.org/downloads)
  - [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/)
  - [xdotool](https://github.com/jordansissel/xdotool)
  - [more_itertools](https://more-itertools.readthedocs.io/en/latest/)
  - [maim](https://github.com/naelstrof/maim)

## Instructions
```
git clone https://github.com/xvol/bezmouse.git
```

## Development
Find something wrong with my code? See room for improvement? Please let me know!
### Regarding Performance
I am looking into injecting mouse events directly into a uinput virtual mouse. This has the benefits of:
  - minimising latency
  - giving OS-level control over mouse acceleration
  - generating perfectly smooth, coordinate independent movements
  - eliminating heavy dependencies

I will implement this feature if I can find an equivalent to uinput for Windows.

### Todos

 - Make available for Windows / OSX
 - Improve performance
 - Remove dependency [PyAutoGui](https://pyautogui.readthedocs.io/en/latest/) in favour of just [xdotool](https://github.com/jordansissel/xdotool).
 
