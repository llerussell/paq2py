# paq2py
PackIO, a National Instruments DAQ interface written by Adam Packer is used to synchronise and record inputs and outputs from multiple National Instruments devices. The recorded data is saved as binary 'PAQ' files. This python module reads in PAQ files and returns the data as a channel-by-samples numpy array. Channel names, hardware lines and acquisition settings are also returned.

#### dependencies
* numpy
* matplotlib (optional)

#### install
```
cd ~
git clone https://github.com/llerussell/paq2py.git
cd paq2py
python setup.py build
sudo python setup.py install
cd ~
```

#### example usage
```ruby
import paq2py

input_path = '/path/to/paqfile.paq'
paq = paq2py.paq_read(input_path, plot=True)

# channel 0 name
paq['chan_names'][0]

# channel 0 data
paq['data'][0]
```
