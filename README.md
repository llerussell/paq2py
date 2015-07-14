# paq2py
PackIO, a National Instruments DAQ interface written by Adam Packer is used to record multiple channels on NI acquisition devices. The recorded data is saved as binary 'PAQ' files. This python module reads in PAQ files and returns the data as a numpy array. Channel names and hardware and acquisition information are also returned.

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
input_file = '/path/to/file.paq'
paq2py.paq_read(input_file, plot=True)
```
