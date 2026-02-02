#!/bin/bash

echo "Creating virtualenv..."
python3 -m venv venv
source venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Cloning Odoo 16..."
git clone -b 16.0 --single-branch https://github.com/odoo/odoo.git odoo

echo "Done!"
