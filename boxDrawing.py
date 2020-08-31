#MenuTitle: boxDrawing

import math
from boxDrawingRecipes import recipes

__doc__ = '''

This script will draw the Unicode ranges "Box Drawing Characters" (U+2500 to
U+257F) and "Block Elements" (U+2580 to U+259F). It makes use of the FontParts
Python library (https://github.com/robotools/fontParts).
The script was successfully tested in RoboFont, Glyphs and on the command line.
It is possible to run this script straight from the command line, given that
the FontParts Python module is installed. The drawing itself is done using
combinations of simple drawing instructions; listed in the external
boxDrawingRecipes.py module.

'''

# ----------------------------------------------------------------
# Edit these values if you want (currently set to match Source Code Pro):
WIDTH = 600                 # Glyph width.
HEIGHT = 1400               # Height for line elements, including overlap.
MEDIAN = 300                # Median line.
STROKE = 160                # General stroke weight.
FAT = 2                     # Multiplication factor for drawing 'fat' strokes.
RADIUS = WIDTH / 2          # Radius for arc elements.
BLOCK_HEIGHT = 1400         # Height for block elements.
EM_HEIGHT = 1200            # Height for elements that don't connect
                            # vertically, such as dashed strokes.
FAT_STROKE = STROKE * FAT   # STROKE thickness for 'fat' lines.
BUTT = STROKE               # Horizontal overlap.


# Bezier point distance for drawing circles.
KAPPA = 4 * (math.sqrt(2) - 1) / 3


# These values are for block elements,
# and are dependent of the values above:
BLOCK_ORIGIN = (0, MEDIAN - BLOCK_HEIGHT / 2)
BLOCK_TOP = (WIDTH, MEDIAN + BLOCK_HEIGHT / 2)


# Nothing below here _needs_ to be edited, but feel free to do so:
# ----------------------------------------------------------------

# Checking which application we are in:

IN_RF = False
IN_FL = False
IN_GLYPHS = False
IN_SHELL = False

if not any((IN_RF, IN_FL, IN_GLYPHS)):
    try:
        import mojo.roboFont
        IN_RF = True
    except ImportError:
        pass

if not any((IN_RF, IN_FL, IN_GLYPHS)):
    try:
        import GlyphsApp
        IN_GLYPHS = True
    except ImportError:
        pass

if not any((IN_RF, IN_FL, IN_GLYPHS)):
    try:
        import flsys
        IN_FL = True
    except ImportError:
        pass

if not any((IN_RF, IN_FL, IN_GLYPHS)):
    IN_SHELL = True
    import os
    import time
    from fontParts.fontshell import RFont


if IN_GLYPHS:
    try:
        import GSPen
        from objectsGS import CurrentFont
    except ImportError:
        print(
            'The files GSPen.py and objectsGS.py are needed for '
            'Robofab to work in Glyphs. Please get them at '
            'https://github.com/schriftgestalt/Glyphs-Scripts')
    try:
        test = getattr(GSLayer, "removeOverlap")
        if not callable(test):
            raise
    except:
        raise AttributeError(
            'Please update your objectsGS.py file. '
            'Download the latest verion at: '
            'https://github.com/schriftgestalt/Glyphs-Scripts')


# Check if a font is open -- if not, create a new one.
if IN_SHELL:
    f = RFont()
else:
    f = CurrentFont()

if f is None:
    f = RFont()

if f is not None and IN_GLYPHS:
    Font.disableUpdateInterface()


def roundInt(float):
    return int(round(float))


def floatRange(x, y, step):
    '''
    Variation on range(), since step values for dashed lines may be floats.
    '''
    while x < y:
        yield x
        x += step


def drawRect(pen, BL, BR, TR, TL):
    '''
    General drawing function for a rectangle.
    '''

    pen.moveTo(BL)
    pen.lineTo(BR)
    pen.lineTo(TR)
    pen.lineTo(TL)
    pen.closePath()


def drawPoly(pen, *coords):
    '''
    General drawing function for a polygon.
    '''

    if len(set(coords)) >= 3:
        pen.moveTo(coords[0])
        for pointIndex, pointCoords in enumerate(coords):
            # print pointCoords
            if pointIndex > 0:
                if not pointCoords == coords[pointIndex - 1]:
                    pen.lineTo(pointCoords)
        pen.closePath()


def drawArc(
    pen, start1, start2, end1, end2,
    IAstart, IApoint1, IApoint2, IAend,
    OAstart, OApoint1, OApoint2, OAend
):
    '''
    General drawing function for an arc.
    '''

    pen.moveTo(start1)
    pen.lineTo(start2)
    pen.lineTo(IAstart)
    pen.curveTo(IApoint1, IApoint2, IAend)
    pen.lineTo(end1)
    pen.lineTo(end2)
    pen.lineTo(OAstart)
    pen.curveTo(OApoint1, OApoint2, OAend)

    pen.closePath()


def horLine(pen, start, end, stroke, buttL=BUTT, buttR=BUTT):
    '''
    General drawing function for a horizontal line.
    '''

    startX = start[0]
    startY = start[1]
    endX = end[0]
    endY = end[1]

    BL = (startX - buttL / 2, endY - stroke / 2)
    BR = (endX + buttR / 2, endY - stroke / 2)
    TR = (endX + buttR / 2, endY + stroke / 2)
    TL = (startX - buttL / 2, startY + stroke / 2)

    drawRect(pen, BL, BR, TR, TL)


def vertLine(pen, start, end, stroke, buttB=0, buttT=0):
    '''
    General drawing function for a vertical line.
    '''

    startX = start[0]
    startY = start[1]
    endY = end[1]

    BL = (startX - stroke / 2, startY - buttB / 2)
    BR = (startX + stroke / 2, startY - buttB / 2)
    TR = (startX + stroke / 2, endY + buttT / 2)
    TL = (startX - stroke / 2, endY + buttT / 2)

    drawRect(pen, BL, BR, TR, TL)


def box(pen, start=BLOCK_ORIGIN, end=BLOCK_TOP):
    '''
    A box.
    '''

    startX = start[0]
    startY = start[1]
    endX = end[0]
    endY = end[1]

    BL = (startX, startY)
    BR = (endX, startY)
    TR = (endX, endY)
    TL = (startX, endY)

    drawRect(pen, BL, BR, TR, TL)


def dashedHorLine(pen, step, width=WIDTH, stroke=STROKE):
    '''
    Dashed horizontal bar.
    '''

    stepLength = width / step
    gap = stepLength / step
    for w in floatRange(0, width, stepLength):
        if w + stepLength - gap < width:
            w = w + gap / 2  # centering the dashed line in the glyph
            horLine(
                boxPen,
                (w, MEDIAN),
                (w + stepLength - gap, MEDIAN),
                stroke,
                buttL=0,
                buttR=0
            )


def dashedVertLine(pen, step, length=EM_HEIGHT, stroke=STROKE):
    '''
    Dashed vertical bar.
    '''

    stepLength = length / step
    gap = stepLength / step
    top = MEDIAN + EM_HEIGHT / 2

    for h in floatRange(MEDIAN - length / 2, MEDIAN + length / 2, stepLength):
        if h + stepLength - gap < top:
            h += gap / 2
            vertLine(
                boxPen,
                (WIDTH / 2, h),
                (WIDTH / 2, h + stepLength - gap),
                stroke
            )


def dot(pen, center, radius):
    '''
    A dot.
    '''
    x, y = center

    pen.moveTo(
        (x - radius, y)
    )
    pen.curveTo(
        (x - radius, y - radius * KAPPA),
        (x - radius * KAPPA, y - radius),
        (x, y - radius)
    )
    pen.curveTo(
        (x + radius * KAPPA, y - radius),
        (x + radius, y - radius * KAPPA),
        (x + radius, y)
    )
    pen.curveTo(
        (x + radius, y + radius * KAPPA),
        (x + radius * KAPPA, y + radius),
        (x, y + radius)
    )
    pen.curveTo(
        (x - radius * KAPPA, y + radius),
        (x - radius, y + radius * KAPPA),
        (x - radius, y)
    )
    pen.closePath()


def polkaShade(pen, shade):
    '''
    Shading patterns, consisting of polka dots.
    Not used in any of the drawing recipes, but perhaps useful for somebody.
    '''

    vstep = 100
    hstep = 200
    if shade == '25':
        radius = 24
    if shade == '50':
        radius = 36
    if shade == '75':
        radius = 54

    for w in range(0, WIDTH, hstep):
        for h in range(
            roundInt(MEDIAN - BLOCK_HEIGHT / 2),
            roundInt(MEDIAN + BLOCK_HEIGHT / 2),
            vstep * 2
        ):
            dot(
                boxPen,
                (w, h),
                radius
            )
            dot(
                boxPen,
                (w + hstep / 2, h + vstep),
                radius * 1.5
            )


def shade(pen, shade):
    '''
    Shading patterns, consisting of little boxes.
    Not used in any of the drawing recipes, but maybe useful for somebody.
    Reliable way to crash makeOTF (in 2016).
    '''

    vstep = 50
    hstep = 100
    if shade == '25':
        boxWidth = 20
        boxHeight = 30
    if shade == '50':
        boxWidth = 40
        boxHeight = 50
    if shade == '75':
        boxWidth = 45
        boxHeight = 70

    for w in range(0, WIDTH, hstep):
        for h in range(
            MEDIAN - BLOCK_HEIGHT / 2,
            MEDIAN + BLOCK_HEIGHT / 2,
            vstep * 2
        ):
            box(
                boxPen,
                (w, h),
                (w + boxWidth, h + boxHeight)
            )
            box(
                boxPen,
                (w + hstep / 2, h + vstep),
                (w + boxWidth + hstep / 2, h + boxHeight + vstep)
            )


def stripedShade(pen, shade):
    '''
    Shading patterns, consisting of diagonal lines.

    This function assumes a bunch of right triangles being moved across
    the width of the glyph. The law of sines is used for start- and end
    point calculations.
    '''

    if shade == '25':
        step = WIDTH / 3
    if shade == '50':
        step = WIDTH / 6
    if shade == '75':
        step = WIDTH / 12

    stroke = WIDTH / 30
    # angle = math.asin(2 / math.hypot(1, 2))  # 1 : 2 ratio
    angle = math.radians(45)  # 1 : 1 ratio

    yShift = MEDIAN - BLOCK_HEIGHT / 2
    hypotenuse = BLOCK_HEIGHT / math.sin(angle)

    # leftmost point:
    leftmost_x = 0 - math.cos(angle) * hypotenuse - stroke
    xValues = []

    for xValue in floatRange(leftmost_x, WIDTH + stroke, step):
        xValues.append(xValue)
        xValues.append(xValue + stroke)

    drawList = []

    for (raw_x1, raw_x2) in zip(xValues[:-1:2], xValues[1::2]):
        bot_x1 = roundInt(raw_x1)
        bot_x2 = roundInt(raw_x2)
        top_x1 = roundInt(raw_x1 + hypotenuse * math.cos(angle))
        top_x2 = roundInt(raw_x2 + hypotenuse * math.cos(angle))

        bot_y1 = 0
        bot_y2 = 0
        top_y1 = BLOCK_HEIGHT
        top_y2 = BLOCK_HEIGHT

        if bot_x1 <= 0:
            bot_x1 = 0
            bot_y1 = roundInt(math.tan(angle) * abs(raw_x1))

        if bot_x2 <= 0:
            bot_x2 = 0
            bot_y2 = roundInt(math.tan(angle) * abs(raw_x2))

        if top_x1 >= WIDTH:
            top_x1 = WIDTH
            top_y1 = roundInt(math.tan(angle) * abs(raw_x1 - WIDTH))

        if top_x2 >= WIDTH:
            top_x2 = WIDTH
            top_y2 = roundInt(math.tan(angle) * abs(raw_x2 - WIDTH))

        if top_y1 <= bot_y1:
            top_y1 = bot_y1 = BLOCK_HEIGHT

        if top_x1 <= bot_x1:
            top_x1 = bot_x1 = WIDTH

        if bot_x2 >= WIDTH:
            bot_x2 = WIDTH
            top_y2 = 0

        stripe = (
            (bot_x1, bot_y1),
            (bot_x2, bot_y2),
            (top_x2, top_y2),
            (top_x1, top_y1),
        )

        drawList.append(shiftCoords(stripe, 0, yShift))

    for (BL, BR, TR, TL) in drawList:
        drawPoly(pen, BL, BR, TR, TL)


def verticalShade(pen, shade):
    '''
    Boring shading patterns, consisting of vertical lines.
    '''

    if shade == '25':
        step = WIDTH / 3
    if shade == '50':
        step = WIDTH / 6
    if shade == '75':
        step = WIDTH / 12

    stroke = WIDTH / 30

    for xValue in floatRange(0, WIDTH, step):
        y_bot = MEDIAN - HEIGHT / 2
        y_top = y_bot + HEIGHT
        x_left = xValue
        x_rght = xValue + stroke

        drawRect(
            pen,
            (x_left, y_bot),
            (x_rght, y_bot),
            (x_rght, y_top),
            (x_left, y_top)
        )


def diagonal(pen, start, end, direction):
    '''
    Diagonal line in two possible directions; either bottomUp or topDown.
    '''

    diagonalLength = math.hypot(WIDTH, EM_HEIGHT)
    angle1 = math.asin(WIDTH / diagonalLength)
    angle2 = math.pi / 2 - angle1
    xDist = STROKE / 2 / math.cos(angle1)
    yDist = STROKE / 2 / math.cos(angle2)

    startX = start[0]
    startY = start[1]
    endX = end[0]
    endY = end[1]

    TL1 = (startX + xDist, startY)
    TL2 = (startX, startY)
    TL3 = (startX, startY - yDist)
    BR1 = (endX - xDist, endY)
    BR2 = (endX, endY)
    BR3 = (endX, endY + yDist)

    BL1 = (startX, startY + yDist)
    BL2 = (startX, startY)
    BL3 = (startX + xDist, startY)
    TR1 = (endX, endY - yDist)
    TR2 = (endX, endY)
    TR3 = (endX - xDist, endY)

    if direction == 'topDown':
        pen.moveTo(TL1)
        pen.lineTo(TL2)
        pen.lineTo(TL3)
        pen.lineTo(BR1)
        pen.lineTo(BR2)
        pen.lineTo(BR3)
        pen.closePath()

    if direction == 'bottomUp':
        pen.moveTo(BL1)
        pen.lineTo(BL2)
        pen.lineTo(BL3)
        pen.lineTo(TR1)
        pen.lineTo(TR2)
        pen.lineTo(TR3)
        pen.closePath()


def arc(pen, start, end, side, stroke, radius, butt=0):
    '''
    Rounded corner.
    '''

    if side == 'TL':
        yflip = 1
        xflip = 1
    if side == 'BL':
        yflip = -1
        xflip = 1
    if side == 'TR':
        yflip = 1
        xflip = -1
    if side == 'BR':
        yflip = -1
        xflip = -1

    startX = start[0]
    startY = start[1]
    endX = end[0]
    endY = end[1]

    cStartX = startX
    cStartY = endY - (radius * yflip)
    cEndX = startX + (radius * xflip)
    cEndY = endY

    start1 = (startX - (stroke / 2 * xflip), startY)
    start2 = (startX + (stroke / 2 * xflip), startY)
    end1 = (endX + (butt / 2 * xflip), endY - (stroke / 2 * yflip))
    end2 = (endX + (butt / 2 * xflip), endY + (stroke / 2 * yflip))

    IAstart = (cStartX + (stroke / 2 * xflip), cStartY)

    IApoint1 = (
        cStartX + (stroke / 2 * xflip),
        cStartY + ((radius - stroke / 2) * KAPPA * yflip)
    )
    IApoint2 = (
        cEndX - ((radius - stroke / 2) * KAPPA * xflip),
        cEndY - (stroke / 2 * yflip)
    )
    IAend = (cEndX, cEndY - (stroke / 2 * yflip))

    OAstart = (cEndX, cEndY + (stroke / 2 * yflip))

    OApoint1 = (
        cEndX - ((radius + stroke / 2) * KAPPA * xflip),
        cEndY + (stroke / 2 * yflip)
    )
    OApoint2 = (
        cStartX - (stroke / 2 * xflip),
        cStartY + ((radius + stroke / 2) * KAPPA * yflip)
    )
    OAend = (cStartX - (stroke / 2 * xflip), cStartY)

    drawArc(
        pen,
        start1, start2,
        end1, end2,
        IAstart,
        IApoint1, IApoint2,
        IAend,
        OAstart,
        OApoint1, OApoint2,
        OAend
    )


def horBar(fatness=1, median=MEDIAN, buttL=BUTT, buttR=BUTT):
    '''
    Horizontal bar.
    '''

    horLine(
        boxPen,
        (0, median),
        (WIDTH, median),
        STROKE * fatness,
        buttL, buttR
    )


def vertBar(fatness=1, buttB=0, buttT=0):
    '''
    Vertical bar.
    '''

    vertLine(
        boxPen,
        (WIDTH / 2, MEDIAN - HEIGHT / 2),
        (WIDTH / 2, MEDIAN + HEIGHT / 2),
        STROKE * fatness,
        buttB, buttT
    )


def horHalfBar(side, fatness=1, median=MEDIAN, buttL=BUTT, buttR=BUTT):
    '''
    Halfwidth horizontal bar, left or right.
    '''

    if side == 'left':
        if buttR == BUTT != STROKE:
            buttR = 0
        horLine(
            boxPen,
            (0, median),
            (WIDTH / 2, median),
            STROKE * fatness,
            buttL, buttR
        )
    elif side == 'right':
        if buttL == BUTT != STROKE:
            buttL = 0
        horLine(
            boxPen,
            (WIDTH / 2, median),
            (WIDTH, median),
            STROKE * fatness,
            buttL, buttR
        )


def vertHalfBar(fold, fatness=1, buttB=0, buttT=0):
    '''
    Half-height vertical bar, top or bottom.
    '''

    if fold == 'top':
        vertLine(
            boxPen,
            (WIDTH / 2, MEDIAN),
            (WIDTH / 2, MEDIAN + HEIGHT / 2),
            STROKE * fatness,
            buttB, buttT
        )
    if fold == 'bottom':
        vertLine(
            boxPen,
            (WIDTH / 2, MEDIAN - HEIGHT / 2),
            (WIDTH / 2, MEDIAN),
            STROKE * fatness,
            buttB, buttT
        )


def horSplitBar(fatness=1, buttL=BUTT, buttR=BUTT):
    '''
    Double-stroked horizontal bar, left or right.
    '''

    topMedian = MEDIAN + STROKE * fatness
    bottomMedian = MEDIAN - STROKE * fatness

    horBar(fatness, topMedian, buttL, buttR)
    horBar(fatness, bottomMedian, buttL, buttR)


def vertSplitBar(fatness=1, buttB=0, buttT=0):
    '''
    Double-stroked vertical bar, top or bottom.
    '''

    leftX = WIDTH / 2 - (STROKE * fatness)
    rightX = WIDTH / 2 + (STROKE * fatness)
    vertLine(
        boxPen,
        (leftX, MEDIAN - HEIGHT / 2),
        (leftX, MEDIAN + HEIGHT / 2),
        STROKE * fatness,
        buttB, buttT
    )
    vertLine(
        boxPen,
        (rightX, MEDIAN - HEIGHT / 2),
        (rightX, MEDIAN + HEIGHT / 2),
        STROKE * fatness,
        buttB, buttT
    )


def horSplitHalfBar(side, fatness=1, buttL=BUTT, buttR=BUTT):
    '''
    Double-stroked halfwidth horizontal bar, left or right.
    '''

    topMedian = MEDIAN + STROKE * fatness
    bottomMedian = MEDIAN - STROKE * fatness

    horHalfBar(side, fatness, topMedian, buttL, buttR)
    horHalfBar(side, fatness, bottomMedian, buttL, buttR)


def vertSplitHalfBar(fold, fatness=1, buttB=0, buttT=0):
    '''
    Double-stroked half-height vertical bar, top or bottom.
    '''

    leftX = WIDTH / 2 - STROKE * fatness
    rightX = WIDTH / 2 + STROKE * fatness

    if fold == 'top':
        vertLine(
            boxPen,
            (leftX, MEDIAN),
            (leftX, MEDIAN + HEIGHT / 2),
            STROKE * fatness,
            buttB, buttT
        )
        vertLine(
            boxPen,
            (rightX, MEDIAN),
            (rightX, MEDIAN + HEIGHT / 2),
            STROKE * fatness,
            buttB, buttT
        )
    if fold == 'bottom':
        vertLine(
            boxPen,
            (leftX, MEDIAN - HEIGHT / 2),
            (leftX, MEDIAN),
            STROKE * fatness,
            buttB, buttT
        )
        vertLine(
            boxPen,
            (rightX, MEDIAN - HEIGHT / 2),
            (rightX, MEDIAN),
            STROKE * fatness,
            buttB, buttT
        )


def outerCorner(side, fold, fatness=1, cornerMedian=MEDIAN):
    '''
    Outer part of a double-stroked corner.
    '''

    if fold == 'top':
        cornerMedian -= STROKE * fatness
    if fold == 'bottom':
        cornerMedian += STROKE * fatness

    if side == 'right':
        horHalfBar(
            side,
            median=cornerMedian,
            buttL=3 * STROKE,
            buttR=BUTT
        )
        x = WIDTH / 2 - STROKE * fatness

    if side == 'left':
        horHalfBar(
            side,
            median=cornerMedian,
            buttL=BUTT,
            buttR=3 * STROKE
        )
        x = WIDTH / 2 + STROKE * fatness

    if fold == 'top':
        cornerMedian += STROKE * fatness
        vertLine(
            boxPen,
            (x, cornerMedian),
            (x, cornerMedian + HEIGHT / 2),
            STROKE * fatness,
            buttB=3 * STROKE
        )

    if fold == 'bottom':
        cornerMedian -= STROKE * fatness
        vertLine(
            boxPen,
            (x, cornerMedian - HEIGHT / 2),
            (x, cornerMedian),
            STROKE * fatness,
            buttT=3 * STROKE
        )


def innerCorner(side, fold, fatness=1, cornerMedian=MEDIAN):
    '''
    Inner part of a double-stroked corner.
    '''

    if fold == 'top':
        cornerMedian += STROKE * fatness
    if fold == 'bottom':
        cornerMedian -= STROKE * fatness

    if side == 'right':
        horHalfBar(
            side,
            median=cornerMedian,
            buttL=-1 * STROKE,
            buttR=BUTT
        )
        x = WIDTH / 2 + STROKE * fatness

    if side == 'left':
        horHalfBar(
            side,
            median=cornerMedian,
            buttL=BUTT,
            buttR=-1 * STROKE
        )
        x = WIDTH / 2 - STROKE * fatness

    if fold == 'top':
        cornerMedian -= STROKE * fatness
        vertLine(
            boxPen,
            (x, cornerMedian),
            (x, cornerMedian + HEIGHT / 2),
            STROKE * fatness,
            buttB=-1 * STROKE
        )
    if fold == 'bottom':
        cornerMedian += STROKE * fatness
        vertLine(
            boxPen,
            (x, cornerMedian - HEIGHT / 2),
            (x, cornerMedian),
            STROKE * fatness,
            buttT=-1 * STROKE
        )


def shiftCoords(coordList, xShift=0, yShift=0):
    return [(x + xShift, y + yShift) for (x, y) in coordList]


if f is not None:
    print('Drawing boxes ...')

    generatedGlyphs = []
    # Keeping track of the glyph order

    for name, uni in sorted(recipes, key=lambda x: int(x[1], 16)):
        # sorting the dictionary by the Unicode value of the glyph.
        generatedGlyphs.append(name)
        commands = recipes[name, uni]
        print(name)

        g = f.newGlyph(name, clear=True)
        g.width = WIDTH
        g.unicode = int(uni, 16)
        boxPen = g.getPen()
        for command in commands:
            exec(command)

        if not IN_SHELL:
            g.removeOverlap()
            g.correctDirection()

        g.str = int(uni, 16)
        if not any([IN_GLYPHS, IN_FL]):
            g.changed()
        else:
            g.update()

    if not any([IN_GLYPHS, IN_FL]):
        f.changed()
    else:
        f.update()

    if IN_SHELL:
        timeString = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
        fileName = '%s_boxes.ufo' % timeString
        # fileName = 'boxes.ufo'
        f.lib['public.glyphOrder'] = generatedGlyphs
        outputPath = os.sep.join((os.path.curdir, fileName))
        f.save(outputPath)
        print('\nFind your UFO file at %s' % os.path.abspath(outputPath))

    if IN_FL:
        fl.UpdateFont(fl.ifont)

    if IN_RF:
        # Modifying the glyph order, so it looks like the glyphs
        # have been appended at the end of the font.
        glyphOrder = f.lib['public.glyphOrder']
        if not set(generatedGlyphs) <= set(glyphOrder):
            oldGlyphOrder = [g for g in glyphOrder if g not in generatedGlyphs]
            newGlyphOrder = oldGlyphOrder + generatedGlyphs
            f.glyphOrder = newGlyphOrder
            f.lib['public.glyphOrder'] = newGlyphOrder

    if IN_GLYPHS:
        # Update glyph names to comply with Glyphs' standard.
        for glyphName in generatedGlyphs:
            Font.glyphs[glyphName].updateGlyphInfo()
        Font.enableUpdateInterface()

    print('\nDone.')
