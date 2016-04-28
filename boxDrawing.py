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
    import os
    import time



if not inRF:
    from robofab.world import RFont, CurrentFont

if inGlyphs:
    try:
        import objectsGS, GSPen
    except ImportError:
        print '''
        The files GSPen.py and objectsGS.py are needed for
        Robofab to work in Glyphs. Please get them at
        https://github.com/schriftgestalt/Glyphs-Scripts
        '''
    try:
        test = getattr(GSLayer, "removeOverlap")
        if not callable(test):
            raise
    except:
        raise AttributeError(
            '''\
            Please update your objectsGS.py file.
            Download the latest verion at:
            https://github.com/schriftgestalt/Glyphs-Scripts''')


# Check if a font is open -- if not, create a new one.

f = CurrentFont()

if f is None:
    f = RFont()

if f is not None and inGlyphs:
    f._object.font.disableUpdateInterface()


names = {
    # List of glyphs and their drawing recipes.

    # Lines:
    ('lighthorzbxd',
        '2500'): ['horBar()'],

    ('heavyhorzbxd',
        '2501'): ['horBar(FAT)'],

    ('lightvertbxd',
        '2502'): ['vertBar()'],

    ('heavyvertbxd',
        '2503'): ['vertBar(FAT)'],

    ('lighttrpldashhorzbxd',
        '2504'): ['dashedHorLine(boxPen, step=3)'],

    ('heavytrpldashhorzbxd',
        '2505'): ['dashedHorLine(boxPen, step=3, stroke=FAT_STROKE)'],

    ('lighttrpldashvertbxd',
        '2506'): ['dashedVertLine(boxPen, step=3)'],

    ('heavytrpldashvertbxd',
        '2507'): ['dashedVertLine(boxPen, step=3, stroke=FAT_STROKE)'],

    ('lightquaddashhorzbxd',
        '2508'): ['dashedHorLine(boxPen, step=4)'],

    ('heavyquaddashhorzbxd',
        '2509'): ['dashedHorLine(boxPen, step=4, stroke=FAT_STROKE)'],

    ('lightquaddashvertbxd',
        '250A'): ['dashedVertLine(boxPen, step=4)'],

    ('heavyquaddashvertbxd',
        '250B'): ['dashedVertLine(boxPen, step=4, stroke=FAT_STROKE)'],

    ('lightdbldashhorzbxd',
        '254C'): ['dashedHorLine(boxPen, step=2)'],

    ('heavydbldashhorzbxd',
        '254D'): ['dashedHorLine(boxPen, step=2, stroke=FAT_STROKE)'],

    ('lightdbldashvertbxd',
        '254E'): ['dashedVertLine(boxPen, step=2)'],

    ('heavydbldashvertbxd',
        '254F'): ['dashedVertLine(boxPen, step=2, stroke=FAT_STROKE)'],


    # Corners:
    ('lightdnrightbxd',
        '250C'): ['horHalfBar("right", buttL=STROKE)',
                  'vertHalfBar("bottom")'],

    ('dnlightrightheavybxd',
        '250D'): ['horHalfBar("right", FAT, buttL=STROKE)',
                  'vertHalfBar("bottom")'],

    ('dnheavyrightlightbxd',
        '250E'): ['horHalfBar("right")',
                  'vertHalfBar("bottom", FAT, buttT=STROKE)'],

    ('heavydnrightbxd',
        '250F'): ['horHalfBar("right", FAT)',
                  'vertHalfBar("bottom", FAT, buttT=FAT_STROKE)'],

    ('lightdnleftbxd',
        '2510'): ['horHalfBar("left", buttR=STROKE)',
                  'vertHalfBar("bottom")'],

    ('dnlightleftheavybxd',
        '2511'): ['horHalfBar("left", FAT, buttR=STROKE)',
                  'vertHalfBar("bottom")'],

    ('dnheavyleftlightbxd',
        '2512'): ['horHalfBar("left")',
                  'vertHalfBar("bottom", FAT, buttT=STROKE)'],

    ('heavydnleftbxd',
        '2513'): ['horHalfBar("left", FAT)',
                  'vertHalfBar("bottom", FAT, buttT=FAT_STROKE)'],

    ('lightuprightbxd',
        '2514'): ['horHalfBar("right", buttL=STROKE)',
                  'vertHalfBar("top")'],

    ('uplightrightheavybxd',
        '2515'): ['horHalfBar("right", FAT, buttL=STROKE)',
                  'vertHalfBar("top")'],

    ('upheavyrightlightbxd',
        '2516'): ['horHalfBar("right")',
                  'vertHalfBar("top", FAT, buttB=STROKE)'],

    ('heavyuprightbxd',
        '2517'): ['horHalfBar("right", FAT)',
                  'vertHalfBar("top", FAT, buttB=FAT_STROKE)'],

    ('lightupleftbxd',
        '2518'): ['horHalfBar("left", buttR=STROKE)',
                  'vertHalfBar("top")'],

    ('uplightleftheavybxd',
        '2519'): ['horHalfBar("left", FAT, buttR=STROKE)',
                  'vertHalfBar("top")'],

    ('upheavyleftlightbxd',
        '251A'): ['horHalfBar("left")',
                  'vertHalfBar("top", FAT, buttB=STROKE)'],

    ('heavyupleftbxd',
        '251B'): ['horHalfBar("left", FAT)',
                  'vertHalfBar("top", FAT, buttB=FAT_STROKE)'],


    # Joints:
    ('lightvertrightbxd',
        '251C'): ['horHalfBar("right")',
                  'vertBar()'],

    ('vertlightrightheavybxd',
        '251D'): ['horHalfBar("right", FAT)',
                  'vertBar()'],

    ('upheavyrightdnlightbxd',
        '251E'): ['horHalfBar("right")',
                  'vertHalfBar("top", FAT, buttB=STROKE)',
                  'vertHalfBar("bottom")'],

    ('dnheavyrightuplightbxd',
        '251F'): ['horHalfBar("right")',
                  'vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT, buttT=STROKE)'],

    ('vertheavyrightlightbxd',
        '2520'): ['horHalfBar("right")',
                  'vertBar(FAT)'],

    ('dnlightrightupheavybxd',
        '2521'): ['horHalfBar("right", FAT)',
                  'vertHalfBar("top", FAT, buttB=FAT_STROKE)',
                  'vertHalfBar("bottom")'],

    ('uplightrightdnheavybxd',
        '2522'): ['horHalfBar("right", FAT)',
                  'vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT, buttT=FAT_STROKE)'],

    ('heavyvertrightbxd',
        '2523'): ['horHalfBar("right", FAT)',
                  'vertBar(FAT)'],

    ('lightvertleftbxd',
        '2524'): ['horHalfBar("left")',
                  'vertBar()'],

    ('vertlightleftheavybxd',
        '2525'): ['horHalfBar("left", FAT)',
                  'vertBar()'],

    ('upheavyleftdnlightbxd',
        '2526'): ['horHalfBar("left")',
                  'vertHalfBar("top", FAT, buttB=STROKE)',
                  'vertHalfBar("bottom")'],

    ('dnheavyleftuplightbxd',
        '2527'): ['horHalfBar("left")',
                  'vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT, buttT=STROKE)'],

    ('vertheavyleftlightbxd',
        '2528'): ['horHalfBar("left")',
                  'vertBar(FAT)'],

    ('dnlightleftupheavybxd',
        '2529'): ['horHalfBar("left", FAT)',
                  'vertHalfBar("top", FAT, buttB=FAT_STROKE)',
                  'vertHalfBar("bottom")'],

    ('uplightleftdnheavybxd',
        '252A'): ['horHalfBar("left", FAT)',
                  'vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT, buttT=FAT_STROKE)'],

    ('heavyvertleftbxd',
        '252B'): ['horHalfBar("left", FAT)',
                  'vertBar(FAT)'],

    ('lightdnhorzbxd',
        '252C'): ['horBar()',
                  'vertHalfBar("bottom")'],

    ('leftheavyrightdnlightbxd',
        '252D'): ['horHalfBar("left", FAT, buttR=STROKE)',
                  'horHalfBar("right")',
                  'vertHalfBar("bottom")'],

    ('rightheavyleftdnlightbxd',
        '252E'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT, buttL=STROKE)',
                  'vertHalfBar("bottom")'],

    ('dnlighthorzheavybxd',
        '252F'): ['horBar(FAT)',
                  'vertHalfBar("bottom")'],

    ('dnheavyhorzlightbxd',
        '2530'): ['horBar()',
                  'vertHalfBar("bottom", FAT)'],

    ('rightlightleftdnheavybxd',
        '2531'): ['horHalfBar("left", FAT)',
                  'horHalfBar("right")',
                  'vertHalfBar("bottom", FAT, buttT=FAT_STROKE)'],

    ('leftlightrightdnheavybxd',
        '2532'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT)',
                  'vertHalfBar("bottom", FAT, buttT=FAT_STROKE)'],

    ('heavydnhorzbxd',
        '2533'): ['horBar(FAT)',
                  'vertHalfBar("bottom", FAT)'],

    ('lightuphorzbxd',
        '2534'): ['horBar()',
                  'vertHalfBar("top")'],

    ('leftheavyrightuplightbxd',
        '2535'): ['horHalfBar("left", FAT, buttR=STROKE)',
                  'horHalfBar("right")',
                  'vertHalfBar("top")'],

    ('rightheavyleftuplightbxd',
        '2536'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT, buttL=STROKE)',
                  'vertHalfBar("top")'],

    ('uplighthorzheavybxd',
        '2537'): ['horBar(FAT)',
                  'vertHalfBar("top")'],

    ('upheavyhorzlightbxd',
        '2538'): ['horBar()',
                  'vertHalfBar("top", FAT)'],

    ('rightlightleftupheavybxd',
        '2539'): ['horHalfBar("left", FAT)',
                  'horHalfBar("right")',
                  'vertHalfBar("top", FAT, buttB=FAT_STROKE)'],

    ('leftlightrightupheavybxd',
        '253A'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT)',
                  'vertHalfBar("top", FAT, buttB=FAT_STROKE)'],

    ('heavyuphorzbxd',
        '253B'): ['horBar(FAT)',
                  'vertHalfBar("top", FAT)'],


    # Crossings:
    ('lightverthorzbxd',
        '253C'): ['horBar()',
                  'vertBar()'],

    ('leftheavyrightvertlightbxd',
        '253D'): ['horHalfBar("left", FAT)',
                  'horHalfBar("right")',
                  'vertBar()'],

    ('rightheavyleftvertlightbxd',
        '253E'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT)',
                  'vertBar()'],

    ('vertlighthorzheavybxd',
        '253F'): ['horBar(FAT)',
                  'vertBar()'],

    ('upheavydnhorzlightbxd',
        '2540'): ['horBar()',
                  'vertHalfBar("top", FAT)',
                  'vertHalfBar("bottom")'],

    ('dnheavyuphorzlightbxd',
        '2541'): ['horBar()',
                  'vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT)'],

    ('vertheavyhorzlightbxd',
        '2542'): ['horBar()',
                  'vertBar(FAT)'],

    ('leftupheavyrightdnlightbxd',
        '2543'): ['horHalfBar("left", FAT, buttR=FAT_STROKE)',
                  'horHalfBar("right")',
                  'vertHalfBar("top", FAT)',
                  'vertHalfBar("bottom")'],

    ('rightupheavyleftdnlightbxd',
        '2544'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT, buttL=FAT_STROKE)',
                  'vertHalfBar("top", FAT)',
                  'vertHalfBar("bottom")'],

    ('leftdnheavyrightuplightbxd',
        '2545'): ['horHalfBar("left", FAT, buttR=FAT_STROKE)',
                  'horHalfBar("right")',
                  'vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT)'],

    ('rightdnheavyleftuplightbxd',
        '2546'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT, buttL=FAT_STROKE)',
                  'vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT)'],

    ('dnlightuphorzheavybxd',
        '2547'): ['horBar(FAT)',
                  'vertHalfBar("top", FAT)',
                  'vertHalfBar("bottom")'],

    ('uplightdnhorzheavybxd',
        '2548'): ['horBar(FAT)',
                  'vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT)'],

    ('rightlightleftvertheavybxd',
        '2549'): ['horHalfBar("left", FAT)',
                  'horHalfBar("right")',
                  'vertBar(FAT)'],

    ('leftlightrightvertheavybxd',
        '254A'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT)',
                  'vertBar(FAT)'],

    ('heavyverthorzbxd',
        '254B'): ['horBar(FAT)',
                  'vertBar(FAT)'],


    # Double-stroked elements:
    ('dblhorzbxd',
        '2550'): ['horSplitBar()'],

    ('dblvertbxd',
        '2551'): ['vertSplitBar()'],

    ('dnsngrightdblbxd',
        '2552'): ['horSplitHalfBar("right")',
                  'vertHalfBar("bottom", buttT=3*STROKE)'],

    ('dndblrightsngbxd',
        '2553'): ['horHalfBar("right", buttL=3*STROKE)',
                  'vertSplitHalfBar("bottom", buttT=STROKE)'],

    ('dbldnrightbxd',
        '2554'): ['outerCorner("right", "bottom")',
                  'innerCorner("right", "bottom")'],

    ('dnsngleftdblbxd',
        '2555'): ['horSplitHalfBar("left")',
                  'vertHalfBar("bottom", buttT=3*STROKE)'],

    ('dndblleftsngbxd',
        '2556'): ['horHalfBar("left", buttR=3*STROKE)',
                  'vertSplitHalfBar("bottom", buttT=STROKE)'],

    ('dbldnleftbxd',
        '2557'): ['outerCorner("left", "bottom")',
                  'innerCorner("left", "bottom")'],

    ('upsngrightdblbxd',
        '2558'): ['horSplitHalfBar("right")',
                  'vertHalfBar("top", buttB=3*STROKE)'],

    ('updblrightsngbxd',
        '2559'): ['horHalfBar("right", buttL=3*STROKE)',
                  'vertSplitHalfBar("top", buttB=STROKE)'],

    ('dbluprightbxd',
        '255A'): ['outerCorner("right", "top")',
                  'innerCorner("right", "top")'],

    ('upsngleftdblbxd',
        '255B'): ['horSplitHalfBar("left")',
                  'vertHalfBar("top", buttB=3*STROKE)'],

    ('updblleftsngbxd',
        '255C'): ['horHalfBar("left", buttR=3*STROKE)',
                  'vertSplitHalfBar("top", buttB=STROKE)'],

    ('dblupleftbxd',
        '255D'): ['outerCorner("left", "top")',
                  'innerCorner("left", "top")'],

    ('vertsngrightdblbxd',
        '255E'): ['horSplitHalfBar("right")',
                  'vertBar()'],

    ('vertdblrightsngbxd',
        '255F'): ['horHalfBar("right", buttL=-STROKE)',
                  'vertSplitBar()'],

    ('dblvertrightbxd',
        '2560'): ['vertLine(boxPen, (WIDTH/2-STROKE,MEDIAN-HEIGHT/2), (WIDTH/2-STROKE,MEDIAN+HEIGHT/2), STROKE)',
                  'innerCorner("right", "top")',
                  'innerCorner("right", "bottom")'],

    ('vertsngleftdblbxd',
        '2561'): ['horSplitHalfBar("left")',
                  'vertBar()'],

    ('vertdblleftsngbxd',
        '2562'): ['horHalfBar("left", buttR=-STROKE)',
                  'vertSplitBar()'],

    ('dblvertleftbxd',
        '2563'): ['vertLine(boxPen, (WIDTH/2+STROKE,MEDIAN-HEIGHT/2), (WIDTH/2+STROKE,MEDIAN+HEIGHT/2), STROKE)',
                  'innerCorner("left", "top")',
                  'innerCorner("left", "bottom")'],

    ('dnsnghorzdblbxd',
        '2564'): ['horSplitBar()',
                  'vertLine(boxPen, (WIDTH/2, MEDIAN-HEIGHT/2), (WIDTH/2, MEDIAN-STROKE), STROKE)'],

    ('dndblhorzsngbxd',
        '2565'): ['horBar()',
                  'vertSplitHalfBar("bottom")'],

    ('dbldnhorzbxd',
        '2566'): ['horLine(boxPen, (0,MEDIAN+STROKE), (WIDTH,MEDIAN+STROKE), STROKE)',
                  'innerCorner("left", "bottom")',
                  'innerCorner("right", "bottom")'],

    ('upsnghorzdblbxd',
        '2567'): ['horSplitBar()',
                  'vertLine(boxPen, (WIDTH/2, MEDIAN+STROKE), (WIDTH/2, MEDIAN+HEIGHT/2), STROKE)'],

    ('updblhorzsngbxd',
        '2568'): ['horBar()',
                  'vertSplitHalfBar("top")'],

    ('dbluphorzbxd',
        '2569'): ['horLine(boxPen, (0,MEDIAN-STROKE), (WIDTH,MEDIAN-STROKE), STROKE)',
                  'innerCorner("left", "top")',
                  'innerCorner("right", "top")'],

    ('vertsnghorzdblbxd',
        '256A'): ['horSplitBar()',
                  'vertBar()'],

    ('vertdblhorzsngbxd',
        '256B'): ['horBar()',
                  'vertSplitBar()'],

    ('dblverthorzbxd',
        '256C'): ['innerCorner("left", "top")',
                  'innerCorner("right", "top")',
                  'innerCorner("left", "bottom")',
                  'innerCorner("right", "bottom")'],


    # Rounded corners, diagonals:
    ('lightarcdnrightbxd',
        '256D'): ['arc(boxPen, (WIDTH/2,MEDIAN-HEIGHT/2), (WIDTH,MEDIAN), "TL", STROKE, RADIUS, BUTT)'],

    ('lightarcdnleftbxd',
        '256E'): ['arc(boxPen, (WIDTH/2,MEDIAN-HEIGHT/2), (0,MEDIAN), "TR", STROKE, RADIUS, BUTT)'],

    ('lightarcupleftbxd',
        '256F'): ['arc(boxPen, (WIDTH/2,MEDIAN+HEIGHT/2), (0,MEDIAN), "BR", STROKE, RADIUS, BUTT)'],

    ('lightarcuprightbxd',
        '2570'): ['arc(boxPen, (WIDTH/2,MEDIAN+HEIGHT/2), (WIDTH,MEDIAN), "BL", STROKE, RADIUS, BUTT)'],

    ('lightdiaguprightdnleftbxd',
        '2571'): ['diagonal(boxPen, (0,MEDIAN-EM_HEIGHT/2), (WIDTH,MEDIAN+EM_HEIGHT/2), "bottomUp")'],

    ('lightdiagupleftdnrightbxd',
        '2572'): ['diagonal(boxPen, (0,MEDIAN+EM_HEIGHT/2), (WIDTH,MEDIAN-EM_HEIGHT/2), "topDown")'],

    ('lightdiagcrossbxd',
        '2573'): ['diagonal(boxPen, (0,MEDIAN+EM_HEIGHT/2), (WIDTH,MEDIAN-EM_HEIGHT/2), "topDown")',
                  'diagonal(boxPen, (0,MEDIAN-EM_HEIGHT/2), (WIDTH,MEDIAN+EM_HEIGHT/2), "bottomUp")'],


    # Half-width/Half-height:
    ('lightleftbxd',
        '2574'): ['horHalfBar("left", buttR=STROKE)'],

    ('lightupbxd',
        '2575'): ['vertHalfBar("top", buttB=STROKE)'],

    ('lightrightbxd',
        '2576'): ['horHalfBar("right", buttL=STROKE)'],

    ('lightdnbxd',
        '2577'): ['vertHalfBar("bottom", buttT=STROKE)'],

    ('heavyleftbxd',
        '2578'): ['horHalfBar("left", FAT, buttR=STROKE)'],

    ('heavyupbxd',
        '2579'): ['vertHalfBar("top", FAT, buttB=STROKE)'],

    ('heavyrightbxd',
        '257A'): ['horHalfBar("right", FAT, buttL=STROKE)'],

    ('heavydnbxd',
        '257B'): ['vertHalfBar("bottom", FAT, buttT=STROKE)'],

    ('lightleftheavyrightbxd',
        '257C'): ['horHalfBar("left")',
                  'horHalfBar("right", FAT, buttL=STROKE)'],

    ('lightupheavydnbxd',
        '257D'): ['vertHalfBar("top")',
                  'vertHalfBar("bottom", FAT, buttT=STROKE)'],

    ('heavyleftlightrightbxd',
        '257E'): ['horHalfBar("right")',
                  'horHalfBar("left", FAT, buttR=STROKE)'],

    ('heavyuplightdnbxd',
        '257F'): ['vertHalfBar("bottom")',
                  'vertHalfBar("top", FAT, buttB=STROKE)'],


    # Block elements:
    ('uphalfblock',
        '2580'): ['box(boxPen, start=(BLOCK_ORIGIN[0], MEDIAN))'],

    ('dneighthblock',
        '2581'): ['box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 1/8))'],

    ('dnquarterblock',
        '2582'): ['box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 1/4))'],

    ('dnthreeeighthsblock',
        '2583'): ['box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 3/8))'],

    ('dnhalfblock',
        '2584'): ['box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 1/2))'],

    ('dnfiveeighthsblock',
        '2585'): ['box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 5/8))'],

    ('dnthreequartersblock',
        '2586'): ['box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 3/4))'],

    ('dnseveneighthsblock',
        '2587'): ['box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 7/8))'],

    ('fullblock',
        '2588'): ['box(boxPen)'],

    ('leftseveneighthsblock',
        '2589'): ['box(boxPen, end=(WIDTH * 7/8, BLOCK_TOP[1]))'],

    ('leftthreequartersblock',
        '258A'): ['box(boxPen, end=(WIDTH * 3/4, BLOCK_TOP[1]))'],

    ('leftfiveeighthsblock',
        '258B'): ['box(boxPen, end=(WIDTH * 5/8, BLOCK_TOP[1]))'],

    ('lefthalfblock',
        '258C'): ['box(boxPen, end=(WIDTH * 1/2, BLOCK_TOP[1]))'],

    ('leftthreeeighthsblock',
        '258D'): ['box(boxPen, end=(WIDTH * 3/8, BLOCK_TOP[1]))'],

    ('leftquarterblock',
        '258E'): ['box(boxPen, end=(WIDTH * 1/4, BLOCK_TOP[1]))'],

    ('lefteighthblock',
        '258F'): ['box(boxPen, end=(WIDTH * 1/8, BLOCK_TOP[1]))'],

    ('righthalfblock',
        '2590'): ['box(boxPen, start=(WIDTH/2, BLOCK_ORIGIN[1]))'],

    ('upeighthblock',
        '2594'): ['box(boxPen, start=(BLOCK_ORIGIN[0], BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 7/8))'],

    ('righteighthblock',
        '2595'): ['box(boxPen, start=(WIDTH * 7/8, BLOCK_ORIGIN[1]))'],


    # Shades:
    ('lightshade',
        '2591'): ['polkaShade(boxPen, "25")'],

    ('mediumshade',
        '2592'): ['polkaShade(boxPen, "50")'],

    ('darkshade',
        '2593'): ['polkaShade(boxPen, "75")'],


    # Quadrants:
    ('dnleftquadrant',
        '2596'): ['box(boxPen, end=(WIDTH * 1/2, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 1/2))'],

    ('dnrightquadrant',
        '2597'): ['box(boxPen, start=(WIDTH / 2, BLOCK_ORIGIN[1]), end=(BLOCK_TOP[0], MEDIAN))'],

    ('upleftquadrant',
        '2598'): ['box(boxPen, start=(BLOCK_ORIGIN[0], MEDIAN), end=(WIDTH * 1/2, BLOCK_TOP[1]))'],

    ('upleftdnleftdnrightquadrant',
        '2599'): ['box(boxPen, end=(WIDTH * 1/2, BLOCK_TOP[1]))',
                  'box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 1/2))'],

    ('upleftdnrightquadrant',
        '259A'): ['box(boxPen, start=(WIDTH / 2, BLOCK_ORIGIN[1]), end=(BLOCK_TOP[0], MEDIAN))',
                  'box(boxPen, start=(BLOCK_ORIGIN[0], MEDIAN), end=(WIDTH * 1/2, BLOCK_TOP[1]))'],

    ('upleftuprightdnleftquadrant',
        '259B'): ['box(boxPen, end=(WIDTH * 1/2, BLOCK_TOP[1]))',
                  'box(boxPen, start=(BLOCK_ORIGIN[0], MEDIAN))'],

    ('upleftuprightdnrightquadrant',
        '259C'): ['box(boxPen, start=(WIDTH / 2, BLOCK_ORIGIN[1]))',
                  'box(boxPen, start=(BLOCK_ORIGIN[0], MEDIAN))'],

    ('uprightquadrant',
        '259D'): ['box(boxPen, start=(WIDTH / 2, MEDIAN))'],

    ('uprightdnleftquadrant',
        '259E'): ['box(boxPen, end=(WIDTH * 1/2, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 1/2))',
                  'box(boxPen, start=(WIDTH / 2, MEDIAN))'],

    ('uprightdnleftdnrightquadrant',
        '259F'): ['box(boxPen, start=(WIDTH / 2, BLOCK_ORIGIN[1]))',
                  'box(boxPen, end=(WIDTH, BLOCK_ORIGIN[1] + BLOCK_HEIGHT * 1/2))'],

}


def roundInt(float):
    return int(round(float))


def floatRange(x, y, step):
    "Variation on range(), since step values for dashed lines may be floats."
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


def drawPoly(pen, *coords):
    "General drawing function for a polygon."

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


def horLine(pen, start, end, stroke, buttL=BUTT, buttR=BUTT):
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
    endY = end[1]

    BL = (startX - stroke / 2, startY - buttB / 2)
    BR = (startX + stroke / 2, startY - buttB / 2)
    TR = (startX + stroke / 2, endY + buttT / 2)
    TL = (startX - stroke / 2, endY + buttT / 2)

    drawRect(pen, BL, BR, TR, TL)


def box(pen, start=BLOCK_ORIGIN, end=BLOCK_TOP):
    "A box."

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
    "Dashed horizontal bar."

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
    "Dashed vertical bar."

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
    "Shading patterns, consisting of polka dots."
    # Not used in recipes above, but maybe useful for somebody.

    vstep = 100
    hstep = 200
    if shade == '25':
        radius = 24
    if shade == '50':
        radius = 36
    if shade == '75':
        radius = 54

    for w in xrange(0, WIDTH, hstep):
        for h in xrange(
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
    "Shading patterns, consisting of little boxes."
    # Not used in recipes above, but maybe useful for somebody.
    # Reliable way to crash makeOTF

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

    for w in xrange(0, WIDTH, hstep):
        for h in xrange(
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
    "Shading patterns, consisting of diagonal lines."

    # This function assumes a bunch of right triangles being moved across
    # the width of the glyph. Below, the law of sines is used for start-
    # and endpoint calculations.

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
    "Boring shading patterns, consisting of vertical lines."

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
    "Diagonal line in two possible directions; either bottomUp or topDown."

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
    "Rounded corner."

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
    "Horizontal bar."

    horLine(
        boxPen,
        (0, median),
        (WIDTH, median),
        STROKE * fatness,
        buttL, buttR
    )


def vertBar(fatness=1, buttB=0, buttT=0):
    "Vertical bar."

    vertLine(
        boxPen,
        (WIDTH / 2, MEDIAN - HEIGHT / 2),
        (WIDTH / 2, MEDIAN + HEIGHT / 2),
        STROKE * fatness,
        buttB, buttT
    )


def horHalfBar(side, fatness=1, median=MEDIAN, buttL=BUTT, buttR=BUTT):
    "Halfwidth horizontal bar, left or right."

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
    "Half-height vertical bar, top or bottom."

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
    "Double-stroked horizontal bar, left or right."

    topMedian = MEDIAN + STROKE * fatness
    bottomMedian = MEDIAN - STROKE * fatness

    horBar(fatness, topMedian, buttL, buttR)
    horBar(fatness, bottomMedian, buttL, buttR)


def vertSplitBar(fatness=1, buttB=0, buttT=0):
    "Double-stroked vertical bar, top or bottom."

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
    "Double-stroked halfwidth horizontal bar, left or right."

    topMedian = MEDIAN + STROKE * fatness
    bottomMedian = MEDIAN - STROKE * fatness

    horHalfBar(side, fatness, topMedian, buttL, buttR)
    horHalfBar(side, fatness, bottomMedian, buttL, buttR)


def vertSplitHalfBar(fold, fatness=1, buttB=0, buttT=0):
    "Double-stroked half-height vertical bar, top or bottom."

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
    "Outer part of a double-stroked corner."

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
    "Inner part of a double-stroked corner."

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
        g.width = WIDTH
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
        fileName = 'boxes.ufo'
        f.lib['public.glyphOrder'] = generatedGlyphs
        outputPath = os.sep.join((os.path.curdir, fileName))
        f.save(outputPath)
        print '\nFind your UFO file at %s' % os.path.abspath(outputPath)

    if inFL:
        fl.UpdateFont(fl.ifont)

    if inRF:
        # Modifying the glyph order, so it looks like the glyphs
        # have been appended at the end of the font.
        oldGlyphOrder = [
            g for g in f.lib['public.glyphOrder'] if g not in generatedGlyphs
        ]
        newGlyphOrder = oldGlyphOrder + generatedGlyphs
        f.glyphOrder = newGlyphOrder
        f.lib['public.glyphOrder'] = newGlyphOrder

    if inGlyphs:
        f._object.font.enableUpdateInterface()

    print '\nDone.'
