recipes = {
    # dictionary of glyphs and their drawing recipes.

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


