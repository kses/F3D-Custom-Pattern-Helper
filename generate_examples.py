import patterns


#Quarter Peony
with open('examples/100mm_quarter_peony.txt', 'w') as f:
    f.write(str(patterns.azimuth_slices(120,4,0)))
with open('examples/100mm_dense_quarter_peony.txt', 'w') as f:
    f.write(str(patterns.azimuth_slices(240,4,0)))
    
with open('examples/125mm_quarter_peony.txt', 'w') as f:
    f.write(str(patterns.azimuth_slices(140,4,0)))
with open('examples/125mm_dense_quarter_peony.txt', 'w') as f:
    f.write(str(patterns.azimuth_slices(280,4,0)))

with open('examples/150mm_quarter_peony.txt', 'w') as f:
    f.write(str(patterns.azimuth_slices(160,4,0)))
with open('examples/150mm_dense_quarter_peony.txt', 'w') as f:
    f.write(str(patterns.azimuth_slices(320,4,0)))
    
with open('examples/175mm_quarter_peony.txt', 'w') as f:
    f.write(str(patterns.azimuth_slices(180,4,0)))
with open('examples/175mm_dense_quarter_peony.txt', 'w') as f:
    f.write(str(patterns.azimuth_slices(360,4,0)))
    
#4 Ghosting Bands Peony
with open('examples/100mm_4_ghost_bands.txt', 'w') as f:
    f.write(str(patterns.cartesian_bands(120,4,0.2)))
with open('examples/100mm_dense_4_ghost_bands.txt', 'w') as f:
    f.write(str(patterns.cartesian_bands(240,4,0.2)))
    
with open('examples/125mm_4_ghost_bands.txt', 'w') as f:
    f.write(str(patterns.cartesian_bands(140,4,0.2)))
with open('examples/125mm_dense_4_ghost_bands.txt', 'w') as f:
    f.write(str(patterns.cartesian_bands(280,4,0.2)))

with open('examples/150mm_4_ghost_bands.txt', 'w') as f:
    f.write(str(patterns.cartesian_bands(160,4,0.2)))
with open('examples/150mm_dense_4_ghost_bands.txt', 'w') as f:
    f.write(str(patterns.cartesian_bands(320,4,0.2)))
    
with open('examples/175mm_4_ghost_bands.txt', 'w') as f:
    f.write(str(patterns.cartesian_bands(180,4,0.2)))
with open('examples/175mm_dense_4_ghost_bands.txt', 'w') as f:
    f.write(str(patterns.cartesian_bands(360,4,0.2)))

#6 sections Peony
with open('examples/100mm_6_sections.txt', 'w') as f:
    f.write(str(patterns.six_sections(120,0)))
with open('examples/100mm_dense_6_sections.txt', 'w') as f:
    f.write(str(patterns.six_sections(240,0)))
    
with open('examples/125mm_6_sections.txt', 'w') as f:
    f.write(str(patterns.six_sections(140,0)))
with open('examples/125mm_dense_6_sections.txt', 'w') as f:
    f.write(str(patterns.six_sections(280,0)))

with open('examples/150mm_6_sections.txt', 'w') as f:
    f.write(str(patterns.six_sections(160,0)))
with open('examples/150mm_dense_6_sections.txt', 'w') as f:
    f.write(str(patterns.six_sections(320,0)))
    
with open('examples/175mm_6_sections.txt', 'w') as f:
    f.write(str(patterns.six_sections(180,0)))
with open('examples/175mm_dense_6_sections.txt', 'w') as f:
    f.write(str(patterns.six_sections(360,0)))
    