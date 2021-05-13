# Generating bcrypt passwords
This script generates bcrypt passwords using 10 rounds and the prefix 2a, it works with some project where I was working.

## Installation
Please follow this instructions.

```shell
sudo apt install -y python3 python3-pip
sudo python3 -m pip install -U pip virtualenv
git clone https://github.com/elshaio/bcrypt_gen
cd bcrypt_gen 
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Use
Just run this command
```shell
# Only once
source venv/bin/activate

# This generates the string
python main.py [your password here]
```
