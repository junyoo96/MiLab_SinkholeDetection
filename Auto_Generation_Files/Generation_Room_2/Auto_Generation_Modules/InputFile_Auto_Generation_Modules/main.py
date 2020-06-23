# -*- coding: utf-8 -*-
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
from Pipe import Pipe
from Manhole import Manhole

import sys
import os.path
import math
from math import gcd
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

#jun-modify
# DOMAIN_X = 0.2
# DOMAIN_Y = 0.8
DOMAIN_X = 0.15
DOMAIN_Y = 0.9
DOMAIN_Z = DOMAIN_Z_UNDERGROUND_START + DOMAIN_Z_FREESPACE_OFFSET  # 1m + 0.1m(지표면에서 안테나 살짝 띄울공간 확보)

# ================================================================
# dx_dy_dz parameter
DX_DY_DZ_X = 0.002
DX_DY_DZ_Y = 0.002
DX_DY_DZ_Z = 0.002

# ================================================================
# time window
TIME_WINDOW = "30e-9"

# ================================================================
##material
# free_space
MATERIAL_FREESPACE_IDENTIFIER = "free_space"
MATERIAL_FREESPACE_DIELECTRIC_SMOOTHING_ACTIVATION= "y"

# ================================================================
##material
# soil(4~12)
MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN = 4
MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX = 12

MATERIAL_SOIL_CONDUCTIVITY_MIN = 1e-07 # 1e-07
MATERIAL_SOIL_CONDUCTIVITY_MAX = 0.1

MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN = 1
MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX = 1

MATERIAL_SOIL_MAGNETIC_LOSS_MIN = 0
MATERIAL_SOIL_MAGNETIC_LOSS_MAX = 0

MATERIAL_SOIL_IDENTIFIER = "soil"

# ================================================================
# #material
# asphalt

#asphalt
# MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MIN = 4
# MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MAX = 7
#jun-modify
MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MIN = 3
MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MAX = 5

# MATERIAL_ASPHALT_CONDUCTIVITY_MIN = 0.02
# MATERIAL_ASPHALT_CONDUCTIVITY_MAX = 0.02
MATERIAL_ASPHALT_CONDUCTIVITY_MIN = 1e-13
MATERIAL_ASPHALT_CONDUCTIVITY_MAX = 1e-11

MATERIAL_ASPHALT_RELATIVE_PERMEABILITY_MIN = 1
MATERIAL_ASPHALT_RELATIVE_PERMEABILITY_MAX = 1

MATERIAL_ASPHALT_MAGNETIC_LOSS_MIN = 0
MATERIAL_ASPHALT_MAGNETIC_LOSS_MAX = 0

MATERIAL_ASPHALT_IDENTIFIER = "asphalt"
MATERIAL_ASPHALT_DIELECTRIC_SMOOTHING_ACTIVATION="n"

# ================================================================
##material
# water
# MATERIAL_WATER_RELATIVE_PERMITTIVITY_MIN = 80
# MATERIAL_WATER_RELATIVE_PERMITTIVITY_MAX = 80
#jun-modify
MATERIAL_WATER_RELATIVE_PERMITTIVITY_MIN = 81
MATERIAL_WATER_RELATIVE_PERMITTIVITY_MAX = 81

# MATERIAL_WATER_CONDUCTIVITY_MIN = 0.05
# MATERIAL_WATER_CONDUCTIVITY_MAX = 0.05
#jun-modify
MATERIAL_WATER_CONDUCTIVITY_MIN = 1e-04
MATERIAL_WATER_CONDUCTIVITY_MAX = 0.03

MATERIAL_WATER_RELATIVE_PERMEABILITY_MIN = 1
MATERIAL_WATER_RELATIVE_PERMEABILITY_MAX = 1

MATERIAL_WATER_MAGNETIC_LOSS_MIN = 0
MATERIAL_WATER_MAGNETIC_LOSS_MAX = 0

MATERIAL_WATER_IDENTIFIER = "water"
MATERIAL_WATER_DIELECTRIC_SMOOTHING_ACTIVATION="n"

# ================================================================
##material
# concrete
# MATERIAL_CONCRETE_RELATIVE_PERMITTIVITY_MIN = 6
# MATERIAL_CONCRETE_RELATIVE_PERMITTIVITY_MAX = 6
#jun-modify
MATERIAL_CONCRETE_RELATIVE_PERMITTIVITY_MIN = 5
MATERIAL_CONCRETE_RELATIVE_PERMITTIVITY_MAX = 10

MATERIAL_CONCRETE_CONDUCTIVITY_MIN = 0.01
MATERIAL_CONCRETE_CONDUCTIVITY_MAX = 0.01

MATERIAL_CONCRETE_RELATIVE_PERMEABILITY_MIN = 1
MATERIAL_CONCRETE_RELATIVE_PERMEABILITY_MAX = 1

MATERIAL_CONCRETE_MAGNETIC_LOSS_MIN = 0
MATERIAL_CONCRETE_MAGNETIC_LOSS_MAX = 0

MATERIAL_CONCRETE_IDENTIFIER = "concrete"
MATERIAL_CONCRETE_DIELECTRIC_SMOOTHING_ACTIVATION="n"

# ================================================================
##material
# METAL(Perfect electric Conductor)
MATERIAL_PEC_IDENTIFIER = "pec"
MATERIAL_PEC_DIELECTRIC_SMOOTHING_ACTIVATION="n"

# ================================================================
# waveform

WAVEFORM_TYPE = "ricker"

WAVEFORM_MAX_AMPLITUDE_MIN = 1
WAVEFORM_MAX_AMPLITUDE_MAX = 1

#jun-modify
# WAVEFORM_CENTER_FREQUENCY_MIN = 0.2
WAVEFORM_CENTER_FREQUENCY_MIN = 0.5
WAVEFORM_CENTER_FREQUENCY_MAX = 0.8

WAVEFORM_IDENTIFIER = "my_pulse"

# ================================================================
# hertzian_dipole
# 지표면에서 안테나 얼마나 띄울지
#jun modify
ANTENNA_HEIGHT_OFFSET = 0.02  # 2cm
# PML에 안테나가 붙어었으면 안되서 좀 떨어뜨리기 위한 offset
ANTENNA_Y_OFFSET = 0.1

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
SRC_STEPS_Y = 0.02
SRC_STEPS_Z = 0

# 예외처리
# ================================================================
# rx(Reciever 좌표)
SOURCE_RECEIVER_BETWEEN_OFFSET = 0.05

RX_X = HERTZIAN_DIPOLE_SOURCE_X
RX_Y = round(HERTZIAN_DIPOLE_SOURCE_Y + SOURCE_RECEIVER_BETWEEN_OFFSET,2)
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
ASPHALT_THICKNESS = 0.2 # 20cm

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
# #cavity information

SPHERE_MOVING_OFFSET_X = 0.05
#jun-modify 0.4
SPHERE_MOVING_OFFSET_Y = 0.15
SPHERE_MOVING_OFFSET_Z= 0.38
SPHERE_MOVING_OFFSET_Z_TOP = 0.38
SPHERE_MOVING_OFFSET_Z_BOTTOM = 0.19

# sphere coordinate
SPHERE_X_MIN = round(DOMAIN_X / 2 - SPHERE_MOVING_OFFSET_X,2)
SPHERE_X_MAX = round(DOMAIN_X / 2 + SPHERE_MOVING_OFFSET_X,2)
SPHERE_Y_MIN = round(DOMAIN_Y / 2 - SPHERE_MOVING_OFFSET_Y,2)
SPHERE_Y_MAX = round(DOMAIN_Y / 2 + SPHERE_MOVING_OFFSET_Y,2)
#0.2(because of background removal time)

#0.21~0.78
SPHERE_TOP_Z_MIN = round(ASPHALT_BOX_LOWER_LEFT_Z/2-SPHERE_MOVING_OFFSET_Z_BOTTOM,3)
SPHERE_TOP_Z_MAX = round(ASPHALT_BOX_LOWER_LEFT_Z/2+SPHERE_MOVING_OFFSET_Z_TOP,3)

#need to modify like sphere top z
SPHERE_Z_MIN = round(DOMAIN_Z_UNDERGROUND_START/2-SPHERE_MOVING_OFFSET_Z,3)
#jun-modify
SPHERE_Z_MAX = round(DOMAIN_Z_UNDERGROUND_START/2,3)

# sphere radius(10cm~20cm)
SPHERE_RADIUS_MIN = 0.10
SPHERE_RADIUS_MAX = 0.25

# sphere material
SPHERE_MATERIAL = "free_space"

# dielectric smoothing activation
SPHERE_DIELECTRIC_SMOOTHING_ACTIVATION = "y"

#cavity water portion
#jun-modify
CAVITY_WATER_PORTION_MIN=0.01
CAVITY_WATER_PORTION_MAX=0.30

#Determined waveform center frequency(save to write waveform freqeuncy file)
DETERMINED_WAVERFORM_CENTER_FREQUENCY=0

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
        utility.random_sampling(MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN,MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX,2),
        utility.random_sampling(MATERIAL_SOIL_CONDUCTIVITY_MIN, MATERIAL_SOIL_CONDUCTIVITY_MAX),
        utility.random_sampling(MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN, MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX),
        utility.random_sampling(MATERIAL_SOIL_MAGNETIC_LOSS_MIN, MATERIAL_SOIL_MAGNETIC_LOSS_MAX),
        MATERIAL_SOIL_IDENTIFIER
    )

    material_soil.write_textfile(textfile)

def generate_material_asphalt():

    material_asphalt = Material(
        utility.random_sampling(MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MIN,MATERIAL_ASPHALT_RELATIVE_PERMITTIVITY_MAX,2),
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

def generate_material_concrete():
    material_concrete=Material(
        utility.random_sampling(MATERIAL_CONCRETE_RELATIVE_PERMITTIVITY_MIN,MATERIAL_CONCRETE_RELATIVE_PERMITTIVITY_MAX),
        utility.random_sampling(MATERIAL_CONCRETE_CONDUCTIVITY_MIN,MATERIAL_CONCRETE_CONDUCTIVITY_MAX),
        utility.random_sampling(MATERIAL_CONCRETE_RELATIVE_PERMEABILITY_MIN,MATERIAL_CONCRETE_RELATIVE_PERMEABILITY_MAX),
        utility.random_sampling(MATERIAL_CONCRETE_MAGNETIC_LOSS_MIN,MATERIAL_CONCRETE_MAGNETIC_LOSS_MAX),
        MATERIAL_CONCRETE_IDENTIFIER
    )

    material_concrete.write_textfile(textfile)


def generate_waveform():

    global DETERMINED_WAVERFORM_CENTER_FREQUENCY
    DETERMINED_WAVERFORM_CENTER_FREQUENCY=utility.random_sampling(WAVEFORM_CENTER_FREQUENCY_MIN, WAVEFORM_CENTER_FREQUENCY_MAX)
    

    waveform=Waveform(
        WAVEFORM_TYPE,
        utility.random_sampling(WAVEFORM_MAX_AMPLITUDE_MIN, WAVEFORM_MAX_AMPLITUDE_MAX),
        DETERMINED_WAVERFORM_CENTER_FREQUENCY,
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

    #determine sphere_z

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
def generate_cavity_cylinder(water=False, water_portion=0):

    #jun-modify
    #MINIMUM_CAVITY_CYLINDER_END_RADIUS=0.01 
    MINIMUM_CAVITY_CYLINDER_END_RADIUS=0.02

    cavity_lower_x_determined=utility.random_sampling(SPHERE_X_MIN, SPHERE_X_MAX)
    cavity_lower_y_determined=utility.random_sampling(SPHERE_Y_MIN, SPHERE_Y_MAX)
    cavity_radius_determined = utility.random_sampling(SPHERE_RADIUS_MIN, SPHERE_RADIUS_MAX)
    cavity_z_top_determined=utility.random_sampling(SPHERE_TOP_Z_MIN, SPHERE_TOP_Z_MAX)
    
    cavity_z_determined=cavity_z_top_determined-cavity_radius_determined
    cavity_lower_z_determined = cavity_z_determined-cavity_radius_determined

    #jun-modify
    # cavity_lower_x_determined=0.3
    # cavity_lower_y_determined=0.3
    # cavity_radius_determined =0.05
    # cavity_lower_z_determined = 0.2
    #water_portion=
    
    #
    #to_generate_cylinder_num=int(cavity_radius_determined/MINIMUM_CAVITY_CYLINDER_END_RADIUS)*2-1

    water_portion=int(water_portion*100)

    to_generate_cylinder_num=100
    to_genearte_cylinder_with_water_portion_num=0

    calculated_gcd=gcd(to_generate_cylinder_num,water_portion)
    # to_generate_cylinder_num=int(to_generate_cylinder_num/calculated_gcd)
    to_generate_cylinder_num=100
    #to_genearte_cylinder_with_water_portion_num=int(water_portion/calculated_gcd)
    if water==True:
        to_genearte_cylinder_with_water_portion_num=water_portion
    else:
        to_genearte_cylinder_with_water_portion_num=0

    
    radius_per_cylinder=(cavity_radius_determined-MINIMUM_CAVITY_CYLINDER_END_RADIUS)/50
    height_per_cylinder=cavity_radius_determined*2/to_generate_cylinder_num

    # if to_genearte_cylinder_with_water_portion_num!=0:
    #     to_genearte_cylinder_with_water_portion_num+=1
    
    current_cylinder_lower_x=cavity_lower_x_determined
    current_cylinder_lower_y= cavity_lower_y_determined
    current_cylinder_lower_z = cavity_lower_z_determined   
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
            round(current_cylinder_lower_z,3),
            current_cylinder_lower_x,
            current_cylinder_lower_y,
            round(current_cylinder_lower_z+height_per_cylinder,3),
            round(current_cylinder_radius,3),
            current_material_identifier,
            current_dielectric_smoothing_activation
        )

        if round(current_cylinder_lower_z,3)>0:
            cavity_cylinder.write_textfile(textfile)

        current_cylinder_lower_z+=height_per_cylinder

        if i<to_generate_cylinder_num/2:
            current_cylinder_radius+=radius_per_cylinder
        else:
            tmp=current_cylinder_radius
            current_cylinder_radius -= radius_per_cylinder
            if current_cylinder_radius<MINIMUM_CAVITY_CYLINDER_END_RADIUS:
                current_cylinder_radius=MINIMUM_CAVITY_CYLINDER_END_RADIUS


def generate_pipe(water=False):
    pipe=None
    if water==True:
        pipe = Pipe(pipe_material=MATERIAL_CONCRETE_IDENTIFIER,
                    pipe_dielectirc_smoothing_activation=MATERIAL_CONCRETE_DIELECTRIC_SMOOTHING_ACTIVATION,
                    water=water,
                    pipe_content_material_identifier=MATERIAL_WATER_IDENTIFIER,
                    pipe_content_dielectric_smoothing_activation=MATERIAL_WATER_DIELECTRIC_SMOOTHING_ACTIVATION
                    )

    else:
        pipe = Pipe(pipe_material=MATERIAL_CONCRETE_IDENTIFIER,
                    pipe_dielectirc_smoothing_activation=MATERIAL_CONCRETE_DIELECTRIC_SMOOTHING_ACTIVATION,
                    water=water,
                    pipe_content_material_identifier=MATERIAL_FREESPACE_IDENTIFIER,
                    pipe_content_dielectric_smoothing_activation=MATERIAL_FREESPACE_DIELECTRIC_SMOOTHING_ACTIVATION
                    )


    pipe.generate_pipe_with_cylinder(DOMAIN_X,
                                 DOMAIN_Y,
                                 DOMAIN_Z,
                                 ANTENNA_Y_OFFSET,
                                 textfile
                                 )

    textfile.write("\n")

def generate_manhole(water):
    manhole=Manhole(manhole_cover_material=MATERIAL_PEC_IDENTIFIER,
                    manhole_cover_dielectric_smoothing_activation=MATERIAL_PEC_DIELECTRIC_SMOOTHING_ACTIVATION,
                    water_material_identifier=MATERIAL_WATER_IDENTIFIER,
                    water_dielectric_smoothing_activation=MATERIAL_WATER_DIELECTRIC_SMOOTHING_ACTIVATION,
                    free_space_material_identifier=MATERIAL_FREESPACE_IDENTIFIER,
                    free_space_dielectric_smoothing_activation=MATERIAL_FREESPACE_DIELECTRIC_SMOOTHING_ACTIVATION,
                    water=water
    )

    manhole.generate_manhole(DOMAIN_X,
                             DOMAIN_Y,
                             DOMAIN_Z_UNDERGROUND_START,
                             ANTENNA_Y_OFFSET,
                             textfile)

    textfile.write("\n")

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


def generate_model_environment_setting():
    generate_title()
    generate_domain()
    generate_dx_dz_dy()
    generate_time_window()

    textfile.write("\n")

def generate_waveform_setting():
    generate_waveform()
    generate_hertzian_dipole()
    generate_rx()
    generate_src_steps()
    generate_rx_steps()

    textfile.write("\n")

# ================================================================
# def check_parameter_range():
#     print("Check Parameters...")

#     wrong_parameter_list = ""

#     try:
#         # Material
#         if MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN > MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX:
#             wrong_parameter_list += f"MATERIAL_SOIL_RELATIVE_PERMITTIVITY: ({MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN},{MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX})\n"
#         if MATERIAL_SOIL_CONDUCTIVITY_MIN > MATERIAL_SOIL_CONDUCTIVITY_MAX:
#             wrong_parameter_list += f"MATERIAL_SOIL_CONDUCTIVITY: ({MATERIAL_SOIL_CONDUCTIVITY_MIN},{MATERIAL_SOIL_CONDUCTIVITY_MAX})\n"
#         if MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN > MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX:
#             wrong_parameter_list += f"MATERIAL_SOIL_RELATIVE_PERMEABILITY: ({MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN},{MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX})\n"
#         if MATERIAL_SOIL_MAGNETIC_LOSS_MIN > MATERIAL_SOIL_MAGNETIC_LOSS_MAX:
#             wrong_parameter_list += f"MATERIAL_SOIL_MAGNETIC_LOSS: ({MATERIAL_SOIL_MAGNETIC_LOSS_MIN},{MATERIAL_SOIL_MAGNETIC_LOSS_MAX})\n"

#         # waveform
#         if HERTZIAN_DIPOLE_SOURCE_X > DOMAIN_X:
#             wrong_parameter_list += f"HERTZIAN_DIPOLE_SOURCE_X : {HERTZIAN_DIPOLE_SOURCE_X},DOMAIN_X : {DOMAIN_X})\n"
#         if HERTZIAN_DIPOLE_SOURCE_Y > DOMAIN_Y:
#             wrong_parameter_list += f"HERTZIAN_DIPOLE_SOURCE_Y :{HERTZIAN_DIPOLE_SOURCE_Y},DOMAIN_Y : {DOMAIN_Y})\n"
#         if HERTZIAN_DIPOLE_SOURCE_X > DOMAIN_X:
#             wrong_parameter_list += f"HERTZIAN_DIPOLE_SOURCE_Z :{HERTZIAN_DIPOLE_SOURCE_Z},DOMAIN_Z : {DOMAIN_Z})\n"

#         # rx
#         if RX_X > DOMAIN_X:
#             wrong_parameter_list += f"RX_X:{RX_X},DOMAIN_X : {DOMAIN_X}\n"
#         if RX_Y > DOMAIN_Y:
#             wrong_parameter_list += f"RX_Y:{RX_Y},DOMAIN_Y : {DOMAIN_Y}\n"
#         if RX_Z > DOMAIN_Z:
#             wrong_parameter_list += f"RX_Z:{RX_Z},DOMAIN_Z : {DOMAIN_Z}\n"

#         # src_steps
#         if SRC_STEPS_X > DOMAIN_X:
#             wrong_parameter_list += f"SRC_STEPS_X:{SRC_STEPS_X},DOMAIN_X : {DOMAIN_X}\n"
#         if SRC_STEPS_Y > DOMAIN_Y:
#             wrong_parameter_list += f"SRC_STEPS_Y:{SRC_STEPS_Y},DOMAIN_Y : {DOMAIN_Y}\n"
#         if SRC_STEPS_Z > DOMAIN_Z:
#             wrong_parameter_list += f":SRC_STEPS_Z:{SRC_STEPS_Z},DOMAIN_Z : {DOMAIN_Z}\n"

#         # rx_steps
#         if RX_STEPS_X > DOMAIN_X:
#             wrong_parameter_list += f":RX_STEPS_X:{RX_STEPS_X},DOMAIN_X : {DOMAIN_X}\n"
#         if RX_STEPS_Y > DOMAIN_Y:
#             wrong_parameter_list += f":RX_STEPS_Y:{RX_STEPS_Y},DOMAIN_Y : {DOMAIN_Y}\n"
#         if RX_STEPS_Z > DOMAIN_Z:
#             wrong_parameter_list += f":RX_STEPS_Z:{RX_STEPS_Z},DOMAIN_Z : {DOMAIN_Z}\n"

#         # box
#         if BOX_HIGHER_RIGHT_X > DOMAIN_X:
#             wrong_parameter_list += f"BOX_HIGHER_RIGHT_X : {BOX_HIGHER_RIGHT_X},DOMAIN_X : {DOMAIN_X}\n"
#         if BOX_HIGHER_RIGHT_Y > DOMAIN_Y:
#             wrong_parameter_list += f"BOX_HIGHER_RIGHT_Y : {BOX_HIGHER_RIGHT_Y},DOMAIN_X : {DOMAIN_Y}\n"
#         if BOX_HIGHER_RIGHT_Z > DOMAIN_Z:
#             wrong_parameter_list += f"BOX_HIGHER_RIGHT_Z : {BOX_HIGHER_RIGHT_Z},DOMAIN_X : {DOMAIN_Z}\n"

#         ##sphere
#         # sphere coordinate
#         if SPHERE_X_MIN > SPHERE_X_MAX:
#             wrong_parameter_list += f"SPHERE_X({SPHERE_X_MIN},{SPHERE_X_MAX})\n"
#         if SPHERE_Y_MIN > SPHERE_Y_MAX:
#             wrong_parameter_list += f"SPHERE_Y({SPHERE_Y_MIN},{SPHERE_Y_MAX})\n"
#         if SPHERE_Z_MIN > SPHERE_Z_MAX:
#             wrong_parameter_list += f"SPHERE_Z({SPHERE_Z_MIN},{SPHERE_Z_MAX})\n"

#         if SPHERE_X_MIN > DOMAIN_X:
#             wrong_parameter_list += f"SPHERE_X:{SPHERE_X_MIN},DOMAIN_X:{DOMAIN_X}\n"
#         if SPHERE_Y_MIN > DOMAIN_Y:
#             wrong_parameter_list += f"SPHERE_Y:{SPHERE_Y_MIN},DOMAIN_Y:{DOMAIN_Y}\n"
#         if SPHERE_Z_MIN > DOMAIN_Z:
#             wrong_parameter_list += f"SPHERE_Z:{SPHERE_Z_MIN},DOMAIN_Z:{DOMAIN_Z}\n"
#         if SPHERE_X_MAX > DOMAIN_X:
#             wrong_parameter_list += f"SPHERE_X:{SPHERE_X_MAX},DOMAIN_X:{DOMAIN_X}\n"
#         if SPHERE_Y_MAX > DOMAIN_Y:
#             wrong_parameter_list += f"SPHERE_Y:{SPHERE_Y_MAX},DOMAIN_Y:{DOMAIN_Y}\n"
#         if SPHERE_Z_MAX > DOMAIN_Z:
#             wrong_parameter_list += f"SPHERE_Z:{SPHERE_Z_MAX},DOMAIN_Z:{DOMAIN_Z}\n"

#         if wrong_parameter_list != "":
#             raise Exception("Wrong parameter error")

#     except Exception as e:
#         print(e)
#         print("==========================Wrong parameter list=======================")
#         print(wrong_parameter_list)
#         print("=====================================================================")

#         sys.exit()

def cavity_generation(iteration_index, water=False):
    print("Starting Cavity_Input_File_Generation...")

    ##write parameters on file
    generate_model_environment_setting()

    generate_material_soil()
    generate_material_asphalt()
    if water == True:
        generate_material_water()
    textfile.write("\n")

    generate_waveform_setting()

    generate_asphalt_box()
    generate_soil_box()
    
    
    generate_cavity_cylinder(water,water_portion=utility.random_sampling(CAVITY_WATER_PORTION_MIN,CAVITY_WATER_PORTION_MAX))
    
    textfile.write("\n")

    generate_geometry_view(iteration_index)

    textfile.close()
# ================================================================
def pipe_generation(iteration_index,water=False):
    print("Starting Pipe_Input_File_Generation...")

    ##write parameters on file
    generate_model_environment_setting()

    generate_material_soil()
    generate_material_asphalt()
    if water == True:
        generate_material_water()
    generate_material_concrete()
    textfile.write("\n")

    generate_waveform_setting()

    generate_asphalt_box()
    generate_soil_box()

    generate_pipe(water)

    generate_geometry_view(iteration_index)

    textfile.close()
# ================================================================
def manhole_generation(iteration_index,water=False):
    print("Starting Manhole_Input_File_Generation...")

    ##write parameters on file
    generate_model_environment_setting()

    generate_material_soil()
    generate_material_asphalt()
    if water == True:
        generate_material_water()
    textfile.write("\n")

    generate_waveform_setting()

    generate_asphalt_box()
    generate_soil_box()

    generate_manhole(water)

    generate_geometry_view(iteration_index)

    textfile.close()
# ================================================================

def subsoil_generation(iteration_index):
    print("Starting Subsoil_Input_File_Generation...")

    ##write parameters on file
    generate_model_environment_setting()

    generate_material_soil()
    generate_material_asphalt()
    textfile.write("\n")

    generate_waveform_setting()

    generate_asphalt_box()
    generate_soil_box()
    textfile.write("\n")

    generate_geometry_view(iteration_index)

    textfile.close()

def generate_waveform_info_file():

    #waveform_info_file_path
    waveform_info_file_path=os.path.dirname(__file__)+"/../../Worktable/waveform_info.txt"
    wave_info_file=open(waveform_info_file_path,'w')
    splited_waveform_center_frequency=str(DETERMINED_WAVERFORM_CENTER_FREQUENCY).split('.')    
    wave_info_file.write(splited_waveform_center_frequency[0]+"\n")    
    wave_info_file.write(splited_waveform_center_frequency[1]+"\n")

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

    #check_parameter_range()

    if underground_object_type=="cavity":
        cavity_generation(iteration_index,water=True)
        # cavity_generation(iteration_index,water=False)
    elif underground_object_type=="manhole":
        manhole_generation(iteration_index,water=True)
    elif underground_object_type=="pothole":
        print("pothole")
    elif underground_object_type=="pipe":
        pipe_generation(iteration_index,water=True)
    elif underground_object_type=="subsoil":
        subsoil_generation(iteration_index)
    else:
        print("wrong underground_object_type")
        sys.exit()
    
    
    #generate waveform info file for image processing
    generate_waveform_info_file()

    print("Generation Done")

if __name__ == '__main__':
    auto_generation(sys.argv[1], int(sys.argv[2]))
    sys.exit()



