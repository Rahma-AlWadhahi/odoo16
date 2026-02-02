# Odoo 16 Custom Development Environment

This repository contains only:

- Custom addons
- Configuration
- Setup instructions

It DOES NOT include:

- Odoo source code
- Python virtual environment

You must create them locally.

---

## Folder Structure

addons-custom/ → custom modules  
config/ → odoo.conf  
odoo/ → (local only, not committed)  
venv/ → (local only, not committed)

---

## Setup Instructions

### 1. Clone repository

git clone <repo-url>
cd project

---

### 2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Download Odoo 16 source

git clone https://github.com/odoo/odoo.git -b 16.0 odoo

IMPORTANT:
Folder must be named exactly: odoo

---

### 5. Run Odoo

./odoo/odoo-bin -c config/odoo.conf

---

## Notes

- Never commit venv/
- Never commit odoo/
- Only commit custom addons
