# Scratch-Texture-Mapper
A png ripper for the Textured Polys Framework on scratch.


This is a texture mapper used for ripping images from pngs to be used in the Textured Polys Framework.

Instructions for use:
 You'll be prompted about the texture reading limitations follow by a request for the png file path, followed by an output path.

Requirements:
-Python 3.6+
-CairoSVG

Limits (may be fixed at a later date):
 -You can only rip one texture at a time
 -Only the left half of the image will get ripped. You'll have to turn the image 180 degrees to rip the other half.
 -Only PNG format's have been tested right now.
 
 ==============================
 ||XXXXXXXXXXXXXXXXXXXXXXXXXX||
 ||XXXXXXXXXXXXXXXXXXXXXXXX/ ||
 ||XXXXXXXXXXXXXXXXXXXXX/    ||
 ||XXXXXXXXXXXXXXXXXX/       ||
 ||XXXXXXXXXXXXXXX/          ||
 ||XXXXXXXXXXXX/             ||
 ||XXXXXXXXX/                ||
 ||XXXXXX/   Only this half  ||
 ||XXX/         is read      ||
 ||/                         ||
 ==============================
