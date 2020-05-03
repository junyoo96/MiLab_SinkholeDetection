from Box import Box
from Domain import Domain
from Dx_Dy_Dz import Dx_Dy_Dz
from Geometry_View import Geometry_View
from Hertzian_Dipole import Hertzian_Dipole
from Material import Material
from Rx import Rx
from Rx_Steps import Rx_Steps
from SRC_Steps import SRC_Steps
from Sphere import Sphere
from Cylinder import Cylinder
from Time_Window import Time_Window
from Title import Title
from Utility import Utility
from Waveform import Waveform


import sys
import os.path
# Underground Object Generation File

UNDERGROUND_OBJECT_TYPE = None
# =================================================================
# parameters
# ================================================================
# titie parameter
TITLE = None

# ================================================================
#dielectric smoothing
DIELECTRIC_SMOOTHING_ACTIVATION_YES="y"
DIELECTRIC_SMOOTHING_ACTIVATION_NO="n"

# ================================================================
# domain parameter
# 지하가 시작되는 지점(높이)
DOMAIN_Z_UNDERGROUND_START = 1
# 안테나 띄울 공간 얼마나 확보할지
DOMAIN_Z_FREESPACE_OFFSET = 0.1

DOMAIN_X = 0.6
DOMAIN_Y = 0.6
DOMAIN_Z = DOMAIN_Z_UNDERGROUND_START + DOMAIN_Z_FREESPACE_OFFSET  # 1m + 0.1m(지표면에서 안테나 살짝 띄울공간 확보)

# ================================================================
# dx_dy_dz parameter
DX_DY_DZ_X = 0.002
DX_DY_DZ_Y = 0.002
DX_DY_DZ_Z = 0.002

# ================================================================
# time window
TIME_WINDOW = "15e-9"

# ================================================================
##material
# free_space
MATERIAL_FREESPACE_IDENTIFIER = "free_space"

# ================================================================
##material
# soil
MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN = 10
MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX = 10

MATERIAL_SOIL_CONDUCTIVITY_MIN = 0.01
MATERIAL_SOIL_CONDUCTIVITY_MAX = 0.01

MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN = 1
MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX = 1

MATERIAL_SOIL_MAGNETIC_LOSS_MIN = 0
MATERIAL_SOIL_MAGNETIC_LOSS_MAX = 0

MATERIAL_SOIL_IDENTIFIER = "soil"

# ================================================================
##material
# asphalt
MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MIN = 4
MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MAX = 7

MATERIAL_ASPHALT_CONDUCTIVITY_MIN = 0.02
MATERIAL_ASPHALT_CONDUCTIVITY_MAX = 0.02

MATERIAL_ASPHALT_RELATIVE_PERMEABILITY_MIN = 1
MATERIAL_ASPHALT_RELATIVE_PERMEABILITY_MAX = 1

MATERIAL_ASPHALT_MAGNETIC_LOSS_MIN = 0
MATERIAL_ASPHALT_MAGNETIC_LOSS_MAX = 0

MATERIAL_ASPHALT_IDENTIFIER = "asphalt"

# ================================================================
##material
# water
MATERIAL_WATER_RELATIVE_PERMITTIVITY_MIN = 80
MATERIAL_WATER_RELATIVE_PERMITTIVITY_MAX = 80

MATERIAL_WATER_CONDUCTIVITY_MIN = 0.05
MATERIAL_WATER_CONDUCTIVITY_MAX = 0.05

MATERIAL_WATER_RELATIVE_PERMEABILITY_MIN = 1
MATERIAL_WATER_RELATIVE_PERMEABILITY_MAX = 1

MATERIAL_WATER_MAGNETIC_LOSS_MIN = 0
MATERIAL_WATER_MAGNETIC_LOSS_MAX = 0

MATERIAL_WATER_IDENTIFIER = "water"

# ================================================================
# waveform

WAVEFORM_TYPE = "ricker"

WAVEFORM_MAX_AMPLITUDE_MIN = 1
WAVEFORM_MAX_AMPLITUDE_MAX = 1

WAVEFORM_CENTER_FREQUENCY_MIN = 0.2
WAVEFORM_CENTER_FREQUENCY_MAX = 0.8

WAVEFORM_IDENTIFIER = "my_pulse"

# ================================================================
# hertzian_dipole
# 지표면에서 안테나 얼마나 띄울지
ANTENNA_HEIGHT_OFFSET = 0.05  # Don't use offset! It makes antenna figure disappear
# PML에 안테나가 붙어었으면 안되서 좀 떨어뜨리기 위한 offset
ANTENNA_Y_OFFSET = 0.25

HERTZIAN_DIPOLE_SOURCE_POLARISATION = "x"
HERTZIAN_DIPOLE_SOURCE_X = DOMAIN_X / 2
HERTZIAN_DIPOLE_SOURCE_Y = 0 + ANTENNA_Y_OFFSET
HERTZIAN_DIPOLE_SOURCE_Z = DOMAIN_Z_UNDERGROUND_START + ANTENNA_HEIGHT_OFFSET
HERTZIAN_DIPOLE_SOURCE_IDENTIFIER = "my_pulse"
# 예외처리
# offset처리

# ================================================================
# src_steps
# src_steps must not be lower than dx_dy_dz value!!!

SRC_STEPS_X = 0
SRC_STEPS_Y = 0.01
SRC_STEPS_Z = 0

# 예외처리
# ================================================================
# rx(Reciever 좌표)
SOURCE_RECEIVER_BETWEEN_OFFSET = 0.05

RX_X = HERTZIAN_DIPOLE_SOURCE_X
RX_Y = HERTZIAN_DIPOLE_SOURCE_Y + SOURCE_RECEIVER_BETWEEN_OFFSET
RX_Z = HERTZIAN_DIPOLE_SOURCE_Z

# 예외처리
# ================================================================
# rx_steps
RX_STEPS_X = SRC_STEPS_X
RX_STEPS_Y = SRC_STEPS_Y
RX_STEPS_Z = SRC_STEPS_Z

# 예외처리

# ================================================================
##box(asphalt area)
# box low coordinate
ASPHALT_THICKNESS = 0.2

ASPHALT_BOX_LOWER_LEFT_X = 0
ASPHALT_BOX_LOWER_LEFT_Y = 0
ASPHALT_BOX_LOWER_LEFT_Z = DOMAIN_Z_UNDERGROUND_START - ASPHALT_THICKNESS

# box high coordinate
ASPHALT_BOX_HIGHER_RIGHT_X = DOMAIN_X
ASPHALT_BOX_HIGHER_RIGHT_Y = DOMAIN_Y
ASPHALT_BOX_HIGHER_RIGHT_Z = DOMAIN_Z_UNDERGROUND_START

# box material
ASPHALT_BOX_MATERIAL_IDENTIFIER = "asphalt"

# dielectric smoothing activation
ASPHALT_BOX_DIELECTRIC_SMOOTHING_ACTIVATION = "n"

# ================================================================
##box(soil area)
# box low coordinate
BOX_LOWER_LEFT_X = 0
BOX_LOWER_LEFT_Y = 0
BOX_LOWER_LEFT_Z = 0

# box high coordinate
BOX_HIGHER_RIGHT_X = DOMAIN_X
BOX_HIGHER_RIGHT_Y = DOMAIN_Y
BOX_HIGHER_RIGHT_Z = ASPHALT_BOX_LOWER_LEFT_Z

# box material
BOX_MATERIAL_IDENTIFIER = "soil"

# dielectric smoothing activation
BOX_DIELECTRIC_SMOOTHING_ACTIVATION = "n"

# 예외처리


# ================================================================
##sphere(cavity)

SPHERE_MOVING_OFFSET = 0.05

# sphere coordinate
SPHERE_X_MIN = DOMAIN_X / 2 - SPHERE_MOVING_OFFSET
SPHERE_X_MAX = DOMAIN_X / 2 + SPHERE_MOVING_OFFSET
SPHERE_Y_MIN = DOMAIN_Y / 2 - SPHERE_MOVING_OFFSET
SPHERE_Y_MAX = DOMAIN_Y / 2 + SPHERE_MOVING_OFFSET
SPHERE_Z_MIN = BOX_HIGHER_RIGHT_Z / 2 - SPHERE_MOVING_OFFSET
SPHERE_Z_MAX = BOX_HIGHER_RIGHT_Z / 2 + SPHERE_MOVING_OFFSET

# sphere radius
SPHERE_RADIUS_MIN = 0.1
# 수정해야함
SPHERE_RADIUS_MAX = 0.1

# sphere material
SPHERE_MATERIAL = "free_space"

# dielectric smoothing activation
SPHERE_DIELECTRIC_SMOOTHING_ACTIVATION = "y"



# ================================================================
# geometry_view(모델의 기하학적인 정보를 file형태로 출력하게 하는 명령어)
# geometry low coordinate
GEOMETRY_VIEW_LOWER_LEFT_X = 0
GEOMETRY_VIEW_LOWER_LEFT_Y = 0
GEOMETRY_VIEW_LOWER_LEFT_Z = 0

# geometry high coordinate
GEOMETRY_VIEW_HIGHER_RIGHT_X = DOMAIN_X
GEOMETRY_VIEW_HIGHER_RIGHT_Y = DOMAIN_Y
GEOMETRY_VIEW_HIGHER_RIGHT_Z = DOMAIN_Z

# geometry dx_dy_dz
GEOMETRY_VIEW_DX = DX_DY_DZ_X
GEOMETRY_VIEW_DY = DX_DY_DZ_Y
GEOMETRY_VIEW_DZ = DX_DY_DZ_Z

# input file과 동일한 경로에 저장될 geometry view의 file이름 설정
GEOMETRY_VIEW_FILENAME = None
# ================================================================
# ================================================================
##Generation Code
# ================================================================

textfile = None
utility=Utility()

def generate_title():
    # title
    title=Title(TITLE)
    title.write_textfile(textfile)

def generate_domain(): ##여기서부터 이어서 시작
    # domain
    domain = Domain(DOMAIN_X,DOMAIN_Y,DOMAIN_Z)
    domain.write_textfile(textfile)

def generate_dx_dz_dy():
    # dx_dy_dz
    dx_dy_dz = Dx_Dy_Dz(DX_DY_DZ_X,DX_DY_DZ_Y,DX_DY_DZ_Z)
    dx_dy_dz.write_textfile(textfile)

def generate_time_window():
    # time_window
    time_window = Time_Window(TIME_WINDOW)
    time_window.write_textfile(textfile)

def generate_material_soil():
    # relative permittivity

    material_soil=Material(
        utility.random_sampling(MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN,MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX),
        utility.random_sampling(MATERIAL_SOIL_CONDUCTIVITY_MIN, MATERIAL_SOIL_CONDUCTIVITY_MAX),
        utility.random_sampling(MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN, MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX),
        utility.random_sampling(MATERIAL_SOIL_MAGNETIC_LOSS_MIN, MATERIAL_SOIL_MAGNETIC_LOSS_MAX),
        MATERIAL_SOIL_IDENTIFIER
    )

    material_soil.write_textfile(textfile)

def generate_material_asphalt():

    material_asphalt = Material(
        utility.random_sampling(MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MIN,MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MAX),
        utility.random_sampling(MATERIAL_ASPHALT_CONDUCTIVITY_MIN, MATERIAL_ASPHALT_CONDUCTIVITY_MAX),
        utility.random_sampling(MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN, MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX),
        utility.random_sampling(MATERIAL_SOIL_MAGNETIC_LOSS_MIN, MATERIAL_SOIL_MAGNETIC_LOSS_MAX),
        MATERIAL_ASPHALT_IDENTIFIER
    )

    material_asphalt.write_textfile(textfile)

def generate_material_water():
    material_water = Material(
        utility.random_sampling(MATERIAL_WATER_RELATIVE_PERMITTIVITY_MIN,MATERIAL_WATER_RELATIVE_PERMITTIVITY_MAX),
        utility.random_sampling(MATERIAL_WATER_CONDUCTIVITY_MIN, MATERIAL_WATER_CONDUCTIVITY_MAX),
        utility.random_sampling(MATERIAL_WATER_RELATIVE_PERMEABILITY_MIN,MATERIAL_WATER_RELATIVE_PERMEABILITY_MAX),
        utility.random_sampling(MATERIAL_WATER_MAGNETIC_LOSS_MIN, MATERIAL_WATER_MAGNETIC_LOSS_MAX),
        MATERIAL_WATER_IDENTIFIER
    )

    material_water.write_textfile(textfile)

def generate_waveform():

    waveform=Waveform(
        WAVEFORM_TYPE,
        utility.random_sampling(WAVEFORM_MAX_AMPLITUDE_MIN, WAVEFORM_MAX_AMPLITUDE_MAX),
        utility.random_sampling(WAVEFORM_CENTER_FREQUENCY_MIN, WAVEFORM_CENTER_FREQUENCY_MAX),
        WAVEFORM_IDENTIFIER
    )

    waveform.write_textfile(textfile)

def generate_hertzian_dipole():

    hertzian_dipole=Hertzian_Dipole(
        HERTZIAN_DIPOLE_SOURCE_POLARISATION,
        HERTZIAN_DIPOLE_SOURCE_X,
        HERTZIAN_DIPOLE_SOURCE_Y,
        HERTZIAN_DIPOLE_SOURCE_Z,
        HERTZIAN_DIPOLE_SOURCE_IDENTIFIER
    )

    hertzian_dipole.write_textfile(textfile)

def generate_rx():

    rx=Rx(
        RX_X,
        RX_Y,
        RX_Z
    )

    rx.write_textfile(textfile)

def generate_src_steps():

    src_steps=SRC_Steps(
        SRC_STEPS_X,
        SRC_STEPS_Y,
        SRC_STEPS_Z
    )

    src_steps.write_textfile(textfile)

def generate_rx_steps():

    rx_steps=Rx_Steps(
       RX_STEPS_X,
       RX_STEPS_Y,
       RX_STEPS_Z
    )

    rx_steps.write_textfile(textfile)

def generate_soil_box():

    soil_box=Box(
        BOX_LOWER_LEFT_X,
        BOX_LOWER_LEFT_Y,
        BOX_LOWER_LEFT_Z,
        BOX_HIGHER_RIGHT_X,
        BOX_HIGHER_RIGHT_Y,
        BOX_HIGHER_RIGHT_Z,
        BOX_MATERIAL_IDENTIFIER,
        BOX_DIELECTRIC_SMOOTHING_ACTIVATION
    )

    soil_box.write_textfile(textfile)

def generate_asphalt_box():

   asphalt_box=Box(
       ASPHALT_BOX_LOWER_LEFT_X,
       ASPHALT_BOX_LOWER_LEFT_Y,
       ASPHALT_BOX_LOWER_LEFT_Z,
       ASPHALT_BOX_HIGHER_RIGHT_X,
       ASPHALT_BOX_HIGHER_RIGHT_Y,
       ASPHALT_BOX_HIGHER_RIGHT_Z,
       ASPHALT_BOX_MATERIAL_IDENTIFIER,
       ASPHALT_BOX_DIELECTRIC_SMOOTHING_ACTIVATION
   )

   asphalt_box.write_textfile(textfile)

#generate cavity by shape of sphere
def generate_cavity_sphere(water=False):

    if water == False:
        sphere_material = MATERIAL_FREESPACE_IDENTIFIER
    else:
        sphere_material = MATERIAL_WATER_IDENTIFIER

    if water == False:
        sphere_dielectric_smoothing_activation = SPHERE_DIELECTRIC_SMOOTHING_ACTIVATION
    else:
        sphere_dielectric_smoothing_activation = "n"

    cavity_sphere=Sphere(
        utility.random_sampling(SPHERE_X_MIN, SPHERE_X_MAX),
        utility.random_sampling(SPHERE_Y_MIN, SPHERE_Y_MAX),
        utility.random_sampling(SPHERE_Z_MIN, SPHERE_Z_MAX),
        utility.random_sampling(SPHERE_RADIUS_MIN, SPHERE_RADIUS_MAX),
        sphere_material,
        sphere_dielectric_smoothing_activation
    )

    cavity_sphere.write_textfile(textfile)

#generate cavity by shape of cylinder
def generate_cavity_cylinder(water=False, water_portion=0.5):

    MINIMUM_CAVITY_CYLINDER_END_RADIUS=0.01 #1

    cavity_lower_x_determined=utility.random_sampling(SPHERE_X_MIN, SPHERE_X_MAX)
    cavity_lower_y_determined=utility.random_sampling(SPHERE_Y_MIN, SPHERE_Y_MAX)
    cavity_radius_determined = utility.random_sampling(SPHERE_RADIUS_MIN, SPHERE_RADIUS_MAX)
    cavity_lower_z_determined = utility.random_sampling(SPHERE_Z_MIN, SPHERE_Z_MAX)-cavity_radius_determined

    to_generate_cylinder_num=int(cavity_radius_determined/(cavity_radius_determined/MINIMUM_CAVITY_CYLINDER_END_RADIUS))*2-1
    height_per_cylinder=cavity_radius_determined*2/to_generate_cylinder_num

    to_genearte_cylinder_with_water_portion_num=int(to_generate_cylinder_num/water_portion)

    current_cylinder_lower_x=cavity_lower_x_determined
    current_cylinder_lower_y= cavity_lower_y_determined
    current_cylinder_lower_z = cavity_lower_z_determined
    # current_cylinder_higher_x=cavity_lower_x_determined
    # current_cylinder_higher_y = cavity_lower_y_determined
    current_cylinder_higher_z = cavity_lower_z_determined+height_per_cylinder
    current_cylinder_radius=MINIMUM_CAVITY_CYLINDER_END_RADIUS
    current_material_identifier=None
    current_dielectric_smoothing_activation = None

    for i in range(1,to_generate_cylinder_num+1):

        if i<=to_genearte_cylinder_with_water_portion_num:
            current_material_identifier = MATERIAL_WATER_IDENTIFIER
            current_dielectric_smoothing_activation=DIELECTRIC_SMOOTHING_ACTIVATION_NO
        else:
            current_material_identifier = MATERIAL_FREESPACE_IDENTIFIER
            current_dielectric_smoothing_activation = DIELECTRIC_SMOOTHING_ACTIVATION_YES

        cavity_cylinder=Cylinder(
            current_cylinder_lower_x,
            current_cylinder_lower_y,
            current_cylinder_lower_z,
            current_cylinder_lower_x,
            current_cylinder_lower_y,
            current_cylinder_lower_z+height_per_cylinder,
            current_cylinder_radius,
            current_material_identifier,
            current_dielectric_smoothing_activation
        )

        cavity_cylinder.write_textfile(textfile)

        current_cylinder_lower_z +=height_per_cylinder

        if i<to_generate_cylinder_num/2+1:
            current_cylinder_radius+=MINIMUM_CAVITY_CYLINDER_END_RADIUS
        else:
            current_cylinder_radius -= MINIMUM_CAVITY_CYLINDER_END_RADIUS

def generate_geometry_view(iteration_index):
    GEOMETRY_VIEW_FILENAME = "%s_%d_" % (UNDERGROUND_OBJECT_TYPE, iteration_index)

    geometry_view=Geometry_View(
        GEOMETRY_VIEW_LOWER_LEFT_X,
        GEOMETRY_VIEW_LOWER_LEFT_Y,
        GEOMETRY_VIEW_LOWER_LEFT_Z,
        GEOMETRY_VIEW_HIGHER_RIGHT_X,
        GEOMETRY_VIEW_HIGHER_RIGHT_Y,
        GEOMETRY_VIEW_HIGHER_RIGHT_Z,
        GEOMETRY_VIEW_DX,
        GEOMETRY_VIEW_DY,
        GEOMETRY_VIEW_DZ,
        GEOMETRY_VIEW_FILENAME
    )

    geometry_view.write_textfile(textfile)

# ================================================================
def check_parameter_range():
    print("Check Parameters...")

    wrong_parameter_list = ""

    try:
        # Material
        if MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN > MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX:
            wrong_parameter_list += f"MATERIAL_SOIL_RELATIVE_PERMITTIVITY: ({MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN},{MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX})\n"
        if MATERIAL_SOIL_CONDUCTIVITY_MIN > MATERIAL_SOIL_CONDUCTIVITY_MAX:
            wrong_parameter_list += f"MATERIAL_SOIL_CONDUCTIVITY: ({MATERIAL_SOIL_CONDUCTIVITY_MIN},{MATERIAL_SOIL_CONDUCTIVITY_MAX})\n"
        if MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN > MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX:
            wrong_parameter_list += f"MATERIAL_SOIL_RELATIVE_PERMEABILITY: ({MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN},{MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX})\n"
        if MATERIAL_SOIL_MAGNETIC_LOSS_MIN > MATERIAL_SOIL_MAGNETIC_LOSS_MAX:
            wrong_parameter_list += f"MATERIAL_SOIL_MAGNETIC_LOSS: ({MATERIAL_SOIL_MAGNETIC_LOSS_MIN},{MATERIAL_SOIL_MAGNETIC_LOSS_MAX})\n"

        # waveform
        if HERTZIAN_DIPOLE_SOURCE_X > DOMAIN_X:
            wrong_parameter_list += f"HERTZIAN_DIPOLE_SOURCE_X : {HERTZIAN_DIPOLE_SOURCE_X},DOMAIN_X : {DOMAIN_X})\n"
        if HERTZIAN_DIPOLE_SOURCE_Y > DOMAIN_Y:
            wrong_parameter_list += f"HERTZIAN_DIPOLE_SOURCE_Y :{HERTZIAN_DIPOLE_SOURCE_Y},DOMAIN_Y : {DOMAIN_Y})\n"
        if HERTZIAN_DIPOLE_SOURCE_X > DOMAIN_X:
            wrong_parameter_list += f"HERTZIAN_DIPOLE_SOURCE_Z :{HERTZIAN_DIPOLE_SOURCE_Z},DOMAIN_Z : {DOMAIN_Z})\n"

        # rx
        if RX_X > DOMAIN_X:
            wrong_parameter_list += f"RX_X:{RX_X},DOMAIN_X : {DOMAIN_X}\n"
        if RX_Y > DOMAIN_Y:
            wrong_parameter_list += f"RX_Y:{RX_Y},DOMAIN_Y : {DOMAIN_Y}\n"
        if RX_Z > DOMAIN_Z:
            wrong_parameter_list += f"RX_Z:{RX_Z},DOMAIN_Z : {DOMAIN_Z}\n"

        # src_steps
        if SRC_STEPS_X > DOMAIN_X:
            wrong_parameter_list += f"SRC_STEPS_X:{SRC_STEPS_X},DOMAIN_X : {DOMAIN_X}\n"
        if SRC_STEPS_Y > DOMAIN_Y:
            wrong_parameter_list += f"SRC_STEPS_Y:{SRC_STEPS_Y},DOMAIN_Y : {DOMAIN_Y}\n"
        if SRC_STEPS_Z > DOMAIN_Z:
            wrong_parameter_list += f":SRC_STEPS_Z:{SRC_STEPS_Z},DOMAIN_Z : {DOMAIN_Z}\n"

        # rx_steps
        if RX_STEPS_X > DOMAIN_X:
            wrong_parameter_list += f":RX_STEPS_X:{RX_STEPS_X},DOMAIN_X : {DOMAIN_X}\n"
        if RX_STEPS_Y > DOMAIN_Y:
            wrong_parameter_list += f":RX_STEPS_Y:{RX_STEPS_Y},DOMAIN_Y : {DOMAIN_Y}\n"
        if RX_STEPS_Z > DOMAIN_Z:
            wrong_parameter_list += f":RX_STEPS_Z:{RX_STEPS_Z},DOMAIN_Z : {DOMAIN_Z}\n"

        # box
        if BOX_HIGHER_RIGHT_X > DOMAIN_X:
            wrong_parameter_list += f"BOX_HIGHER_RIGHT_X : {BOX_HIGHER_RIGHT_X},DOMAIN_X : {DOMAIN_X}\n"
        if BOX_HIGHER_RIGHT_Y > DOMAIN_Y:
            wrong_parameter_list += f"BOX_HIGHER_RIGHT_Y : {BOX_HIGHER_RIGHT_Y},DOMAIN_X : {DOMAIN_Y}\n"
        if BOX_HIGHER_RIGHT_Z > DOMAIN_Z:
            wrong_parameter_list += f"BOX_HIGHER_RIGHT_Z : {BOX_HIGHER_RIGHT_Z},DOMAIN_X : {DOMAIN_Z}\n"

        ##sphere
        # sphere coordinate
        if SPHERE_X_MIN > SPHERE_X_MAX:
            wrong_parameter_list += f"SPHERE_X({SPHERE_X_MIN},{SPHERE_X_MAX})\n"
        if SPHERE_Y_MIN > SPHERE_Y_MAX:
            wrong_parameter_list += f"SPHERE_Y({SPHERE_Y_MIN},{SPHERE_Y_MAX})\n"
        if SPHERE_Z_MIN > SPHERE_Z_MAX:
            wrong_parameter_list += f"SPHERE_Z({SPHERE_Z_MIN},{SPHERE_Z_MAX})\n"

        if SPHERE_X_MIN > DOMAIN_X:
            wrong_parameter_list += f"SPHERE_X:{SPHERE_X_MIN},DOMAIN_X:{DOMAIN_X}\n"
        if SPHERE_Y_MIN > DOMAIN_Y:
            wrong_parameter_list += f"SPHERE_Y:{SPHERE_Y_MIN},DOMAIN_Y:{DOMAIN_Y}\n"
        if SPHERE_Z_MIN > DOMAIN_Z:
            wrong_parameter_list += f"SPHERE_Z:{SPHERE_Z_MIN},DOMAIN_Z:{DOMAIN_Z}\n"
        if SPHERE_X_MAX > DOMAIN_X:
            wrong_parameter_list += f"SPHERE_X:{SPHERE_X_MAX},DOMAIN_X:{DOMAIN_X}\n"
        if SPHERE_Y_MAX > DOMAIN_Y:
            wrong_parameter_list += f"SPHERE_Y:{SPHERE_Y_MAX},DOMAIN_Y:{DOMAIN_Y}\n"
        if SPHERE_Z_MAX > DOMAIN_Z:
            wrong_parameter_list += f"SPHERE_Z:{SPHERE_Z_MAX},DOMAIN_Z:{DOMAIN_Z}\n"

        if wrong_parameter_list != "":
            raise Exception("Wrong parameter error")

    except Exception as e:
        print(e)
        print("==========================Wrong parameter list=======================")
        print(wrong_parameter_list)
        print("=====================================================================")

        sys.exit()


def cavity_generation(iteration_index, water=False):
    print("Starting Cavity_Input_File_Generation...")

    ##write parameters on file
    generate_title()
    generate_domain()
    generate_dx_dz_dy()
    generate_time_window()

    textfile.write("\n")
    generate_material_soil()
    generate_material_asphalt()
    if water == True:
        generate_material_water()
    textfile.write("\n")

    generate_waveform()
    generate_hertzian_dipole()
    generate_rx()
    generate_src_steps()
    generate_rx_steps()

    textfile.write("\n")
    generate_asphalt_box()
    generate_soil_box()
    if water == True:
        # generate_cavity_sphere(water=True)
        generate_cavity_cylinder(water=True,water_portion=0.5)
    else:
        generate_cavity_sphere()

    textfile.write("\n")
    generate_geometry_view(iteration_index)

    textfile.close()

# ================================================================
def subsoil_generation(iteration_index):
    print("Starting Subsoil_Input_File_Generation...")

    ##write parameters on file
    generate_title()
    generate_domain()
    generate_dx_dz_dy()
    generate_time_window()

    textfile.write("\n")
    generate_material_soil()
    generate_material_asphalt()
    textfile.write("\n")

    generate_waveform()
    generate_hertzian_dipole()
    generate_rx()
    generate_src_steps()
    generate_rx_steps()

    textfile.write("\n")
    generate_asphalt_box()
    generate_soil_box()

    textfile.write("\n")
    generate_geometry_view(iteration_index)

    textfile.close()

# ================================================================

def auto_generation(underground_object_type,iteration_index):

    print("==================InputFile_Auto_Generation Start!======================")

    global UNDERGROUND_OBJECT_TYPE
    UNDERGROUND_OBJECT_TYPE=underground_object_type
    global TITLE
    TITLE= "B-scan of a %s" % UNDERGROUND_OBJECT_TYPE

    print(os.path.realpath(__file__))
    # generate file
    filepath = os.path.dirname(__file__)+"/../../Worktable/%s_%d.in" % (UNDERGROUND_OBJECT_TYPE, iteration_index)
    global textfile
    textfile = open(filepath, 'w')

    check_parameter_range()

    if underground_object_type=="cavity":
        cavity_generation(iteration_index,water=True)
    elif underground_object_type=="manhole":
        print("manhole")
    elif underground_object_type=="pothole":
        print("pothole")
    elif underground_object_type=="pipe":
        print("pipe")
    elif underground_object_type=="subsoil":
        subsoil_generation(iteration_index)
    else:
        print("wrong underground_object_type")
        sys.exit()

    print("Generation Done")

if __name__ == '__main__':
    auto_generation(sys.argv[1], int(sys.argv[2]))



