from Utility import Utility
from Cylinder import Cylinder

class Manhole(Utility):
    def __init__(self, manhole_cover_material, manhole_cover_dielectric_smoothing_activation, water_material_identifier, water_dielectric_smoothing_activation, free_space_material_identifier, free_space_dielectric_smoothing_activation, water=False):
        self.manhole_point_x_range_offset=0.02
        self.manhole_point_y_range_offset=0.02
        self.manhole_height_offset_min=0.45
        self.manhole_height_offset_max=0.80
        self.manhole_thickness_min=0.15
        self.manhole_thickness_max=0.45
        self.manhole_cover_thickness_min=0.05
        self.manhole_cover_thickness_max = 0.1
        self.manhole_cover_material=manhole_cover_material
        self.manhole_cover_dielectric_smoothing_activation=manhole_cover_dielectric_smoothing_activation
        self.water_material_identifier=water_material_identifier
        self.water_dielectric_smoothing_activation=water_dielectric_smoothing_activation
        self.free_space_material_identifier=free_space_material_identifier
        self.free_space_dielectric_smoothing_activation=free_space_dielectric_smoothing_activation
        self.water=water
        self.water_portion_min=0.30
        self.water_portion_max=1

    def generate_manhole(self,domain_x,domain_y,domain_z_underground_start,antenna_y_offset,textfile):
        utility=Utility()

        #1. manhole의 x,y,z좌표 정하기
        domain_center_point_y=domain_y/2
        offset_y_between_antenna_and_center = domain_center_point_y - antenna_y_offset

        manhole_lower_point_y_min=round(antenna_y_offset+self.manhole_point_y_range_offset,2)
        manhole_lower_point_y_max=round(domain_center_point_y+(offset_y_between_antenna_and_center-self.manhole_point_y_range_offset),2)
        manhole_lower_point_y=utility.random_sampling(manhole_lower_point_y_min,manhole_lower_point_y_max)

        domain_center_point_x = domain_x / 2
        manhole_lower_point_x_min = round(domain_center_point_x - self.manhole_point_x_range_offset,2)
        manhole_lower_point_x_max = round(domain_center_point_x + self.manhole_point_x_range_offset,2)
        manhole_lower_point_x = utility.random_sampling(manhole_lower_point_x_min,manhole_lower_point_x_max)

        manhole_higher_point_z=domain_z_underground_start

        manhole_height=utility.random_sampling(self.manhole_height_offset_min,self.manhole_height_offset_max)
        manhole_cover_thickness=utility.random_sampling(self.manhole_cover_thickness_min,self.manhole_cover_thickness_max)
        manhole_content_height=round(manhole_height-manhole_cover_thickness,2)
        manhole_lower_point_z=round(manhole_higher_point_z-manhole_height,2)

        #manhole_radius
        manhole_thickness=utility.random_sampling(self.manhole_thickness_min,self.manhole_thickness_max)
        
        print(manhole_cover_thickness)
        print(manhole_height)
        print(manhole_content_height)
        print(manhole_lower_point_x,manhole_lower_point_y,manhole_lower_point_z)
        

        #2. manhole content 정하기

        manhole_components=[]
        if self.water==False:
            manhole_content_free_space=Cylinder(manhole_lower_point_x,
                                                manhole_lower_point_y,
                                                manhole_lower_point_z,
                                                manhole_lower_point_x,
                                                manhole_lower_point_y,
                                                manhole_content_height,
                                                manhole_thickness,
                                                self.water_material_identifier,
                                                self.water_dielectric_smoothing_activation
                                                )
            manhole_components.append(manhole_content_free_space)
        else:
            #manhole water로 채우기
            manhole_content_lower_point_z = manhole_lower_point_z
            manhole_content_water_portion=utility.random_sampling(self.water_portion_min,self.water_portion_max)
            manhole_content_water_height=round(manhole_content_height*manhole_content_water_portion,2)
            manhole_content_higher_point_z=round(manhole_lower_point_z+manhole_content_water_height,2)

            

            manhole_content_water = Cylinder(manhole_lower_point_x,
                                                  manhole_lower_point_y,
                                                  manhole_content_lower_point_z,
                                                  manhole_lower_point_x,
                                                  manhole_lower_point_y,
                                                  manhole_content_higher_point_z,
                                                  manhole_thickness,
                                                  self.water_material_identifier,
                                                  self.water_dielectric_smoothing_activation
                                                  )
            manhole_components.append(manhole_content_water)

            # manhole freespace로 채우기
            if manhole_content_water_portion<1:
                manhole_content_lower_point_z=manhole_content_higher_point_z
                manhole_content_higher_point_z=round(manhole_higher_point_z - manhole_cover_thickness,2)

                manhole_content_free_space = Cylinder(manhole_lower_point_x,
                                                      manhole_lower_point_y,
                                                      manhole_content_lower_point_z,
                                                      manhole_lower_point_x,
                                                      manhole_lower_point_y,
                                                      manhole_content_higher_point_z,
                                                      manhole_thickness,
                                                      self.free_space_material_identifier,
                                                      self.free_space_dielectric_smoothing_activation
                                                      )
                manhole_components.append(manhole_content_free_space)

        print(manhole_content_water_portion, manhole_content_water_height)

        #manhole cover
        manhole_cover=Cylinder(manhole_lower_point_x,
                                manhole_lower_point_y,
                                round(manhole_higher_point_z - manhole_cover_thickness,2),
                                manhole_lower_point_x,
                                manhole_lower_point_y,
                                manhole_higher_point_z,
                                manhole_thickness,
                                self.manhole_cover_material,
                                self.manhole_cover_dielectric_smoothing_activation
                                )
        manhole_components.append(manhole_cover)
        

        for manhole_component in manhole_components:
            manhole_component.write_textfile(textfile)








