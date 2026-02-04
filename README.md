# 📦 Odoo 16 Custom Development Environment

This repository contains a clean development workspace for building custom modules for Odoo 16 Community.

It includes only:

- Custom addons
- Configuration files
- Setup instructions
- Module documentation

It **does NOT include**:

- Odoo core source code
- Python virtual environment
- Databases

These must be created locally.

---

# 📁 Repository Structure

```
project/
│
├── addons-custom/        → Custom Odoo modules only
│   └── itsm_support/     → ITSM/Helpdesk module
│       └── docs/         → Technical documentation
│
├── config/               → odoo.conf
├── requirements.txt      → Python dependencies
│
├── odoo/                 → (local only, NOT committed)
├── venv/                 → (local only, NOT committed)
└── README.md
```

---

# 📚 Module Documentation

Each custom addon contains its **own technical documentation** inside a `docs/` folder.

## Available Modules

### 🔹 itsm_support (ITSM / Helpdesk)

Features:

- Website ticket submission
- Portal ticket tracking
- Backend ticket management
- Teams & stages workflow
- Attachments/screenshots

Documentation location:

```
addons-custom/itsm_support/docs/
```

Start reading here:

```
addons-custom/itsm_support/docs/README.md
```

Contains:

- Functional guide
- Technical architecture
- Models
- Controllers
- Security
- Views
- Installation
- Deployment
- Customization guide
- API reference

---

# ⚙️ Setup Instructions

## 1. Clone repository

```
git clone git@github.com:Rahma-AlWadhahi/odoo16.git
cd project
```

---

## 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Download Odoo 16 source

```
git clone https://github.com/odoo/odoo.git -b 16.0 odoo
```

IMPORTANT:  
Folder must be named exactly:

```
odoo/
```

---

## 5. Run Odoo

```
./odoo/odoo-bin -c config/odoo.conf
```

---

# 🧩 Adding New Custom Modules

When creating a new addon:

Place it inside:

```
addons-custom/
```

Recommended structure:

```
my_module/
├── models/
├── views/
├── controllers/
├── security/
├── data/
└── docs/   ← always include documentation
```

Each module should:

- be self-contained
- include its own docs
- not depend on local paths

---

# 🚫 Git Rules

Never commit:

```
venv/
odoo/
*.pyc
__pycache__/
```

Only commit:

- custom addons
- configs
- documentation

---

# ✅ Best Practices

- One feature = one module
- Keep business logic in models
- Keep controllers thin
- Always document in `/docs`
- Test on a clean database
