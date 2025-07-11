# FFTea

The code in craft_signal.py applies the inverse [Fourier Transform](https://en.wikipedia.org/wiki/Fourier_transform) on the bytes it reads from the flag.txt. So we only need to apply the Fourier Transform on the fftea data.
This code thus recovers the flag : 
```python
import numpy as np

# Load the data from the "fftea" file
data = np.fromfile("challenge", dtype = np.complex64)
data = np.fromfile("fftea", dtype = np.complex64)

# Perform Fourier transform
original_data = np.fft.fft(data, n=64)

# Convert the complex64 array to bytes
flag = original_data.real.astype(np.complex64)
int_array = np.array([int(c.real) for c in flag])
aa = [chr(i) for i in int_array]
print(''.join(aa))
```
