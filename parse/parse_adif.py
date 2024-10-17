#!./venv/bin/python3  
  
from datetime import datetime,timezone  
import sys

callsign = sys.argv[1]  

def cut_to_dot(text: str)->str:
    index = text.find('.')

    if index != -1:  # Проверяем, что точка найдена
        result = text[:index]
    else:
        result = text  # Если точки нет, возвращаем всю строку

    return(result)  # Вывод: Это пример



  
def parse_adif_to_txt():
    prev_band_value = "1"  
    band_value = "1"
    with open(f'parse/dx_spots/{callsign}.adif') as inp_file:  
        with open(f'parse/dx_spots/{callsign}.txt', 'w') as out_file:  
            for line in inp_file:  
                qso_date = line.find('QSO_DATE:')  
                if qso_date == -1:  
                    continue  
                prev_band_value = band_value
                qso_date_value = line[line.find('>', qso_date) + 1 : line.find('<', qso_date)]  
                time_on = line.find('TIME_ON:')  
                time_on_value = line[line.find('>', time_on) + 1 : line.find('<', time_on) -2 ]  
                band = line.find('FREQ:')  
                band_value = line[line.find('>', band) + 1 : line.find('<', band)]  
                mode = line.find('MODE:')  
                mode_value = line[line.find('>', mode) + 1 : line.find('<', mode)]  
                #call = line.find('CALL:')  
                #call_value = line[line.find('>', call) + 1 : line.find('<', call)]  
                #rst_send = line.find('APP_PSKREP_SNR')  
                #rst_send_value = line[line.find('>', rst_send) + 1 : line.find('<', rst_send)]  
                if int(cut_to_dot(band_value)) != int(cut_to_dot(prev_band_value)):
                    result = qso_date_value + ' ' + time_on_value + ' ' + band_value + ' ' + mode_value + ' '
                    print(result)  
                    out_file.write(result + '\n')  
  
  
  
def main():  
    parse_adif_to_txt()   
  
  
if __name__ == "__main__":  
    main()