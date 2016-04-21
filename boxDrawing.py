#MenuTitle: boxDrawing

import math

__doc__ = '''

This script will draw the Unicode ranges "Box Drawing Characters" (U+2500 to
U+257F) and "Block Elements" (U+2580 to U+259F). It makes use of the Robofab
Python library (https://github.com/robofab-developers/robofab).
The script was successfully tested in RoboFont, Glyphs and FontLab.
It is possible to run this script straight from the command line, given that
Robofab can be imported. The box-drawing itself is done using combinations
of simple drawing commands; listed in the long dictionary below.

'''

# ----------------------------------------------------------------
# Edit these values if you want:
width        = 1000          # Glyph width.
height       = 1000          # Height for line elements, including overlap.
median       = 500           # Median line.
stroke       = 40            # General stroke weight.
fat          = 3             # Multiplication factor for drawing 'fat' lines; will multiply stroke weight.
radius       = width/2       # Radius for arc elements.
blockHeight  = 1000          # Height for block elements.
fatStroke    = stroke*fat    # Stroke thickness for 'fat' lines.
butt         = stroke*2      # Horizontal overlap.

# Those following values are for block elements, and are dependent of the values above.
blockOrigin = (0,median-blockHeight/2)
blockTop = (width,median+blockHeight/2)


# Nothing below here _needs_ to be edited, but feel free to do so:
# ----------------------------------------------------------------


# Checking which application we are in:

inRF = False
inFL = False
inGlyphs = False
inShell = False

if not any((inRF, inFL, inGlyphs)):
    try:
        import mojo.roboFont
        inRF = True
    except ImportError:
        pass

if not any((inRF, inFL, inGlyphs)):
    try:
        import GlyphsApp
        inGlyphs = True
    except ImportError:
        pass

if not any((inRF, inFL, inGlyphs)):
    try:
        import flsys
        inFL = True
    except ImportError:
        pass

if not any((inRF, inFL, inGlyphs)):
    inShell = True
    import os, time



if not inRF:
    from robofab.world import RFont, CurrentFont

if inGlyphs:
    try:
        import objectsGS, GSPen
    except ImportError:
        print '''
        The files GSPen.py and objectsGS.py are needed for Robofab to be working in Glyphs.
        Please get them at https://github.com/schriftgestalt/Glyphs-Scripts
        '''
    try:
        test = getattr(GSLayer, "removeOverlap")
        if not callable(test):
            raise
    except:
        raise AttributeError("Please update your objectsGS.py file. Download the latest verion at: https://github.com/schriftgestalt/Glyphs-Scripts")


# Check if a font is open -- if not, create a new one.

f = CurrentFont()

if f == None:
    f = RFont()

if f != None and inGlyphs:
    f._object.font.disableUpdateInterface()


names = {
    # List of glyphs and their drawing recipes.

    # Lines:
    ('lighthorzbxd', '2500'):                   ['horBar()'],

    ('heavyhorzbxd', '2501'):                   ['horBar(fat)'],

    ('lightvertbxd', '2502'):                   ['vertBar()'],

    ('heavyvertbxd', '2503'):                   ['vertBar(fat)'],

    ('lighttrpldashhorzbxd', '2504'):           ['dashedHorLine(boxPen, step=3)'],

    ('heavytrpldashhorzbxd', '2505'):           ['dashedHorLine(boxPen, step=3, stroke=fatStroke)'],

    ('lighttrpldashvertbxd', '2506'):           ['dashedVertLine(boxPen, step=3)'],

    ('heavytrpldashvertbxd', '2507'):           ['dashedVertLine(boxPen, step=3, stroke=fatStroke)'],

    ('lightquaddashhorzbxd', '2508'):           ['dashedHorLine(boxPen, step=4)'],

    ('heavyquaddashhorzbxd', '2509'):           ['dashedHorLine(boxPen, step=4, stroke=fatStroke)'],

    ('lightquaddashvertbxd', '250A'):           ['dashedVertLine(boxPen, step=4)'],

    ('heavyquaddashvertbxd', '250B'):           ['dashedVertLine(boxPen, step=4, stroke=fatStroke)'],

    ('lightdbldashhorzbxd', '254C'):            ['dashedHorLine(boxPen, step=2)'],

    ('heavydbldashhorzbxd', '254D'):            ['dashedHorLine(boxPen, step=2, stroke=fatStroke)'],

    ('lightdbldashvertbxd', '254E'):            ['dashedVertLine(boxPen, step=2)'],

    ('heavydbldashvertbxd', '254F'):            ['dashedVertLine(boxPen, step=2, stroke=fatStroke)'],


    # Corners:
    ('lightdnrightbxd', '250C'):                ['horHalfBar("right", buttL=stroke)',
                                                 'vertHalfBar("bottom")'],

    ('dnlightrightheavybxd', '250D'):           ['horHalfBar("right", fat, buttL=stroke)',
                                                 'vertHalfBar("bottom")'],

    ('dnheavyrightlightbxd', '250E'):           ['horHalfBar("right")',
                                                 'vertHalfBar("bottom", fat, buttT=stroke)'],

    ('heavydnrightbxd', '250F'):                ['horHalfBar("right", fat)',
                                                 'vertHalfBar("bottom", fat, buttT=fatStroke)'],

    ('lightdnleftbxd', '2510'):                 ['horHalfBar("left", buttR=stroke)',
                                                 'vertHalfBar("bottom")'],

    ('dnlightleftheavybxd', '2511'):            ['horHalfBar("left", fat, buttR=stroke)',
                                                 'vertHalfBar("bottom")'],

    ('dnheavyleftlightbxd', '2512'):            ['horHalfBar("left")',
                                                 'vertHalfBar("bottom", fat, buttT=stroke)'],

    ('heavydnleftbxd', '2513'):                 ['horHalfBar("left", fat)',
                                                 'vertHalfBar("bottom", fat, buttT=fatStroke)'],

    ('lightuprightbxd', '2514'):                ['horHalfBar("right", buttL=stroke)',
                                                 'vertHalfBar("top")'],

    ('uplightrightheavybxd', '2515'):           ['horHalfBar("right", fat, buttL=stroke)',
                                                 'vertHalfBar("top")'],

    ('upheavyrightlightbxd', '2516'):           ['horHalfBar("right")',
                                                 'vertHalfBar("top", fat, buttB=stroke)'],

    ('heavyuprightbxd', '2517'):                ['horHalfBar("right", fat)',
                                                 'vertHalfBar("top", fat, buttB=fatStroke)'],

    ('lightupleftbxd', '2518'):                 ['horHalfBar("left", buttR=stroke)',
                                                 'vertHalfBar("top")'],

    ('uplightleftheavybxd', '2519'):            ['horHalfBar("left", fat, buttR=stroke)',
                                                 'vertHalfBar("top")'],

    ('upheavyleftlightbxd', '251A'):            ['horHalfBar("left")',
                                                 'vertHalfBar("top", fat, buttB=stroke)'],

    ('heavyupleftbxd', '251B'):                 ['horHalfBar("left", fat)',
                                                 'vertHalfBar("top", fat, buttB=fatStroke)'],


    # Joints:
    ('lightvertrightbxd', '251C'):              ['horHalfBar("right")',
                                                 'vertBar()'],

    ('vertlightrightheavybxd', '251D'):         ['horHalfBar("right", fat)',
                                                 'vertBar()'],

    ('upheavyrightdnlightbxd', '251E'):         ['horHalfBar("right")',
                                                 'vertHalfBar("top", fat, buttB=stroke)',
                                                 'vertHalfBar("bottom")'],

    ('dnheavyrightuplightbxd', '251F'):         ['horHalfBar("right")',
                                                 'vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat, buttT=stroke)'],

    ('vertheavyrightlightbxd', '2520'):         ['horHalfBar("right")',
                                                 'vertBar(fat)'],

    ('dnlightrightupheavybxd', '2521'):         ['horHalfBar("right", fat)',
                                                 'vertHalfBar("top", fat, buttB=fatStroke)',
                                                 'vertHalfBar("bottom")'],

    ('uplightrightdnheavybxd', '2522'):         ['horHalfBar("right", fat)',
                                                 'vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat, buttT=fatStroke)'],

    ('heavyvertrightbxd', '2523'):              ['horHalfBar("right", fat)',
                                                 'vertBar(fat)'],

    ('lightvertleftbxd', '2524'):               ['horHalfBar("left")',
                                                 'vertBar()'],

    ('vertlightleftheavybxd', '2525'):          ['horHalfBar("left", fat)',
                                                 'vertBar()'],

    ('upheavyleftdnlightbxd', '2526'):          ['horHalfBar("left")',
                                                 'vertHalfBar("top", fat, buttB=stroke)',
                                                 'vertHalfBar("bottom")'],

    ('dnheavyleftuplightbxd', '2527'):          ['horHalfBar("left")',
                                                 'vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat, buttT=stroke)'],

    ('vertheavyleftlightbxd', '2528'):          ['horHalfBar("left")',
                                                 'vertBar(fat)'],

    ('dnlightleftupheavybxd', '2529'):          ['horHalfBar("left", fat)',
                                                 'vertHalfBar("top", fat, buttB=fatStroke)',
                                                 'vertHalfBar("bottom")'],

    ('uplightleftdnheavybxd', '252A'):          ['horHalfBar("left", fat)',
                                                 'vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat, buttT=fatStroke)'],

    ('heavyvertleftbxd', '252B'):               ['horHalfBar("left", fat)',
                                                 'vertBar(fat)'],

    ('lightdnhorzbxd', '252C'):                 ['horBar()',
                                                 'vertHalfBar("bottom")'],

    ('leftheavyrightdnlightbxd', '252D'):       ['horHalfBar("left", fat, buttR=stroke)',
                                                 'horHalfBar("right")',
                                                 'vertHalfBar("bottom")'],

    ('rightheavyleftdnlightbxd', '252E'):       ['horHalfBar("left")',
                                                 'horHalfBar("right", fat, buttL=stroke)',
                                                 'vertHalfBar("bottom")'],

    ('dnlighthorzheavybxd', '252F'):            ['horBar(fat)',
                                                 'vertHalfBar("bottom")'],

    ('dnheavyhorzlightbxd', '2530'):            ['horBar()',
                                                 'vertHalfBar("bottom", fat)'],

    ('rightlightleftdnheavybxd', '2531'):       ['horHalfBar("left", fat)',
                                                 'horHalfBar("right")',
                                                 'vertHalfBar("bottom", fat, buttT=fatStroke)'],

    ('leftlightrightdnheavybxd', '2532'):       ['horHalfBar("left")',
                                                 'horHalfBar("right", fat)',
                                                 'vertHalfBar("bottom", fat, buttT=fatStroke)'],

    ('heavydnhorzbxd', '2533'):                 ['horBar(fat)',
                                                 'vertHalfBar("bottom", fat)'],

    ('lightuphorzbxd', '2534'):                 ['horBar()',
                                                 'vertHalfBar("top")'],

    ('leftheavyrightuplightbxd', '2535'):       ['horHalfBar("left", fat, buttR=stroke)',
                                                 'horHalfBar("right")',
                                                 'vertHalfBar("top")'],

    ('rightheavyleftuplightbxd', '2536'):       ['horHalfBar("left")',
                                                 'horHalfBar("right", fat, buttL=stroke)',
                                                 'vertHalfBar("top")'],

    ('uplighthorzheavybxd', '2537'):            ['horBar(fat)',
                                                 'vertHalfBar("top")'],

    ('upheavyhorzlightbxd', '2538'):            ['horBar()',
                                                 'vertHalfBar("top", fat)'],

    ('rightlightleftupheavybxd', '2539'):       ['horHalfBar("left", fat)',
                                                 'horHalfBar("right")',
                                                 'vertHalfBar("top", fat, buttB=fatStroke)'],

    ('leftlightrightupheavybxd', '253A'):       ['horHalfBar("left")',
                                                 'horHalfBar("right", fat)',
                                                 'vertHalfBar("top", fat, buttB=fatStroke)'],

    ('heavyuphorzbxd', '253B'):                 ['horBar(fat)',
                                                 'vertHalfBar("top", fat)'],


    # Crossings:
    ('lightverthorzbxd', '253C'):               ['horBar()',
                                                 'vertBar()'],

    ('leftheavyrightvertlightbxd', '253D'):     ['horHalfBar("left", fat)',
                                                 'horHalfBar("right")',
                                                 'vertBar()'],

    ('rightheavyleftvertlightbxd', '253E'):     ['horHalfBar("left")',
                                                 'horHalfBar("right", fat)',
                                                 'vertBar()'],

    ('vertlighthorzheavybxd', '253F'):          ['horBar(fat)',
                                                 'vertBar()'],

    ('upheavydnhorzlightbxd', '2540'):          ['horBar()',
                                                 'vertHalfBar("top", fat)',
                                                 'vertHalfBar("bottom")'],

    ('dnheavyuphorzlightbxd', '2541'):          ['horBar()',
                                                 'vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat)'],

    ('vertheavyhorzlightbxd', '2542'):          ['horBar()',
                                                 'vertBar(fat)'],

    ('leftupheavyrightdnlightbxd', '2543'):     ['horHalfBar("left", fat, buttR=fatStroke)',
                                                 'horHalfBar("right")',
                                                 'vertHalfBar("top", fat)',
                                                 'vertHalfBar("bottom")'],

    ('rightupheavyleftdnlightbxd', '2544'):     ['horHalfBar("left")',
                                                 'horHalfBar("right", fat, buttL=fatStroke)',
                                                 'vertHalfBar("top", fat)',
                                                 'vertHalfBar("bottom")'],

    ('leftdnheavyrightuplightbxd', '2545'):     ['horHalfBar("left", fat, buttR=fatStroke)',
                                                 'horHalfBar("right")',
                                                 'vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat)'],

    ('rightdnheavyleftuplightbxd', '2546'):     ['horHalfBar("left")',
                                                 'horHalfBar("right", fat, buttL=fatStroke)',
                                                 'vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat)'],

    ('dnlightuphorzheavybxd', '2547'):          ['horBar(fat)',
                                                 'vertHalfBar("top", fat)',
                                                 'vertHalfBar("bottom")'],

    ('uplightdnhorzheavybxd', '2548'):          ['horBar(fat)',
                                                 'vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat)'],

    ('rightlightleftvertheavybxd', '2549'):     ['horHalfBar("left", fat)',
                                                 'horHalfBar("right")',
                                                 'vertBar(fat)'],

    ('leftlightrightvertheavybxd', '254A'):     ['horHalfBar("left")',
                                                 'horHalfBar("right", fat)',
                                                 'vertBar(fat)'],

    ('heavyverthorzbxd', '254B'):               ['horBar(fat)',
                                                 'vertBar(fat)'],


    # Double-stroked elements:
    ('dblhorzbxd', '2550'):                     ['horSplitBar()'],

    ('dblvertbxd', '2551'):                     ['vertSplitBar()'],

    ('dnsngrightdblbxd', '2552'):               ['horSplitHalfBar("right")',
                                                 'vertHalfBar("bottom", buttT=3*stroke)'],

    ('dndblrightsngbxd', '2553'):               ['horHalfBar("right", buttL=3*stroke)',
                                                 'vertSplitHalfBar("bottom", buttT=stroke)'],

    ('dbldnrightbxd', '2554'):                  ['outerCorner("right", "bottom")',
                                                 'innerCorner("right", "bottom")'],

    ('dnsngleftdblbxd', '2555'):                ['horSplitHalfBar("left")',
                                                 'vertHalfBar("bottom", buttT=3*stroke)'],

    ('dndblleftsngbxd', '2556'):                ['horHalfBar("left", buttR=3*stroke)',
                                                 'vertSplitHalfBar("bottom", buttT=stroke)'],

    ('dbldnleftbxd', '2557'):                   ['outerCorner("left", "bottom")',
                                                 'innerCorner("left", "bottom")'],

    ('upsngrightdblbxd', '2558'):               ['horSplitHalfBar("right")',
                                                 'vertHalfBar("top", buttB=3*stroke)'],

    ('updblrightsngbxd', '2559'):               ['horHalfBar("right", buttL=3*stroke)',
                                                 'vertSplitHalfBar("top", buttB=stroke)'],

    ('dbluprightbxd', '255A'):                  ['outerCorner("right", "top")',
                                                 'innerCorner("right", "top")'],

    ('upsngleftdblbxd', '255B'):                ['horSplitHalfBar("left")',
                                                 'vertHalfBar("top", buttB=3*stroke)'],

    ('updblleftsngbxd', '255C'):                ['horHalfBar("left", buttR=3*stroke)',
                                                 'vertSplitHalfBar("top", buttB=stroke)'],

    ('dblupleftbxd', '255D'):                   ['outerCorner("left", "top")',
                                                 'innerCorner("left", "top")'],

    ('vertsngrightdblbxd', '255E'):             ['horSplitHalfBar("right")',
                                                 'vertBar()'],

    ('vertdblrightsngbxd', '255F'):             ['horHalfBar("right", buttL=-stroke)',
                                                 'vertSplitBar()'],

    ('dblvertrightbxd', '2560'):                ['vertLine(boxPen, (width/2-stroke,median-height/2), (width/2-stroke,median+height/2), stroke)',
                                                 'innerCorner("right", "top")',
                                                 'innerCorner("right", "bottom")'],

    ('vertsngleftdblbxd', '2561'):              ['horSplitHalfBar("left")',
                                                 'vertBar()'],

    ('vertdblleftsngbxd', '2562'):              ['horHalfBar("left", buttR=-stroke)',
                                                 'vertSplitBar()'],

    ('dblvertleftbxd', '2563'):                 ['vertLine(boxPen, (width/2+stroke,median-height/2), (width/2+stroke,median+height/2), stroke)',
                                                 'innerCorner("left", "top")',
                                                 'innerCorner("left", "bottom")'],

    ('dnsnghorzdblbxd', '2564'):                ['horSplitBar()',
                                                 'vertLine(boxPen, (width/2, median-height/2), (width/2, median-stroke), stroke)'],

    ('dndblhorzsngbxd', '2565'):                ['horBar()',
                                                 'vertSplitHalfBar("bottom")'],

    ('dbldnhorzbxd', '2566'):                   ['horLine(boxPen, (0,median+stroke), (width,median+stroke), stroke)',
                                                 'innerCorner("left", "bottom")',
                                                 'innerCorner("right", "bottom")'],

    ('upsnghorzdblbxd', '2567'):                ['horSplitBar()',
                                                 'vertLine(boxPen, (width/2, median+stroke), (width/2, median+height/2), stroke)'],

    ('updblhorzsngbxd', '2568'):                ['horBar()',
                                                 'vertSplitHalfBar("top")'],

    ('dbluphorzbxd', '2569'):                   ['horLine(boxPen, (0,median-stroke), (width,median-stroke), stroke)',
                                                 'innerCorner("left", "top")',
                                                 'innerCorner("right", "top")'],

    ('vertsnghorzdblbxd', '256A'):              ['horSplitBar()',
                                                 'vertBar()'],

    ('vertdblhorzsngbxd', '256B'):              ['horBar()',
                                                 'vertSplitBar()'],

    ('dblverthorzbxd', '256C'):                 ['innerCorner("left", "top")',
                                                 'innerCorner("right", "top")',
                                                 'innerCorner("left", "bottom")', 'innerCorner("right", "bottom")'],


    # Rounded corners, diagonals:
    ('lightarcdnrightbxd', '256D'):             ['arc(boxPen, (width/2,median-height/2), (width,median), "TL", stroke, radius, butt)'],

    ('lightarcdnleftbxd', '256E'):              ['arc(boxPen, (width/2,median-height/2), (0,median), "TR", stroke, radius, butt)'],

    ('lightarcupleftbxd', '256F'):              ['arc(boxPen, (width/2,median+height/2), (0,median), "BR", stroke, radius, butt)'],

    ('lightarcuprightbxd', '2570'):             ['arc(boxPen, (width/2,median+height/2), (width,median), "BL", stroke, radius, butt)'],

    ('lightdiaguprightdnleftbxd', '2571'):      ['diagonal(boxPen, (0,median-blockHeight/2), (width,median+blockHeight/2), "bottomUp")'],

    ('lightdiagupleftdnrightbxd', '2572'):      ['diagonal(boxPen, (0,median+blockHeight/2), (width,median-blockHeight/2), "topDown")'],

    ('lightdiagcrossbxd', '2573'):              ['diagonal(boxPen, (0,median+blockHeight/2), (width,median-blockHeight/2), "topDown")',
                                                 'diagonal(boxPen, (0,median-blockHeight/2), (width,median+blockHeight/2), "bottomUp")'],


    # Half-width/Half-height:
    ('lightleftbxd', '2574'):                   ['horHalfBar("left", buttR=stroke)'],

    ('lightupbxd', '2575'):                     ['vertHalfBar("top", buttB=stroke)'],

    ('lightrightbxd', '2576'):                  ['horHalfBar("right", buttL=stroke)'],

    ('lightdnbxd', '2577'):                     ['vertHalfBar("bottom", buttT=stroke)'],

    ('heavyleftbxd', '2578'):                   ['horHalfBar("left", fat, buttR=stroke)'],

    ('heavyupbxd', '2579'):                     ['vertHalfBar("top", fat, buttB=stroke)'],

    ('heavyrightbxd', '257A'):                  ['horHalfBar("right", fat, buttL=stroke)'],

    ('heavydnbxd', '257B'):                     ['vertHalfBar("bottom", fat, buttT=stroke)'],

    ('lightleftheavyrightbxd', '257C'):         ['horHalfBar("left")',
                                                 'horHalfBar("right", fat, buttL=stroke)'],

    ('lightupheavydnbxd', '257D'):              ['vertHalfBar("top")',
                                                 'vertHalfBar("bottom", fat, buttT=stroke)'],

    ('heavyleftlightrightbxd', '257E'):         ['horHalfBar("right")',
                                                 'horHalfBar("left", fat, buttR=stroke)'],

    ('heavyuplightdnbxd', '257F'):              ['vertHalfBar("bottom")',
                                                 'vertHalfBar("top", fat, buttB=stroke)'],


    # Block elements:
    ('uphalfblock', '2580'):                    ['box(boxPen, start=(blockOrigin[0], median))'],

    ('dneighthblock', '2581'):                  ['box(boxPen, end=(width, blockOrigin[1]+blockHeight*1/8))'],

    ('dnquarterblock', '2582'):                 ['box(boxPen, end=(width, blockOrigin[1]+blockHeight*1/4))'],

    ('dnthreeeighthsblock', '2583'):            ['box(boxPen, end=(width, blockOrigin[1]+blockHeight*3/8))'],

    ('dnhalfblock', '2584'):                    ['box(boxPen, end=(width, blockOrigin[1]+blockHeight*1/2))'],

    ('dnfiveeighthsblock', '2585'):             ['box(boxPen, end=(width, blockOrigin[1]+blockHeight*5/8))'],

    ('dnthreequartersblock', '2586'):           ['box(boxPen, end=(width, blockOrigin[1]+blockHeight*3/4))'],

    ('dnseveneighthsblock', '2587'):            ['box(boxPen, end=(width, blockOrigin[1]+blockHeight*7/8))'],

    ('fullblock', '2588'):                      ['box(boxPen)'],

    ('leftseveneighthsblock', '2589'):          ['box(boxPen, end=(width*7/8, blockTop[1]))'],

    ('leftthreequartersblock', '258A'):         ['box(boxPen, end=(width*3/4, blockTop[1]))'],

    ('leftfiveeighthsblock', '258B'):           ['box(boxPen, end=(width*5/8, blockTop[1]))'],

    ('lefthalfblock', '258C'):                  ['box(boxPen, end=(width*1/2, blockTop[1]))'],

    ('leftthreeeighthsblock', '258D'):          ['box(boxPen, end=(width*3/8, blockTop[1]))'],

    ('leftquarterblock', '258E'):               ['box(boxPen, end=(width*1/4, blockTop[1]))'],

    ('lefteighthblock', '258F'):                ['box(boxPen, end=(width*1/8, blockTop[1]))'],

    ('righthalfblock', '2590'):                 ['box(boxPen, start=(width/2, blockOrigin[1]))'],

    ('upeighthblock', '2594'):                  ['box(boxPen, start=(blockOrigin[0], blockOrigin[1]+blockHeight*7/8))'],

    ('righteighthblock', '2595'):               ['box(boxPen, start=(width*7/8, blockOrigin[1]))'],


    # Shades:
    ('lightshade', '2591'):                     ['stripedShade(boxPen, "25")'],

    ('mediumshade', '2592'):                    ['stripedShade(boxPen, "50")'],

    ('darkshade', '2593'):                      ['stripedShade(boxPen, "75")'],


    # Quadrants:
    ('dnleftquadrant', '2596'):                 ['box(boxPen, end=(width*1/2, blockOrigin[1]+blockHeight*1/2))'],

    ('dnrightquadrant', '2597'):                ['box(boxPen, start=(width/2, blockOrigin[1]), end=(blockTop[0], median))'],

    ('upleftquadrant', '2598'):                 ['box(boxPen, start=(blockOrigin[0], median), end=(width*1/2, blockTop[1]))'],

    ('upleftdnleftdnrightquadrant', '2599'):    ['box(boxPen, end=(width*1/2, blockTop[1]))',
                                                 'box(boxPen, end=(width, blockOrigin[1]+blockHeight*1/2))'],

    ('upleftdnrightquadrant', '259A'):          ['box(boxPen, start=(width/2, blockOrigin[1]), end=(blockTop[0], median))',
                                                 'box(boxPen, start=(blockOrigin[0], median), end=(width*1/2, blockTop[1]))'],

    ('upleftuprightdnleftquadrant', '259B'):    ['box(boxPen, end=(width*1/2, blockTop[1]))',
                                                 'box(boxPen, start=(blockOrigin[0], median))'],

    ('upleftuprightdnrightquadrant', '259C'):   ['box(boxPen, start=(width/2, blockOrigin[1]))',
                                                 'box(boxPen, start=(blockOrigin[0], median))'],

    ('uprightquadrant', '259D'):                ['box(boxPen, start=(width/2, median))'],

    ('uprightdnleftquadrant', '259E'):          ['box(boxPen, end=(width*1/2, blockOrigin[1]+blockHeight*1/2))',
                                                 'box(boxPen, start=(width/2, median))'],

    ('uprightdnleftdnrightquadrant', '259F'):   ['box(boxPen, start=(width/2, blockOrigin[1]))',
                                                 'box(boxPen, end=(width, blockOrigin[1]+blockHeight*1/2))'],

}


def floatRange(x, y, step):
    "Variation on range(); since step values for dashed lines can sometimes be floats."
    while x < y:
        yield x
        x += step


def drawRect(pen, BL, BR, TR, TL):
    "General drawing function for a rectangle."

    pen.moveTo(BL)
    pen.lineTo(BR)
    pen.lineTo(TR)
    pen.lineTo(TL)
    pen.closePath()


def drawArc(pen, start1, start2, end1, end2, IAstart, IApoint1, IApoint2, IAend, OAstart, OApoint1, OApoint2, OAend):
    "General drawing function for an arc."

    pen.moveTo(start1)
    pen.lineTo(start2)
    pen.lineTo(IAstart)
    pen.curveTo(IApoint1, IApoint2, IAend)
    pen.lineTo(end1)
    pen.lineTo(end2)
    pen.lineTo(OAstart)
    pen.curveTo(OApoint1, OApoint2, OAend)

    pen.closePath()


def horLine(pen, start, end, stroke, buttL=butt, buttR=butt):
    "General drawing function for a horizontal line."

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
    "General drawing function for a vertical line."

    startX = start[0]
    startY = start[1]
    endX = end[0]
    endY = end[1]

    BL = (startX - stroke / 2, startY - buttB / 2)
    BR = (startX + stroke / 2, startY - buttB / 2)
    TR = (startX + stroke / 2, endY + buttT / 2)
    TL = (startX - stroke / 2, endY + buttT / 2)

    drawRect(pen, BL, BR, TR, TL)


def box(pen, start=blockOrigin, end=blockTop):
    "A box."

    startX = start[0]
    startY = start[1]
    endX = end[0]
    endY = end[1]

    BL = (startX, startY)
    BR = (endX,   startY)
    TR = (endX,   endY)
    TL = (startX, endY)

    drawRect(pen, BL, BR, TR, TL)


def dashedHorLine(pen, step, width=width, stroke=stroke):
    "Dashed horizontal bar."

    stepLength = width/step
    gap = stepLength/step
    for w in floatRange(0, width, stepLength):
        if w+stepLength-gap < width:
            w = w+gap/2 # centering the dashed line in the glyph
            horLine(boxPen, (w,median), (w+stepLength-gap,median), stroke, buttL=0, buttR=0)


def dashedVertLine(pen, step, length=blockHeight, stroke=stroke):
    "Dashed vertical bar."

    stepLength = length/step
    gap = stepLength/step
    top = median+blockHeight/2

    for h in floatRange(median-length/2, median+length/2, stepLength):
        if h+stepLength-gap < top:
            h += gap/2
            vertLine(boxPen, (width/2,h), (width/2,h+stepLength-gap), stroke)


def shade(pen, shade):
    "Shading patterns, consisting of little boxes."
    # Not used in recipes above, but maybe useful for somebody.

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

    for w in xrange(0, width, hstep):
        for h in xrange(median-blockHeight/2, median+blockHeight/2, vstep*2):
            box(boxPen, (w, h), (w+boxWidth, h+boxHeight))
            box(boxPen, (w+hstep/2, h+vstep), (w+boxWidth+hstep/2, h+boxHeight+vstep))


def diagonal(pen, start, end, direction):
    "Diagonal line in two possible directions; either bottomUp or topDown."

    diagonalLength = math.hypot(width, blockHeight)
    angle1 = math.asin(width / diagonalLength)
    angle2 = math.pi / 2 - angle1
    xDist = stroke / 2 / math.cos(angle1)
    yDist = stroke / 2 / math.cos(angle2)

    startX = start[0]
    startY = start[1]
    endX = end[0]
    endY = end[1]

    TL1  =  (startX+xDist,  startY)
    TL2  =  (startX,        startY)
    TL3  =  (startX,        startY-yDist)
    BR1  =  (endX-xDist,    endY)
    BR2  =  (endX,          endY)
    BR3  =  (endX,          endY+yDist)

    BL1  =  (startX,        startY+yDist)
    BL2  =  (startX,        startY)
    BL3  =  (startX+xDist,  startY)
    TR1  =  (endX,          endY-yDist)
    TR2  =  (endX,          endY)
    TR3  =  (endX-xDist,    endY)


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
    "Rounded corner."

    kappa = 4 * (math.sqrt(2) - 1) / 3
    # Bezier point distance for drawing circles.

    if side == 'TL':
        yflip =  1
        xflip =  1
    if side == 'BL':
        yflip = -1
        xflip =  1
    if side == 'TR':
        yflip =  1
        xflip = -1
    if side == 'BR':
        yflip = -1
        xflip = -1

    startX = start[0]
    startY = start[1]
    endX = end[0]
    endY = end[1]

    cStartX = startX
    cStartY = endY-(radius*yflip)
    cEndX   = startX+(radius*xflip)
    cEndY   = endY

    start1 = (startX-(stroke/2*xflip), startY)
    start2 = (startX+(stroke/2*xflip), startY)
    end1   = (endX+(butt/2*xflip), endY-(stroke/2*yflip))
    end2   = (endX+(butt/2*xflip), endY+(stroke/2*yflip))

    IAstart  = (cStartX+(stroke/2*xflip),cStartY)
    IApoint1 = (cStartX+(stroke/2*xflip),cStartY+((radius-stroke/2)*kappa*yflip))
    IApoint2 = (cEndX-((radius-stroke/2)*kappa*xflip),cEndY-(stroke/2*yflip))
    IAend    =  (cEndX,cEndY-(stroke/2*yflip))

    OAstart  = (cEndX,cEndY+(stroke/2*yflip))
    OApoint1 = (cEndX-((radius+stroke/2)*kappa*xflip), cEndY+(stroke/2*yflip))
    OApoint2 = (cStartX-(stroke/2*xflip), cStartY+((radius+stroke/2)*kappa*yflip))
    OAend    = (cStartX-(stroke/2*xflip),cStartY)

    drawArc(pen, start1, start2, end1, end2, IAstart, IApoint1, IApoint2, IAend, OAstart, OApoint1, OApoint2, OAend)


def horBar(fatness=1, median=median, buttL=butt, buttR=butt):
    "Horizontal bar."

    horLine(boxPen, (0,median), (width,median), stroke*fatness, buttL, buttR)


def vertBar(fatness=1, buttB=0, buttT=0):
    "Vertical bar."

    vertLine(boxPen, (width/2,median-height/2), (width/2,median+height/2), stroke*fatness, buttB, buttT)


def horHalfBar(side, fatness=1, median=median, buttL=butt, buttR=butt):
    "Half-width horizontal bar, left or right."

    if side == 'left':
        if buttR == butt: buttR = 0
        horLine(boxPen, (0,median), (width/2,median), stroke*fatness, buttL, buttR)
    elif side == 'right':
        if buttL == butt: buttL = 0
        horLine(boxPen, (width/2,median), (width,median), stroke*fatness, buttL, buttR)


def vertHalfBar(fold, fatness=1, buttB=0, buttT=0):
    "Half-height vertical bar, top or bottom."

    if fold == 'top':
        vertLine(boxPen, (width/2,median), (width/2,median+height/2), stroke*fatness, buttB, buttT)
    if fold == 'bottom':
        vertLine(boxPen, (width/2,median-height/2), (width/2,median), stroke*fatness, buttB, buttT)


def horSplitBar(fatness=1, buttL=butt, buttR=butt):
    "Double-stroked horizontal bar, left or right."

    topMedian = median + stroke * fatness
    bottomMedian = median - stroke * fatness

    horBar(fatness, topMedian, buttL, buttR)
    horBar(fatness, bottomMedian, buttL, buttR)


def vertSplitBar(fatness=1, buttB=0, buttT=0):
    "Double-stroked vertical bar, top or bottom."

    leftX = width/2-(stroke*fatness)
    rightX = width/2+(stroke*fatness)
    vertLine(boxPen, (leftX,median-height/2), (leftX,median+height/2), stroke*fatness, buttB, buttT)
    vertLine(boxPen, (rightX,median-height/2), (rightX,median+height/2), stroke*fatness, buttB, buttT)


def horSplitHalfBar(side, fatness=1, buttL=butt, buttR=butt):
    "Double-stroked half-width horizontal bar, left or right."

    topMedian = median + stroke * fatness
    bottomMedian = median - stroke * fatness

    horHalfBar(side, fatness, topMedian, buttL, buttR)
    horHalfBar(side, fatness, bottomMedian, buttL, buttR)


def vertSplitHalfBar(fold, fatness=1, buttB=0, buttT=0):
    "Double-stroked half-height vertical bar, top or bottom."

    leftX = width/2- stroke*fatness
    rightX = width/2+ stroke*fatness
    if fold == 'top':
        vertLine(boxPen, (leftX,median), (leftX,median+height/2), stroke*fatness, buttB, buttT)
        vertLine(boxPen, (rightX,median), (rightX,median+height/2), stroke*fatness, buttB, buttT)
    if fold == 'bottom':
        vertLine(boxPen, (leftX,median-height/2), (leftX,median), stroke*fatness, buttB, buttT)
        vertLine(boxPen, (rightX,median-height/2), (rightX,median), stroke*fatness, buttB, buttT)


def outerCorner(side, fold, fatness=1, cornerMedian=median):
    "Outer part of a double-stroked corner."

    if fold == 'top':
        cornerMedian -= stroke * fatness
    if fold == 'bottom':
        cornerMedian += stroke * fatness

    if side == 'right':
        horHalfBar(side, median=cornerMedian, buttL=3*stroke, buttR=butt)
        x = width/2- stroke*fatness
    if side == 'left':
        horHalfBar(side, median=cornerMedian, buttL=butt, buttR=3*stroke)
        x = width/2+ stroke*fatness

    if fold == 'top':
        cornerMedian += stroke * fatness
    if fold == 'bottom':
        cornerMedian -= stroke * fatness

    if fold == 'top':
        vertLine(boxPen, (x,cornerMedian), (x,cornerMedian+height/2), stroke*fatness, buttB = 3*stroke)
    if fold == 'bottom':
        vertLine(boxPen, (x,cornerMedian-height/2), (x,cornerMedian), stroke*fatness, buttT = 3*stroke)


def innerCorner(side, fold, fatness=1, cornerMedian=median):
    "Inner part of a double-stroked corner."

    if fold == 'top':
        cornerMedian += stroke * fatness
    if fold == 'bottom':
        cornerMedian -= stroke * fatness

    if side == 'right':
        horHalfBar(side, median=cornerMedian, buttL=-1*stroke, buttR=butt)
        x = width/2+ stroke*fatness
    if side == 'left':
        horHalfBar(side, median=cornerMedian, buttL=butt, buttR=-1*stroke)
        x = width/2- stroke*fatness

    if fold == 'top':
        cornerMedian -= stroke * fatness
    if fold == 'bottom':
        cornerMedian += stroke * fatness

    if fold == 'top':
        vertLine(boxPen, (x,cornerMedian), (x,cornerMedian+height/2), stroke*fatness, buttB = -1*stroke)
    if fold == 'bottom':
        vertLine(boxPen, (x,cornerMedian-height/2), (x,cornerMedian), stroke*fatness, buttT = -1*stroke)


def proximity(x, value, dist):
    # checks if a given value is close to another value
    # (used for hatched shades)
    if x > value - dist:
        return True
    else:
        return False


def stripedShade(pen, shade):
    "Shading patterns, consisting of diagonal lines boxes."

    # This function assumes a bunch of right triangles being moved across
    # the width of the glyph. Below, the law of sines is used for start-
    # and endpoint calculations.

    if shade == '25':
        step = width/2
    if shade == '50':
        step = width/4
    if shade == '75':
        step = width/8

    line = width/20
    diagonal = math.sqrt(width**2+blockHeight**2)
    angle = math.asin(blockHeight/diagonal)

    max = width
    # To determine where the iteration below can stop, this is the point where
    # the first diagonal line outside the glyph will cross the given baseline.

    xValues = []
    yValues = []
    for w in floatRange(0, max+line, step):

        if proximity(w, width, line):
            xValues.append(width)
        else:
            xValues.append(w)

        if proximity(w+line, width, line):
            xValues.append(width)
        else:
            xValues.append(w+line)

    yBottom = blockOrigin[1]
    yTop = blockOrigin[1] + blockHeight
    xLeft = 0
    xRight = width

    for v in xValues:
        target_y = yBottom + (v * math.sin(angle))/math.sin(math.radians(90)-angle)

        if proximity(v, yTop, line):
            yValues.append(int(round(target_y)))
        else:
            yValues.append(int(round(target_y)))

    drawList = []
    for step in xrange(0, len(xValues)-2, 2):
        xValues[step], xValues[step+1]
        drawList.append(((xValues[step], yBottom), (xValues[step+1], yBottom), (xLeft, yValues[step+1]), (xLeft, yValues[step])))

    for step in xrange(0, len(xValues)-2, 2):
        drawList.append(((xRight, yValues[step]), (xRight, yValues[step+1]), (xValues[step+1], yTop), (xValues[step], yTop)))

    for i in drawList:
        BL = i[0]
        BR = i[1]
        TR = i[2]
        TL = i[3]

        drawRect(pen, BL, BR, TR, TL)


# The main job is done here:

if f is not None:
    print 'Drawing boxes ...'

    generatedGlyphs = []
    # Keeping track of the glyph order

    for name, uni in sorted(names, key=lambda x: int(x[1], 16)):
        # sorting the dictionary by the Unicode value of the glyph.
        generatedGlyphs.append(name)
        commands = names[name, uni]
        print name

        g = f.newGlyph(name, clear=True)
        g.width = width
        boxPen = g.getPen()
        for command in commands:
            exec(command)

        if not inShell:
            g.removeOverlap()
            g.correctDirection()

        g.unicode = int(uni, 16)
        g.update()

    f.update()

    if inShell:
        timeString = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
        fileName = '%s_boxes.ufo' % timeString
        f.lib['public.glyphOrder'] = generatedGlyphs
        outputPath = os.sep.join((os.path.curdir, fileName))
        f.save(outputPath)
        print '\nFind your UFO file at %s' % os.path.abspath(outputPath)

    if inFL:
        fl.UpdateFont(fl.ifont)

    if inRF:
        # Modifying the glyph order, so it looks like the glyphs
        # have been appended at the end of the font.
        oldGlyphOrder = [ g for g in f.lib['public.glyphOrder'] if g not in generatedGlyphs ]
        newGlyphOrder = oldGlyphOrder + generatedGlyphs
        f.glyphOrder = newGlyphOrder
        f.lib['public.glyphOrder'] = newGlyphOrder

    if inGlyphs:
        f._object.font.enableUpdateInterface()

    print '\nDone.'
