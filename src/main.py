from typing import List
import matplotlib.pyplot as plt


def data_prepare():
    temp = []
    cp = []
    txt_reader("Specific_Heat.txt", temp, cp)
    return temp, cp


def txt_reader(text_input_path: str, temp: List, cp: List):
    with open(text_input_path, "r") as file:
        for number, line in enumerate(file):
            if number < 5:
                pass
            else:
                read_line(line, temp, cp)


def read_line(line: str, temp: List, cp: List):
    for sign_number, sign in enumerate(line):
        if sign == " ":
            temp.append(line[0:sign_number])
            cp.append(line[sign_number+1:-2])


def repair_types(temp: List, cp: List):
    for index, value in enumerate(temp):
        temp[index] = float(value)
    for index, value in enumerate(cp):
        cp[index] = float(value)


def prepare_enthalpy(temp: List, cp: List):
    enthalpy = []
    if len(temp) != len(cp):
        print("The lists aren't equal")
        return 0
    for index in range(len(temp)):
        index = int(index)
        if index == 0:
            enthalpy.append(0)
        else:
            enthalpy.append(enthalpy[index - 1] + (temp[index]-temp[index-1]) * (cp[index]+cp[index-1]) * (1/2))
    return enthalpy


def interpolate(temp_list: List, cp: List, value: int):
    for index in range(len(temp_list)):
        if value > temp_list[index]:
            continue
        else:
            return (((value-temp_list[index - 1]) * ((cp[index]-cp[index - 1])
                                                     / (temp_list[index]- temp_list[index - 1]))) + cp[index - 1])


def add_phase_transition(temp: List, entalph: List, t_start: float, t_end: float, function: int):
    pass


if __name__ == "__main__":
    temp_list, cp_list = data_prepare()
    repair_types(temp_list, cp_list)
    enthalp_list = prepare_enthalpy(temp_list, cp_list)
    # print(temp_list, "\n", cp_list, "\n", enthalp_list)
    if len(enthalp_list) == len(cp_list):
        print("Lists lengths are equal")
    # print(interpolate(temp_list, enthalp_list, 140))
    # print(interpolate(temp_list, enthalp_list, 700))
    # print(interpolate(temp_list, enthalp_list, 800))
    # print(interpolate(temp_list, enthalp_list, 1545))
