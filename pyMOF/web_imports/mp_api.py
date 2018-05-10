import pymatgen as pmg
from pymatgen import MPRester as mpr
from pymatgen.analysis.phase_diagram import PhaseDiagram as phd, PDPlotter as pdp

import matplotlib.pyplot as plt
import matplotlib as mpl


si = pmg.Element("C")
print(si.atomic_mass)
formula = ''
property = ''

# GET method API calls
MATERIALS_CALCULATED_BASE_URL = "https://www.materialsproject.org/rest/v2/materials/{formula}/vasp/{property}".format(formula, property) 
MATERIALS_EXPERIMENTAL_BASE_URL = "https://www.materialsproject.org/rest/v2/materials/{formula}/exp".format(formula)
TASKS_CALCULATION_BASE_URL = "https://www.materialsproject.org/rest/v2/materials/{formula}/exp".format(formula)
MATERIAL_ID_BASE_URL = "https://www.materialsproject.org/rest/v2/materials/{formula}/mids".format(formula)

# POST method API calls
MPQUERY_BASE_URL = "https://www.materialsproject.org/rest/v2/query"

API_KEY = input("Please enter your API Key here:")



