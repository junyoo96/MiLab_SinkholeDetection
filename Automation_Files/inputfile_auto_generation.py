from random import *
import sys

#Sinkhole Generation File
#=================================================================
#parameters
#================================================================
#titie parameter
TITLE= "B-scan of a cavity within a dielectric half-space"

#================================================================
#domain parameter
#지하가 시작되는 지점(높이)
DOMAIN_X_UNDERGROUND_START=1
#안테나 띄울 공간 얼마나 확보할지
DOMAIN_X_FREESPACE_OFFSET=0.1

DOMAIN_X=DOMAIN_X_UNDERGROUND_START+DOMAIN_X_FREESPACE_OFFSET #1m + 0.1m(지표면에서 안테나 살짝 띄울공간 확보)
DOMAIN_Y=0.1
DOMAIN_Z=0.1

#================================================================
#dx_dy_dz parameter
DX_DY_DZ_X=0.002
DX_DY_DZ_Y=0.002
DX_DY_DZ_Z=0.002

#================================================================
#time window
TIME_WINDOW="15e-9"

#================================================================
##material
#soil
MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN=10
MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX=10

MATERIAL_SOIL_CONDUCTIVITY_MIN=0.01
MATERIAL_SOIL_CONDUCTIVITY_MAX=0.01

MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN=1
MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX=1

MATERIAL_SOIL_MAGNETIC_LOSS_MIN=0
MATERIAL_SOIL_MAGNETIC_LOSS_MAX=0

MATERIAL_SOIL_IDENTIFIER="soil"

#================================================================
#waveform

WAVEFORM_TYPE="ricker"

WAVEFORM_MAX_AMPLITUDE_MIN=1
WAVEFORM_MAX_AMPLITUDE_MAX=1

WAVEFORM_CENTER_FREQUENCY_MIN=0.2
WAVEFORM_CENTER_FREQUENCY_MAX=0.8

WAVEFORM_IDENTIFIER="my_pulse"

#================================================================
#hertzian_dipole
#지표면에서 안테나 얼마나 띄울지
ANTENNA_HEIGHT_OFFSET=0.05 #5cm
#PML에 안테나가 붙어었으면 안되서 좀 떨어뜨리기 위한 offset
ANTENNA_Y_OFFSET=0.01

HERTZIAN_DIPOLE_SOURCE_POLARISATION="x"
HERTZIAN_DIPOLE_SOURCE_X=DOMAIN_X_UNDERGROUND_START+ANTENNA_HEIGHT_OFFSET
HERTZIAN_DIPOLE_SOURCE_Y=0+ANTENNA_Y_OFFSET
HERTZIAN_DIPOLE_SOURCE_Z=0.05
HERTZIAN_DIPOLE_SOURCE_IDENTIFIER="my_pulse"
#예외처리
#offset처리

#================================================================
#src_steps
SRC_STEPS_X=0
SRC_STEPS_Y=0.01
SRC_STEPS_Z=0

#예외처리
#================================================================
#rx(Reciever 좌표)
RX_X=HERTZIAN_DIPOLE_SOURCE_X
RX_Y=HERTZIAN_DIPOLE_SOURCE_Y+SRC_STEPS_Y
RX_Z=HERTZIAN_DIPOLE_SOURCE_Z

#예외처리
#================================================================
#rx_steps
RX_STEPS_X=0
RX_STEPS_Y=SRC_STEPS_Y
RX_STEPS_Z=0

#예외처리

#================================================================
##box(soil area)
#box low coordinate
BOX_LOWER_LEFT_X=0
BOX_LOWER_LEFT_Y=0
BOX_LOWER_LEFT_Z=0

#box high coordinate
BOX_HIGHER_RIGHT_X=1
BOX_HIGHER_RIGHT_Y=0.1
BOX_HIGHER_RIGHT_Z=0.1

#box material
BOX_MATERIAL_IDENTIFIER="soil"

#dielectric smoothing activation
BOX_DIELECTRIC_SMOOTHING_ACTIVATION="n"

#예외처리

#================================================================
##sphere(sinkhole)

#sphere coordinate
SPHERE_X_MIN=0.5
SPHERE_X_MAX=0.5
SPHERE_Y_MIN=0.05
SPHERE_Y_MAX=0.05
SPHERE_Z_MIN=0.05
SPHERE_Z_MAX=0.05

#sphere radius
SPHERE_RADIUS_MIN=0.03
SPHERE_RADIUS_MAX=0.03

#sphere material
SPHERE_MATERIAL="free_space"

#dielectric smoothing activation
SPHERE_DIELECTRIC_SMOOTHING_ACTIVATION="n"

#================================================================
#geometry_view(모델의 기하학적인 정보를 file형태로 출력하게 하는 명령어)
#geometry low coordinate
GEOMETRY_VIEW_LOWER_LEFT_X=0
GEOMETRY_VIEW_LOWER_LEFT_Y=0
GEOMETRY_VIEW_LOWER_LEFT_Z=0

#geometry high coordinate
GEOMETRY_VIEW_HIGHER_RIGHT_X=DOMAIN_X
GEOMETRY_VIEW_HIGHER_RIGHT_Y=DOMAIN_Y
GEOMETRY_VIEW_HIGHER_RIGHT_Z=DOMAIN_Z

#geometry dx_dy_dz
GEOMETRY_VIEW_DX=DX_DY_DZ_X
GEOMETRY_VIEW_DY=DX_DY_DZ_Y
GEOMETRY_VIEW_DZ=DX_DY_DZ_Z

#input file과 동일한 경로에 저장될 geometry view의 file이름 설정
GEOMETRY_VIEW_FILENAME="Line01_"
#================================================================
#================================================================
##Generation Code
#================================================================

text=None

def generate_title():
    # title
    title = f"#title: {TITLE}\n"
    text.write(title)

def generate_domain():
    # domain
    domain = f"#domain: {DOMAIN_X} {DOMAIN_Y} {DOMAIN_Z}\n"
    text.write(domain)

def generate_dx_dz_dy():
    # dx_dy_dz
    dx_dy_dz = f"#dx_dy_dz: {DX_DY_DZ_X} {DX_DY_DZ_Y} {DX_DY_DZ_Z}\n"
    text.write(dx_dy_dz)

def generate_time_window():
    #time_window
    time_window=f"#time_window: {TIME_WINDOW}\n"
    text.write(time_window)

def generate_material_soil():
    #relative permittivity
    relative_permittivity=random_sampling(MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN, MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX)
    #conductivity
    conductivity=random_sampling(MATERIAL_SOIL_CONDUCTIVITY_MIN, MATERIAL_SOIL_CONDUCTIVITY_MAX)
    #relative permeability
    relative_permeability=random_sampling(MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN,MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX)
    #magnetic loss
    magnetic_loss=random_sampling(MATERIAL_SOIL_MAGNETIC_LOSS_MIN,MATERIAL_SOIL_MAGNETIC_LOSS_MAX)
    #material identifier
    material_identifier=MATERIAL_SOIL_IDENTIFIER


    material_soil=f"#material: {relative_permittivity} {conductivity} {relative_permeability} {magnetic_loss} {material_identifier}\n"
    text.write(material_soil)

def generate_waveform():
    waveform_type=WAVEFORM_TYPE
    waveform_max_amplitude=random_sampling(WAVEFORM_MAX_AMPLITUDE_MIN, WAVEFORM_MAX_AMPLITUDE_MAX)
    waveform_center_frequency=random_sampling(WAVEFORM_CENTER_FREQUENCY_MIN,WAVEFORM_CENTER_FREQUENCY_MAX)
    waveform_identifier=WAVEFORM_IDENTIFIER

    waveform=f"#waveform: {waveform_type} {waveform_max_amplitude} {waveform_center_frequency}e9 {waveform_identifier}\n"
    text.write(waveform)

def generate_hertzian_dipole():
    hertzian_dipole_source_polarisation=HERTZIAN_DIPOLE_SOURCE_POLARISATION
    hertzian_dipole_source_x=HERTZIAN_DIPOLE_SOURCE_X
    hertzian_dipole_source_z=HERTZIAN_DIPOLE_SOURCE_Z
    hertzian_dipole_source_y=HERTZIAN_DIPOLE_SOURCE_Y
    hertzian_dipole_source_identifier=HERTZIAN_DIPOLE_SOURCE_IDENTIFIER

    hertzian_dipole=f"#hertzian_dipole: {hertzian_dipole_source_polarisation} {hertzian_dipole_source_x} {hertzian_dipole_source_y} {hertzian_dipole_source_z} {hertzian_dipole_source_identifier}\n"
    text.write(hertzian_dipole)

def generate_rx():
    rx_x=RX_X
    rx_y=RX_Y
    rx_z=RX_Z

    rx=f"#rx: {rx_x} {rx_y} {rx_z}\n"
    text.write(rx)

def generate_src_steps():
    src_steps_x=SRC_STEPS_X
    src_steps_y=SRC_STEPS_Y
    src_steps_z=SRC_STEPS_Z

    src_steps= f"#src_steps: {src_steps_x} {src_steps_y} {src_steps_z}\n"
    text.write(src_steps)

def generate_rx_steps():
    rx_steps_x=SRC_STEPS_X
    rx_steps_y=SRC_STEPS_Y
    rx_steps_z=SRC_STEPS_Z

    rx_steps=f"#rx_steps: {rx_steps_x} {rx_steps_y} {rx_steps_z}\n"
    text.write(rx_steps)

def generate_soil_box():
    box_lower_left_x=BOX_LOWER_LEFT_X
    box_lower_left_y =BOX_LOWER_LEFT_Y
    box_lower_left_z =BOX_LOWER_LEFT_Z

    box_higher_right_x = BOX_HIGHER_RIGHT_X
    box_higher_right_y = BOX_HIGHER_RIGHT_Y
    box_higher_right_z = BOX_HIGHER_RIGHT_Z

    box_material_identifier=BOX_MATERIAL_IDENTIFIER
    box_dielectric_smoothing_activation=BOX_DIELECTRIC_SMOOTHING_ACTIVATION

    soil_box = f"#box: {box_lower_left_x} {box_lower_left_y} {box_lower_left_z} {box_higher_right_x} {box_higher_right_y} {box_higher_right_z} {box_material_identifier} {box_dielectric_smoothing_activation}\n"
    text.write(soil_box)

def generate_sinkhole_sphere():
    sphere_x=random_sampling(SPHERE_X_MIN,SPHERE_X_MAX)
    sphere_y=random_sampling(SPHERE_Y_MIN,SPHERE_Y_MAX)
    sphere_z=random_sampling(SPHERE_Z_MIN,SPHERE_Z_MAX)
    sphere_radius=random_sampling(SPHERE_RADIUS_MIN,SPHERE_RADIUS_MAX)

    sphere_material=SPHERE_MATERIAL
    sphere_dielectric_smoothing_activation=SPHERE_DIELECTRIC_SMOOTHING_ACTIVATION

    sphere=f"#sphere: {sphere_x} {sphere_y} {sphere_z} {sphere_radius} {sphere_material} {sphere_dielectric_smoothing_activation}\n"
    text.write(sphere)

def generate_geometry_view():

    geometry_view_lower_left_x=GEOMETRY_VIEW_LOWER_LEFT_X
    geometry_view_lower_left_y=GEOMETRY_VIEW_LOWER_LEFT_Y
    geometry_view_lower_left_Z=GEOMETRY_VIEW_LOWER_LEFT_Z

    geometry_view_higher_right_x=GEOMETRY_VIEW_HIGHER_RIGHT_X
    geometry_view_higher_right_y=GEOMETRY_VIEW_HIGHER_RIGHT_Y
    geometry_view_higher_right_z=GEOMETRY_VIEW_HIGHER_RIGHT_Z

    geometry_view_dx=GEOMETRY_VIEW_DX
    geometry_view_dy=GEOMETRY_VIEW_DY
    geometry_view_dz=GEOMETRY_VIEW_DZ

    geometry_view_filename=GEOMETRY_VIEW_FILENAME

    geometry_view=f"#geometry_view: {geometry_view_lower_left_x} {geometry_view_lower_left_y} {geometry_view_lower_left_Z} {geometry_view_higher_right_x} {geometry_view_higher_right_y} {geometry_view_higher_right_z} {geometry_view_dx} {geometry_view_dy} {geometry_view_dz} {geometry_view_filename} n"
    text.write(geometry_view)

#================================================================
#utility functions

def random_sampling(min,max):

    value=0
    digits=0
    
    min_digits=count_digits(min)
    max_digits=count_digits(max)

    if min_digits<max_digits:
        digits=max_digits
    else:
        digits=min_digits 

    value=round(uniform(min,max),digits)

    return value

def count_digits(num):

    flag=False

    string=str(num)
    count=0
    for char in string:
        if flag==True:
            count+=1
        if char==".":
            flag=True

    return count

#================================================================
def check_parameter_range():
    print("Check Parameters...")

    wrong_parameter_list=""

    try:
        #Material
        if MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN>MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX:
            wrong_parameter_list+=f"MATERIAL_SOIL_RELATIVE_PERMITTIVITY: ({MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MIN},{MATERIAL_SOIL_RELATIVE_PERMITTIVITY_MAX})\n"
        if MATERIAL_SOIL_CONDUCTIVITY_MIN>MATERIAL_SOIL_CONDUCTIVITY_MAX:
            wrong_parameter_list+=f"MATERIAL_SOIL_CONDUCTIVITY: ({MATERIAL_SOIL_CONDUCTIVITY_MIN},{MATERIAL_SOIL_CONDUCTIVITY_MAX})\n"
        if MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN>MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX:
            wrong_parameter_list+=f"MATERIAL_SOIL_RELATIVE_PERMEABILITY: ({MATERIAL_SOIL_RELATIVE_PERMEABILITY_MIN},{MATERIAL_SOIL_RELATIVE_PERMEABILITY_MAX})\n"
        if MATERIAL_SOIL_MAGNETIC_LOSS_MIN>MATERIAL_SOIL_MAGNETIC_LOSS_MAX:
            wrong_parameter_list+=f"MATERIAL_SOIL_MAGNETIC_LOSS: ({MATERIAL_SOIL_MAGNETIC_LOSS_MIN},{MATERIAL_SOIL_MAGNETIC_LOSS_MAX})\n"

        #waveform
        if HERTZIAN_DIPOLE_SOURCE_X>DOMAIN_X:
            wrong_parameter_list+=f"HERTZIAN_DIPOLE_SOURCE_X : {HERTZIAN_DIPOLE_SOURCE_X},DOMAIN_X : {DOMAIN_X})\n"
        if HERTZIAN_DIPOLE_SOURCE_Y>DOMAIN_Y:
            wrong_parameter_list+=f"HERTZIAN_DIPOLE_SOURCE_Y :{HERTZIAN_DIPOLE_SOURCE_Y},DOMAIN_Y : {DOMAIN_Y})\n"
        if HERTZIAN_DIPOLE_SOURCE_X>DOMAIN_X:
            wrong_parameter_list+=f"HERTZIAN_DIPOLE_SOURCE_Z :{HERTZIAN_DIPOLE_SOURCE_Z},DOMAIN_Z : {DOMAIN_Z})\n"

        #rx
        if RX_X>DOMAIN_X:
            wrong_parameter_list+=f"RX_X:{RX_X},DOMAIN_X : {DOMAIN_X}\n"
        if RX_Y>DOMAIN_Y:
            wrong_parameter_list+=f"RX_Y:{RX_Y},DOMAIN_Y : {DOMAIN_Y}\n"
        if RX_Z>DOMAIN_Z:
            wrong_parameter_list+=f"RX_Z:{RX_Z},DOMAIN_Z : {DOMAIN_Z}\n"

        #src_steps
        if SRC_STEPS_X>DOMAIN_X:
            wrong_parameter_list += f"SRC_STEPS_X:{SRC_STEPS_X},DOMAIN_X : {DOMAIN_X}\n"
        if SRC_STEPS_Y>DOMAIN_Y:
            wrong_parameter_list += f"SRC_STEPS_Y:{SRC_STEPS_Y},DOMAIN_Y : {DOMAIN_Y}\n"
        if SRC_STEPS_Z>DOMAIN_Z:
            wrong_parameter_list += f":SRC_STEPS_Z:{SRC_STEPS_Z},DOMAIN_Z : {DOMAIN_Z}\n"

        # rx_steps
        if RX_STEPS_X > DOMAIN_X:
            wrong_parameter_list += f":RX_STEPS_X:{RX_STEPS_X},DOMAIN_X : {DOMAIN_X}\n"
        if RX_STEPS_Y > DOMAIN_Y:
            wrong_parameter_list += f":RX_STEPS_Y:{RX_STEPS_Y},DOMAIN_Y : {DOMAIN_Y}\n"
        if RX_STEPS_Z > DOMAIN_Z:
            wrong_parameter_list += f":RX_STEPS_Z:{RX_STEPS_Z},DOMAIN_Z : {DOMAIN_Z}\n"

        #box
        if BOX_HIGHER_RIGHT_X>DOMAIN_X:
            wrong_parameter_list += f"BOX_HIGHER_RIGHT_X : {BOX_HIGHER_RIGHT_X},DOMAIN_X : {DOMAIN_X}\n"
        if BOX_HIGHER_RIGHT_Y>DOMAIN_Y:
            wrong_parameter_list += f"BOX_HIGHER_RIGHT_Y : {BOX_HIGHER_RIGHT_Y},DOMAIN_X : {DOMAIN_Y}\n"
        if BOX_HIGHER_RIGHT_Z>DOMAIN_Z:
            wrong_parameter_list += f"BOX_HIGHER_RIGHT_Z : {BOX_HIGHER_RIGHT_Z},DOMAIN_X : {DOMAIN_Z}\n"

        ##sphere
        #sphere coordinate
        if SPHERE_X_MIN>SPHERE_X_MAX:
            wrong_parameter_list += f"SPHERE_X({SPHERE_X_MIN},{SPHERE_X_MAX})\n"
        if SPHERE_Y_MIN>SPHERE_Y_MAX:
            wrong_parameter_list += f"SPHERE_Y({SPHERE_Y_MIN},{SPHERE_Y_MAX})\n"
        if SPHERE_Z_MIN>SPHERE_Z_MAX:
            wrong_parameter_list += f"SPHERE_Z({SPHERE_Z_MIN},{SPHERE_Z_MAX})\n"

        if SPHERE_X_MIN>DOMAIN_X:
            wrong_parameter_list += f"SPHERE_X:{SPHERE_X_MIN},DOMAIN_X:{DOMAIN_X}\n"
        if SPHERE_Y_MIN>DOMAIN_Y:
            wrong_parameter_list += f"SPHERE_Y:{SPHERE_Y_MIN},DOMAIN_Y:{DOMAIN_Y}\n"
        if SPHERE_Z_MIN>DOMAIN_Z:
            wrong_parameter_list += f"SPHERE_Z:{SPHERE_Z_MIN},DOMAIN_Z:{DOMAIN_Z}\n"
        if SPHERE_X_MAX>DOMAIN_X:
            wrong_parameter_list += f"SPHERE_X:{SPHERE_X_MAX},DOMAIN_X:{DOMAIN_X}\n"
        if SPHERE_Y_MAX>DOMAIN_Y:
            wrong_parameter_list += f"SPHERE_Y:{SPHERE_Y_MAX},DOMAIN_Y:{DOMAIN_Y}\n"
        if SPHERE_Z_MAX>DOMAIN_Z:
            wrong_parameter_list += f"SPHERE_Z:{SPHERE_Z_MAX},DOMAIN_Z:{DOMAIN_Z}\n"

        if wrong_parameter_list!="":
            raise Exception("Wrong parameter error")

    except Exception as e:
        print(e)
        print("==========================Wrong parameter list=======================")
        print(wrong_parameter_list)
        print("=====================================================================")

        sys.exit()


#================================================================
def auto_generation(iteration_number):
    print("Starting Input_File_Generation...")
    check_parameter_range()
    
    for i in range(1, iteration_number+1):

        #generate file
        filepath="./input_file_generation_test_files/sinkhole_%d_.in" % i
        global text
        text=open(filepath,'w')

        ##write parameters on file
        generate_title()
        generate_domain()
        generate_dx_dz_dy()
        generate_time_window()

        text.write("\n")
        generate_material_soil()
        text.write("\n")

        generate_waveform()
        generate_hertzian_dipole()
        generate_rx()
        generate_src_steps()
        generate_rx_steps()

        text.write("\n")
        generate_soil_box()
        generate_sinkhole_sphere()

        text.write("\n")
        generate_geometry_view()

        text.close()

        print("Generation Done")

if __name__ == '__main__':
    auto_generation(1)