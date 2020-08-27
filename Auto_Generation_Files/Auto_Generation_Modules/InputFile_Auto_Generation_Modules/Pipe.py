from Utility import Utility
#from sympy import Symbol, solve
from Cylinder import Cylinder

class Pipe(Utility):
    def __init__(self, pipe_material, pipe_dielectirc_smoothing_activation, pipe_content_material_identifier, pipe_content_dielectric_smoothing_activation, water=False):
        self.pipe_material = pipe_material
        self.pipe_dielectric_smoothing_activation = pipe_dielectirc_smoothing_activation
        self.pipe_pass_point_y_range_offset = 0.02
        self.pipe_pass_point_x_range_offset = 0.02
        self.pipe_pass_point_z_range_offset = 0.02
        self.pipe_top_z = 0.499
        self.pipe_bottom_z = 0.201
        self.pipe_thickness = 0.2
        self.pipe_content_thickness = 0.1
        self.pipe_content_material_identifier = pipe_content_material_identifier
        self.pipe_content_dielectric_smoothing_activation = pipe_content_dielectric_smoothing_activation
        self.water = water

    def generate_pipe_with_cylinder(self,domain_x,domain_y,domain_z,antenna_y_offset,textfile):
        utility=Utility()

        #1. Pipe 지나갈 점 결정
        domain_center_point_y = domain_y / 2
        offset_y_between_antenna_and_center=domain_center_point_y-antenna_y_offset

        pipe_pass_point_x_min=domain_x/2-self.pipe_pass_point_x_range_offset
        pipe_pass_point_x_max=domain_x/2+self.pipe_pass_point_x_range_offset
        pipe_pass_point_x=utility.random_sampling(pipe_pass_point_x_min,pipe_pass_point_x_max)

        pipe_pass_point_y_min=antenna_y_offset+self.pipe_pass_point_y_range_offset
        pipe_pass_point_y_max=domain_center_point_y+(offset_y_between_antenna_and_center-self.pipe_pass_point_y_range_offset)
        pipe_pass_point_y=utility.random_sampling(pipe_pass_point_y_min,
                                                  pipe_pass_point_y_max)

        pipe_highest_center_point_z=round(self.pipe_top_z-self.pipe_thickness/2,3)
        pipe_lowest_center_point_z=round(self.pipe_bottom_z-self.pipe_thickness/2,3)
        pipe_start_point_z=utility.random_sampling(pipe_lowest_center_point_z,pipe_highest_center_point_z)
        pipe_end_point_z = pipe_start_point_z

        print("pipe z range:",pipe_lowest_center_point_z,pipe_highest_center_point_z)
        

        pipe_direction=utility.random_sampling(0,1)
        pipe_start_point_x =0
        pipe_start_point_y =0
        pipe_end_point_x =0
        pipe_end_point_y =0


        #jun-modify only for horizontal
        pipe_direction=0

        #x축으로 길게
        if pipe_direction==0:
            pipe_start_point_x=pipe_pass_point_x
            pipe_start_point_y=0
            pipe_end_point_x=pipe_pass_point_x
            pipe_end_point_y=domain_y
        #y축으로 길게
        else:
            pipe_start_point_x =0
            pipe_start_point_y =pipe_pass_point_y
            pipe_end_point_x =domain_x
            pipe_end_point_y =pipe_pass_point_y

        
        pipe_start_point_x =round(pipe_start_point_x,2)
        pipe_start_point_y =round(pipe_start_point_y,2)
        pipe_start_point_z=round(pipe_start_point_z,3)
        pipe_end_point_x =round(pipe_end_point_x,2)
        pipe_end_point_y =round(pipe_end_point_y,2)
        pipe_end_point_z =round(pipe_end_point_z,3)

        print("pipe center z:",pipe_start_point_z)


        #1. Pipe 지나갈 점 결정
        # domain_center_point_y = domain_y / 2
        # offset_y_between_antenna_and_center=domain_center_point_y-antenna_y_offset
        #
        # pipe_pass_point_x=domain_x/2
        # pipe_pass_point_y_min=antenna_y_offset+self.pipe_pass_point_y_range_offset
        # pipe_pass_point_y_max=domain_center_point_y+(offset_y_between_antenna_and_center-self.pipe_pass_point_y_range_offset)
        # pipe_pass_point_y=utility.random_sampling(pipe_pass_point_y_min,
        #                                           pipe_pass_point_y_max)

        # 2. Pipe 시작 점 결정
        # pipe_start_point_x = utility.random_sampling(0, 1)
        # pipe_start_point_y = 0
        # # x가 0이면 y가 랜덤
        # if pipe_start_point_x == 0:
        #     pipe_start_point_y = utility.random_sampling(0, domain_y)
        # # x가 1이면 x가 랜덤이고, y=0
        # else:
        #     pipe_start_point_x = utility.random_sampling(0, domain_x)


        # #3. Pipe 끝 점 결정( Pipe 대각선으로 하는 코드 일단 지우지마라)
        # m=Symbol('m')
        # c=Symbol('c')
        # tmp_x=pipe_start_point_x
        # tmp_y=pipe_start_point_y
        # equation1 = m * tmp_x + c - tmp_y
        # tmp_x = pipe_pass_point_x
        # tmp_y = pipe_pass_point_y
        # equation2 = m * tmp_x + c - tmp_y
        #
        # solution=solve((equation1,equation2),dict=True)
        #
        # pipe_end_point_x = None
        # pipe_end_point_y = None
        # if pipe_start_point_x==0:
        #     pipe_end_point_x = domain_x
        #     pipe_end_point_y = solution[0][m] * pipe_end_point_x + solution[0][c]
        # else:
        #     pipe_end_point_y = domain_y
        #     pipe_end_point_x = (pipe_end_point_y - solution[0][c])/solution[0][m]
        #
        # pipe_end_point_x=round(pipe_end_point_x,2)
        # pipe_end_point_y=round(pipe_end_point_y,2)
        #
        # if pipe_end_point_x>domain_x:
        #     pipe_end_point_x=domain_x
        # elif pipe_end_point_x<0:
        #     pipe_end_point_x=0
        #
        # if pipe_end_point_y>domain_y:
        #     pipe_end_point_y=domain_y
        # elif pipe_end_point_y<0:
        #     pipe_end_point_y=0

        # print(round(pipe_start_point_x,2),round(pipe_start_point_y,2))
        # print(round(pipe_pass_point_x, 2), round(pipe_pass_point_y, 2))
        # print(round(pipe_end_point_x,2),round(pipe_end_point_y,2))



        #3. Pipe외관 생성
        pipe_cylinder=Cylinder(pipe_start_point_x,
                               pipe_start_point_y,
                               pipe_start_point_z,
                               pipe_end_point_x,
                               pipe_end_point_y,
                               pipe_end_point_z,
                               self.pipe_thickness,
                               self.pipe_material,
                               self.pipe_dielectric_smoothing_activation
                    )

        pipe_cylinder.write_textfile(textfile)
        

        pipe_content_cylinder=None
        if self.water==True:
            # 4. Pipe내 물 생성
            pipe_content_cylinder = Cylinder(pipe_start_point_x,
                                        pipe_start_point_y,
                                        pipe_start_point_z,
                                        pipe_end_point_x,
                                        pipe_end_point_y,
                                        pipe_end_point_z,
                                        self.pipe_content_thickness,
                                        self.pipe_content_material_identifier,
                                        self.pipe_content_dielectric_smoothing_activation
                                        )
        else:
            # 4. Pipe내 공기 생성
            pipe_content_cylinder=Cylinder(pipe_start_point_x,
                                        pipe_start_point_y,
                                        pipe_start_point_z,
                                        pipe_end_point_x,
                                        pipe_end_point_y,
                                        pipe_end_point_z,
                                        self.pipe_content_thickness,
                                        self.pipe_content_material_identifier,
                                        self.pipe_content_dielectric_smoothing_activation
                                        )

        textfile=pipe_content_cylinder.write_textfile(textfile)

        return textfile
