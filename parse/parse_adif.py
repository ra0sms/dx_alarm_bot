#!./venv/bin/python3  
  
from datetime import datetime,timezone  
import sys

callsign = sys.argv[1]  
  
def parse_adif_to_txt():  
    with open(f'parse/{callsign}.adif') as inp_file:  
        with open(f'parse/{callsign}.txt', 'w') as out_file:  
            for line in inp_file:  
                qso_date = line.find('QSO_DATE:')  
                if qso_date == -1:  
                    continue  
                qso_date_value = line[line.find('>', qso_date) + 1 : line.find('<', qso_date)]  
                time_on = line.find('TIME_ON:')  
                time_on_value = line[line.find('>', time_on) + 1 : line.find('<', time_on)]  
                band = line.find('FREQ:')  
                band_value = line[line.find('>', band) + 1 : line.find('<', band)]  
                mode = line.find('MODE:')  
                mode_value = line[line.find('>', mode) + 1 : line.find('<', mode)]  
                call = line.find('CALL:')  
                call_value = line[line.find('>', call) + 1 : line.find('<', call)]  
                rst_send = line.find('APP_PSKREP_SNR')  
                rst_send_value = line[line.find('>', rst_send) + 1 : line.find('<', rst_send)]  
  
                result = qso_date_value + ' ' + time_on_value + ' ' + band_value + ' ' + mode_value + ' ' + call_value + ' ' + rst_send_value  
                print(result)  
                out_file.write(result + '\n')  
  
  
def get_current_time():  
    now = datetime.now(timezone.utc)  
    current_date = now.strftime("%Y%m%d")  
    current_time = now.strftime("%H%M%S")  
    print(current_date + " " + current_time)  
  
  
def main():  
    parse_adif_to_txt()  
    get_current_time()  
  
  
if __name__ == "__main__":  
    main()