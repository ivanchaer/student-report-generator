# This Python file uses the following encoding: utf-8

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import itertools

class Graph():

    def generate_images(self, evaluations, file_naming_convention):

        collor_pallete = "bgrcmykw"


        # get list of all students
        students = ()
        for evaluation in evaluations:
            for student in evaluation:
                students += (student,)

        students = sorted(set(students))

        for student_name in students:


            student_evaluations = []
            for evaluation in evaluations:
                if student_name in evaluation:
                    student_evaluations.append(evaluation[student_name]['grades'])

            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')

            # x is left / right (chriteria)
            # y is back / forward (evaluations)
            # z is up / down (grade values)

            chriteria_count = len(evaluations[0][student_name])

            xpos = range(0,chriteria_count) * len(student_evaluations)
            ypos = list(itertools.chain(*[[i] * chriteria_count for i in range(len(student_evaluations))]))
            zpos = [0] * chriteria_count * len(student_evaluations)

            dx = [0.7] * chriteria_count * len(student_evaluations)
            dy = [0.2] * chriteria_count * len(student_evaluations)

            dz = []
            for evaluation in student_evaluations:
                for student_chriteria_grade in evaluation.values():
                    if student_chriteria_grade:
                        dz += [student_chriteria_grade]
                    else:
                        dz += [0]

            colors = []
            for color_index, evaluation in enumerate(student_evaluations):
                colors += [collor_pallete[color_index]] * chriteria_count

            # print xpos
            # print ypos
            # print zpos
            # print dx
            # print dy
            # print dz
            # print colors
            ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, edgecolor = "none", alpha=0.7)
            ax1.view_init(elev=15., azim=-109)

            evaluation_names = ['Trimester %s' % (evaluation_number + 1) for evaluation_number in range(len(student_evaluations))]
            chriteria_names = evaluations[0][student_name].keys()

            ticksx = np.arange(0, chriteria_count, 1)
            plt.xticks(ticksx, chriteria_names, rotation='vertical')

            ticksy = np.arange(0, 2, 1)
            plt.yticks(ticksy, evaluation_names)
            ax1.tick_params(axis='y', direction='out', pad=15,length=5,width=2,labelsize=8)


            student_filename = file_naming_convention(student_name)

            fig.savefig('documents/images-output/%s.png' % student_filename) 
            # plt.show()