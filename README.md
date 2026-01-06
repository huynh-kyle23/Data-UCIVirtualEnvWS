# Data-UCIVirtualEnvWS


This repository is a simple workspace for learning how to set up and use Python virtual environments (`venv`) on **Windows** and **macOS**, along with installing dependencies using `requirements.txt`.

---

## 📦 Prerequisites
- Python **3.8+** installed  
- Verify Python installation:
```bash
python --version
# or
python3 --version
```

---

## 🐍 Creating a Virtual Environment

### Windows (Command Prompt or PowerShell)
```bash
python -m venv data@UCI
```

### macOS (Terminal)
```bash
python3 -m venv data@UCI
```

This creates a folder called `data@UCI` that contains an isolated Python environment for this project.
For our case, that is what we will be calling our new venv!

---

## ▶️ Activating the Virtual Environment

### Windows

**Command Prompt**
```bash
data@UCI\Scripts\activate
```

**PowerShell**
```powershell
data@UCI\Scripts\Activate.ps1
```

> If activation is blocked in PowerShell, run:
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

### macOS
```bash
source data@UCI/bin/activate
```

---

### ✅ How to know it worked
Your terminal prompt will look like:
```text
(data@UCI)
```

---

## ⏹ Deactivating the Virtual Environment
```bash
deactivate
```

---

## 📄 Installing Dependencies from `requirements.txt`

Make sure the virtual environment is **activated first**, then run:
```bash
pip install -r requirements.txt
```

If `pip` causes issues, use:
```bash
python -m pip install -r requirements.txt
```

---

## 🔍 Useful Commands

Check installed packages:
```bash
pip list
```

Save installed packages:
```bash
pip freeze > requirements.txt
```

Check which Python is being used:
```bash
where python   # Windows
which python   # macOS
```

---

## 🧹 Removing the Virtual Environment
To delete the virtual environment, simply remove the folder:
```bash
rm -rf data@UCI        # macOS
rmdir /s data@UCI      # Windows
```

---

## ✅ Best Practices
- Use **one virtual environment per project**
- Name it `venv` or `.venv`
- Activate the venv **before installing packages**
- Add `venv/` or `.venv/` to `.gitignore`

---

Happy coding! 🎉
