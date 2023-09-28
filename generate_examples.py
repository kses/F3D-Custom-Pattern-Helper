import patterns

calibers = [
    ["100mm", 120],
    ["100mm_dense", 240],
    ["125mm", 140],
    ["125mm_dense", 280],
    ["150mm", 160],
    ["150mm_dense", 320],
    ["175mm", 180],
    ["175mm_dense", 360],
]

#Quarter Peony
for cal in calibers:
    with open('examples/'+cal[0]+'_quarter_peony.txt', 'w') as f:
        f.write(str(patterns.azimuth_slices(cal[1],4,0)))


#Ghosting Bands
for cal in calibers:
    with open('examples/'+cal[0]+'_4_ghost_bands.txt', 'w') as f:
        f.write(str(patterns.cartesian_bands(cal[1],4,0.2)))

#Six sections
for cal in calibers:
    with open('examples/'+cal[0]+'_6_sections.txt', 'w') as f:
        f.write(str(patterns.six_sections(cal[1],0)))
