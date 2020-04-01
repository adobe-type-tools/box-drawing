# boxDrawing.py

Soon after the first public release of [Source Code Pro][scp], users noted a lack of [Box Drawing Characters][boxwiki]. 
Fortunately, this flaw could be remedied soon after—the whole set of Box Drawing Characters, plus all of the Block Elements are now part of Source Code Pro.  

[Source Code Pro][scp] is a typeface family intended for both programmers and designers. It has a fairly wide range of weights, therefore it was agreed to adjust the Box Drawing Characters in their stem widths, to make for a better corresponding appearance.
The reasoning behind this decision is that everyone will benefit: The programmer will like the screen display adjusted to the chosen text weight. 
The graphic designer will appreciate a multitude of combination possibilities; and an unseen dynamic range of drawing boxes.

All that is why this script was written. Drawing those generic glyphs by hand is not an amazing or creativity-challenging task. Much more fun is derived from modifying a script, which is capable of generating the most unexpected variations of Box Drawing Characters—over and over.


## What does this script do?

This script will draw the complete ranges of [Box Drawing Characters (`U+2500`–`U+257F`)][box] and [Block Elements (`U+2580`–`U+259F`)][block] in the font editor of your choice.  
The design of those characters is based on a handful of parameters, which can be changed in the script file itself. 
Feel free to create Box Drawing Characters that are longer than usual; exceedingly wide, fat (both?); or hairline-thin.  


Time was spent to make this script compatible with the triumvirate of commercial font editing applications; this means that this script will run in [RoboFont][], [Glyphs][], ~and even [FontLab][]~ without any modifications. It is also possible to run the script straight from the command line, which will generate a new [UFO file][ufo] right to your desktop.

_(NB: FontLab 5 can no longer be tested because macOS 10.15 does not run 32-bit applications)._


__Tested versions:__  
Robofont: Version Version 3.4b (build 2003232105)
Glyphs: Version 2.6.1 (1230)


__Dependencies:__  

- When using Glyphs or FontLab, [Robofab][] must be installed and working.

- When using Glyphs, please make sure you have the [GSPen.py][] and [objectsGS.py][] modules installed.

- When running the script from the command line, the [FontParts][] Python module must be installed.


## What does this script not do?

This script is not for adding Box Drawing Characters to existing, compiled fonts.  
It is assumed you have type design software, and font source data available; or at least know what to do with a [UFO file][ufo].


## What are Box Drawing Characters?

__Box Drawing__ [Unicode range 2500-257F][box] and __Block Elements__ [Unicode range 2580-259F][block]:

|         |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  A  |  B  |  C  |  D  |  E  |  F  |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| U+250x  |  ─  |  ━  |  │  |  ┃  |  ┄  |  ┅  |  ┆  |  ┇  |  ┈  |  ┉  |  ┊  |  ┋  |  ┌  |  ┍  |  ┎  |  ┏  |
| U+251x  |  ┐  |  ┑  |  ┒  |  ┓  |  └  |  ┕  |  ┖  |  ┗  |  ┘  |  ┙  |  ┚  |  ┛  |  ├  |  ┝  |  ┞  |  ┟  |
| U+252x  |  ┠  |  ┡  |  ┢  |  ┣  |  ┤  |  ┥  |  ┦  |  ┧  |  ┨  |  ┩  |  ┪  |  ┫  |  ┬  |  ┭  |  ┮  |  ┯  |
| U+253x  |  ┰  |  ┱  |  ┲  |  ┳  |  ┴  |  ┵  |  ┶  |  ┷  |  ┸  |  ┹  |  ┺  |  ┻  |  ┼  |  ┽  |  ┾  |  ┿  |
| U+254x  |  ╀  |  ╁  |  ╂  |  ╃  |  ╄  |  ╅  |  ╆  |  ╇  |  ╈  |  ╉  |  ╊  |  ╋  |  ╌  |  ╍  |  ╎  |  ╏  |
| U+255x  |  ═  |  ║  |  ╒  |  ╓  |  ╔  |  ╕  |  ╖  |  ╗  |  ╘  |  ╙  |  ╚  |  ╛  |  ╜  |  ╝  |  ╞  |  ╟  |
| U+256x  |  ╠  |  ╡  |  ╢  |  ╣  |  ╤  |  ╥  |  ╦  |  ╧  |  ╨  |  ╩  |  ╪  |  ╫  |  ╬  |  ╭  |  ╮  |  ╯  |
| U+257x  |  ╰  |  ╱  |  ╲  |  ╳  |  ╴  |  ╵  |  ╶  |  ╷  |  ╸  |  ╹  |  ╺  |  ╻  |  ╼  |  ╽  |  ╾  |  ╿  |
| U+258x  |  ▀  |  ▁  |  ▂  |  ▃  |  ▄  |  ▅  |  ▆  |  ▇  |  █  |  ▉  |  ▊  |  ▋  |  ▌  |  ▍  |  ▎  |  ▏  |
| U+259x  |  ▐  |  ░  |  ▒  |  ▓  |  ▔  |  ▕  |  ▖  |  ▗  |  ▘  |  ▙  |  ▚  |  ▛  |  ▜  |  ▝  |  ▞  |  ▟  |


Both Box Drawing Characters and Block Elements are mostly at home in the world of text-based UI; you might remember brilliant examples from MS-DOS Defrag or ScanDisk.

	    ┌─┬────────────┐
	┌───┘ │ Beautiful  │  
	│     │ box.       │  ┌────────────╖
	│     ╰─┰──────────┤  │ Another    ╟┐
	│       ┃ The same │  │ quite nice ║│
	│       ┃ ole box. │  │ box.       ║│
	└───────┸──────────┘  ╘╤═══════════╝│
	                       └────────────┘       

Box Drawing Characters can also be used for graphic design.
As an example, see the “source code” (pun) of the [Adobe Type Team holiday card 2012][xmas]:

	╔═*╓─╭╍╮╓─o*›┍━┑╻ ▲,┌─»
	╚═╗║╍╽┅╈╙─╖¡ ┆0┆╽╲╿ ┕━┓
	╚═╜╙━╹©╹╚═╱╳∙┕═┙╵=╹_└─┛
	╦┉╴╓─╮╓─ ╱╳¤╳╲┕ ┎─┎┬┬┒•
	║ ╗║─╮╬(•╱∑╳ɔ╲¡ʻ┣╸ || ┒
	╙─©◊ ◊╙─╱╳╳⅓╳╳╲┆┖─:┗┛ ┸
	┎╲ ╷╭─┨?╱╳¿╳╳▲╲♪╔═╡****
	┃╲╲┃┃─╮╱↑╳╳╳ợ╳╳╲╚═╗from
	╵ H┚╰─ᵒ╱╳╳∞╳╳╳¤╲╞═╝the↓
	↓╎O┊◊ˈ╱╳◉╳%╳╳=╳╳╲◆╦═╦═]
	H╎L┊─╱♪╳╳ʷ╳ ∫╳ §╲┊║A║™]
	A╎I┊╍╱╳∂╳╳◆╳╳╳Ω╳ ╲┊D┊═╗
	P─D──╱╳╳¶╳ ╳$╳  ¤╳┊O┊T║
	P║A┊╱╳ Ø╳╳ƒ╳╳╳☑╳  ╲B┊Y║
	Y║Y┊╱¤╳╳œ╳╳╳Ṃ ╳╳| ╲E┊P║
	│┐S╱╳╳╳ˣ╳╳×╳╳╳◆ ╳¤╳╲┊E│
	↓ !!┟╥─╯┍╇┯█┯╇┑▚│┇──┴─┊
	   ╶═╝┎┘│━┵┼┶━│┈╢TEAM<╯
	   ╺━│┃░▒▓▌!▐▓▒░┃││┼☑┘╳

	
The [Project Page][] has some more examples for Box Drawing Characters in use (using Source Code Pro as a web font).


## Usage:
- Open font editor of your choice (one of the three mentioned above).
- Open the `boxDrawing.py` script file in your font editor; or move it (and `boxDrawingRecipes.py`) to your scripts folder.
- Run.
- Watch Box Drawing Characters emerge.
- Done.

__Alternate method:__

- Run the script on the command line.
- A UFO full of Box Drawing Characters is created (given that [FontParts][] is installed and working).




[box]: http://www.unicode.org/charts/PDF/U2500.pdf
[block]: http://www.unicode.org/charts/PDF/U2580.pdf
[xmas]: http://blogs.adobe.com/typblography/files/2012/12/happy-holidays-2012.pdf
[boxwiki]: http://en.wikipedia.org/wiki/Box_drawing_characters
[scp]: https://github.com/adobe/source-code-pro
[robofont]: http://doc.robofont.com/
[glyphs]: http://glyphsapp.com/
[fontlab]: https://www.fontlab.com/font-editor/fontlab-studio-5/
[fontparts]: https://fontparts.robotools.dev/
[robofab]: http://robofab.com
[ufo]: http://unifiedfontobject.org/
[Project Page]: http://adobe-type-tools.github.io/box-drawing/
[objectsGS.py]: https://github.com/schriftgestalt/Glyphs-Scripts/blob/master/objectsGS.py
[GSpen.py]: https://github.com/schriftgestalt/Glyphs-Scripts/blob/master/GSPen.py
