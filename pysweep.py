#!/usr/bin/env python
import subprocess
import resource
import time

def main():
  print('MAIN FUCNTION')

  # ip_target = '192.168.200.'
  ip_target = '24.165.23.'
  
  fping_responses = []

  # start timer
  start_time = time.time()

  for x in range (0,4): #257
    current_ip_address = ip_target + '{}'.format(x)

    current_fping = subprocess.Popen(['fping', '-a', '-C 5', '-q', '-e', current_ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    std_output = current_fping.stderr.read()
    std_output_decoded = std_output.decode('utf-8')

    print('STD OUTPUT DECODED', std_output_decoded)
    split_output = std_output_decoded.split(':')
    recorded_times = split_output[1][:-1]

    if '- - - - -' not in recorded_times:
      fping_responses.append([current_ip_address, recorded_times])
      printed_output = 'Host: ' + current_ip_address + ' is detected online. Response time(s) were:' + recorded_times

      print(printed_output)
  
  # total time of scan
  elapsed_time = time.time() - start_time

  # for loop completes
  ip_str = ''
  elapsed_time_str = str(elapsed_time).split('.')[0]

  for res in fping_responses:
    ip_str += res[0] + '\n'
  
  results_str = 'The following hosts were found to be online and responding to ping requests: \n \nDetected Hosts:\n==============\n' + ip_str + '\n' + 'Total time to scan took: ' + elapsed_time_str + ' ms'

  print('RESULTS STR', results_str)

if __name__ == '__main__':
  main()