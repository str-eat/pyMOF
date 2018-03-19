'''
Created on Mar 5, 2018

@author: danie
'''
"""
    
"""
import os       
                  
#===============================================================================
# General csv format
# symmetry_space_group_name, value
# cell_length_a, value
# cell_length_b, value       
# cell_length_c, value
# cell_angle_alpha, value
# cell_angle_beta, value
# cell_angle_gamma, value
# symmetry_int_tables_number, value
# chemical_formula_structural, value
# chemical_formula_sum, value
# cell_volume, value
# cell_formula_units, value
# symmetry_equiv_pos_site_id, value
# symmetry_equiv_pos_as_xyz, value
# atom_site_type_symbol, atom_site_fract_x, atom_site_fract_y, atom_site_fract_z, atom_site_charge
# value, value, value, value, value
# value, value, value, value, value
#===============================================================================

filename = os.path.join(os.getcwd(), '..\\datasets\\cifs\\')
output = os.path.join(filename, '..\\..\\cifs_file.csv')

with open(output, 'w') as output:
    for i, each in enumerate(os.listdir(filename)):
        with open(filename + each, 'r') as file:
            for line in file:
                if line[0:1] == '_':
                    i = 0
                    while line[i] != "\n":
                        if line[i] == " ":
                            output.write("," + line[i+3 : line.length])
                        else:
                            output.write(line[i])
                        i = i + 1
                #file.seek[0]
                    
    