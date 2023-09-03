#This code does 2 general tasks:
#   -Creates 2 halves of a triagle for each of the 3 sides based on the triangles opourtunity to be a hypotenuse on a scrach 3d tri.
#   -Converts those halves into pngs and puts them on warp maps where they can be squashed and stretched by the fisheye block.

#import base 64 converter and os for file management
import base64
import os

#Import svg to png converter
from cairosvg import svg2png


#Suggestion to map your image properly
print ("This ripper is only designed to rip triangles from the bottom right corner of the texture")
print (" _____ ")
print ("|----/|")
print ("|--/  |")
print ("|/Here|")
print (" ~~~~~ ")

#get input image path
input_img_path = input("Paste path to png here: ")
#get output location
Save_to = os.path.normpath(input("Paste path to write data to: "))

#define "get_base64_encoded_image," an image to base 64 converter.
def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

#converts image to base 64
Snip = get_base64_encoded_image(input_img_path)

#creates first parts of svg samples before the base 64
Cut_1 = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100" height="100" viewBox="0,0,100,100"><defs><clipPath id="clip-1"><path d="M240,80v100h-100z" fill="none"/></clipPath></defs><g transform="translate(-140,-80)"><g clip-path="url(#clip-1)" data-paper-data="{&quot;isPaintingLayer&quot;:true}" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" style="mix-blend-mode: normal"><image preserveAspectRatio="none" x="-16" y="-52" transform="rotate(135) scale(7.07107,7.07107)" width="20" height="20" xlink:href="data:image/png;base64,'
Cut_2 = '<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100" height="100" viewBox="0,0,100,100"><defs><clipPath id="clip-1"><path d="M240,80v100h-100z" fill="none"/></clipPath></defs><g transform="translate(-140,-80)"><g clip-path="url(#clip-1)" data-paper-data="{&quot;isPaintingLayer&quot;:true}" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" style="mix-blend-mode: normal"><image preserveAspectRatio="none" x="-52" y="-4" transform="rotate(225) scale(7.07107,7.07107)" width="20" height="20" xlink:href="data:image/png;base64,'
Cut_3 = '<svg version="1.1" width="100" height="100" viewBox="0,0,100,100" id="svg13" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs5"> <clipPath clipPathUnits="userSpaceOnUse" id="clipPath1956"> <path style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M 240,80 140,180 h 100 z" id="path1958" /> </clipPath> <clipPath clipPathUnits="userSpaceOnUse" id="clipPath841"> <path d="M 141.42136,-100 V 0 L 0,100 Z" data-paper-data="{&quot;index&quot;:null}" fill="none" id="path843" style="stroke-width:1.18921" /> </clipPath> <clipPath clipPathUnits="userSpaceOnUse" id="clipPath845"> <path d="M 100,0 V 100 H 0 Z" data-paper-data="{&quot;index&quot;:null}" fill="none" id="path847" /> </clipPath> </defs> <path style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M 99.999996,-3.916725e-6 6.6152202e-7,100 99.999996,99.999996 Z" id="path1985" clip-path="url(#clipPath845)" /> <image width="141.42136" height="200" preserveAspectRatio="none" xlink:href="data:image/png;base64,'
Cut_4 = '<svg version="1.1" width="100" height="100" viewBox="0,0,100,100" id="svg13" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs5"> <clipPath clipPathUnits="userSpaceOnUse" id="clipPath1956"> <path  style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M 240,80 140,180 h 100 z" id="path1958" /> </clipPath> <clipPath clipPathUnits="userSpaceOnUse" id="clipPath841"> <path  d="m 0,-100 141.42136,-100 v 100 z" data-paper-data="{&quot;index&quot;:null}" fill="none" id="path843" clip-path="none" style="stroke-width:1.18921" /> </clipPath> <clipPath clipPathUnits="userSpaceOnUse" id="clipPath845"> <path d="M 100,0 V 100 H 0 Z" data-paper-data="{&quot;index&quot;:null}" fill="none" id="path847" clip-path="none" /> </clipPath> </defs> <path style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M 100,-3.6625976e-6 1.1697768e-6,99.999999 H 100 Z" id="path1962" clip-path="url(#clipPath845)" /> <image width="141.42136" height="200" preserveAspectRatio="none" xlink:href="data:image/png;base64,'
Cut_5 = '<svg version="1.1" width="100" height="100" viewBox="0,0,100,100" id="svg13" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs5"> <clipPath id="clip-1"> <path d="M190,130.000000l0,100-100,0z" data-paper-data="{&quot;index&quot;:null}" fill="none" id="path2" /> </clipPath> <clipPath clipPathUnits="userSpaceOnUse" id="clipPath1593"> <path style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.18921px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M 99.999999,0 -99.999996,141.42135 H 2.8284271e-6 Z" id="path1595" /> </clipPath> </defs> <image width="200" height="141.42136" preserveAspectRatio="none" xlink:href="data:image/png;base64,'
Cut_6 = '<svg version="1.1" width="100" height="100" viewBox="0,0,100,100" id="svg13" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <defs id="defs5"> <clipPath id="clip-1"> <path d="M190,130.000000l0,100-100,0z" data-paper-data="{&quot;index&quot;:null}" fill="none" id="path2" /> </clipPath> <clipPath clipPathUnits="userSpaceOnUse" id="clipPath1606"> <path style="fill:#000000;fill-opacity:1;stroke:none;stroke-width:1.18921px;stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1" d="M -99.999996,141.42135 -99.999995,-2.8177646e-6 -199.99999,141.42135 Z" id="path1608" /> </clipPath> </defs> <image width="200" height="141.42136" preserveAspectRatio="none" xlink:href="data:image/png;base64,'

#creates last parts of svg samples after the base 64
End = '" fill="#000000"/></g></g></svg>'
End3 = '" x="0" y="-100" transform="matrix(0.70710678,0.70710678,0,1,0,0)" clip-path="url(#clipPath841)" id="image7" /></svg>'
End4 = '" x="-2.1875772e-07" y="-300" transform="matrix(-0.70710678,0.70710678,-1,0,0,0)" clip-path="url(#clipPath841)" id="image7" /> </svg>'
End5 = '" x="-100" y="0" transform="matrix(1,0,0.70710677,0.70710679,0,0)" clip-path="url(#clipPath1593)" /></svg>'
End6 = '" x="-300" y="-2.8177647e-06" transform="matrix(0,-1,0.70710679,-0.70710677,0,0)" clip-path="url(#clipPath1606)" /> </svg>'

#Sandwhiches the code together which sould create 6 right triangles
Sample_1 = ''.join([Cut_1, Snip, End])
Sample_2 = ''.join([Cut_2, Snip, End])
Sample_3 = ''.join([Cut_3, Snip, End3])
Sample_4 = ''.join([Cut_4, Snip, End4])
Sample_5 = ''.join([Cut_6, Snip, End6])
Sample_6 = ''.join([Cut_5, Snip, End5])

#Sets output
Filename=os.path.basename(os.path.splitext(input_img_path)[0])
Outname = ''.join([Save_to, '/', Filename])

#Converts svg to png
svg2png(bytestring=Sample_1,write_to=''.join([Outname,'1.png']))
svg2png(bytestring=Sample_2,write_to=''.join([Outname,'2.png']))
svg2png(bytestring=Sample_3,write_to=''.join([Outname,'3.png']))
svg2png(bytestring=Sample_4,write_to=''.join([Outname,'4.png']))
svg2png(bytestring=Sample_5,write_to=''.join([Outname,'5.png']))
svg2png(bytestring=Sample_6,write_to=''.join([Outname,'6.png']))

#creating templates for fisheye warping.
Tri_half_a = '<svg viewBox="0,0,480,360" version="1.1" id="svg1448" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg"> <rect style="fill:#d40000;fill-opacity:0;stroke-width:0" id="rect1531" width="438" height="70" x="41" y="45" /> <image transform="scale(0.2,0.2)" width="100" height="100" preserveAspectRatio="none" xlink:href="data:image/png;base64,'
Tri_half_b = '<svg viewBox="0,0,480,360" version="1.1" id="svg1448" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"> <rect style="fill:#d40000;fill-opacity:0;stroke-width:0" id="rect1531" width="438" height="70" x="41" y="-315" transform="scale(1,-1)" /> <image width="100" height="100" preserveAspectRatio="none" xlink:href="data:image/png;base64,'

Tri_half_a_end ='" x="1200" y="800" /> </svg>'
Tri_half_b_end ='" x="-1000" y="1200" transform="rotate(-90) scale(0.2,0.2)" /> </svg>'


#get base 64 of converted right triangle "1.png" and output vectors
Snip = get_base64_encoded_image(''.join([Outname,'1.png']))

Output = open(''.join([Outname,'_A.svg']), 'w')
Output.write(''.join([Tri_half_a, Snip, Tri_half_a_end]))
Output.close()
Output = open(''.join([Outname,'_B.svg']), 'w')
Output.write(''.join([Tri_half_b, Snip, Tri_half_b_end]))
Output.close()

#get base 64 of converted right triangle "2.png" and output vectors
Snip = get_base64_encoded_image(''.join([Outname,'2.png']))

Output = open(''.join([Outname,'_C.svg']), 'w')
Output.write(''.join([Tri_half_a, Snip, Tri_half_a_end]))
Output.close()
Output = open(''.join([Outname,'_D.svg']), 'w')
Output.write(''.join([Tri_half_b, Snip, Tri_half_b_end]))
Output.close()

#get base 64 of converted right triangle "3.png" and output vectors
Snip = get_base64_encoded_image(''.join([Outname,'3.png']))

Output = open(''.join([Outname,'_E.svg']), 'w')
Output.write(''.join([Tri_half_a, Snip, Tri_half_a_end]))
Output.close()
Output = open(''.join([Outname,'_F.svg']), 'w')
Output.write(''.join([Tri_half_b, Snip, Tri_half_b_end]))
Output.close()

#get base 64 of converted right triangle "4.png" and output vectors
Snip = get_base64_encoded_image(''.join([Outname,'4.png']))

Output = open(''.join([Outname,'_G.svg']), 'w')
Output.write(''.join([Tri_half_a, Snip, Tri_half_a_end]))
Output.close()
Output = open(''.join([Outname,'_H.svg']), 'w')
Output.write(''.join([Tri_half_b, Snip, Tri_half_b_end]))
Output.close()

#get base 64 of converted right triangle "5.png" and output vectors
Snip = get_base64_encoded_image(''.join([Outname,'5.png']))

Output = open(''.join([Outname,'_I.svg']), 'w')
Output.write(''.join([Tri_half_a, Snip, Tri_half_a_end]))
Output.close()
Output = open(''.join([Outname,'_J.svg']), 'w')
Output.write(''.join([Tri_half_b, Snip, Tri_half_b_end]))
Output.close()

#get base 64 of converted right triangle "6.png" and output vectors
Snip = get_base64_encoded_image(''.join([Outname,'6.png']))

Output = open(''.join([Outname,'_K.svg']), 'w')
Output.write(''.join([Tri_half_a, Snip, Tri_half_a_end]))
Output.close()
Output = open(''.join([Outname,'_L.svg']), 'w')
Output.write(''.join([Tri_half_b, Snip, Tri_half_b_end]))
Output.close()
