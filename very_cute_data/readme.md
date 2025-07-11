# Very cute data

    I had no idea what this data was. I thus found myself reading a [writeup of the year before](https://hackropole.fr/fr/writeups/fcsc2022-hardware-i2c-you-too/ea0d0518-63e6-4594-ac9c-9b4b02232d8e/)

Once i had understood how this I2C works i went to writing the program to parse the data and extract the flag : extract.py 

```python
import json
import sys
from pyDigitalWaveTools.vcd.parser import VcdParser

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    print('Give me a vcd file to parse')
    sys.exit(-1)

with open(fname) as vcd_file:
    vcd = VcdParser()
    vcd.parse(vcd_file)
    data = vcd.scope.toJson()


# Print the structure of the data variable
#print(json.dumps(data, indent=4))


# Extract all values of D0 when D1 transitions from 1 to 0 within the range of 0 to 350 µs
d0_values = []
d0_counter = 0
prev_d1_state = None
d1_samples = data['children'][0]['children'][1]['data']  # Accessing D1 samples
d0_samples = data['children'][0]['children'][0]['data']  # Accessing D0 samples
for i in range(len(d1_samples)):
    current_d1_state = d1_samples[i][1]
    timestamp = d1_samples[i][0]
    if prev_d1_state is not None and prev_d1_state == '1' and current_d1_state == '0' and 350000 <= timestamp <= 2000000:
        while d0_samples[d0_counter+1][0] < timestamp:
            d0_counter += 1
        d0_value = d0_samples[d0_counter][1]  # Accessing D0 data at the same index as D1
        d0_values.append((timestamp, d0_value))
    prev_d1_state = current_d1_state

# Print or process the captured D0 values within the specified range
#for timestamp, value in d0_values:
#    print(f"D1 transitioned from 1 to 0 at timestamp {timestamp}, D0 value: {value}")



print("FCSC{"+''.join([i[1] for i in d0_values])+"}")
```
So I only needed to execute
 python extract.py very-cute-data.vcd
