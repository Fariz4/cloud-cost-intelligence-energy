# 🌩️ Cloud Cost Intelligence Platform for Energy

## 📌 Overview
This project is a Python-based system that analyzes cloud usage data and calculates energy-related costs. It helps in understanding cost distribution, detecting anomalies, and identifying idle resources.

---

## 🎯 Aim
To build a cost analysis tool that provides insights into cloud energy usage and helps optimize expenses.

---

## ⚙️ Technologies Used
- Python
- Pandas
- Matplotlib
- OpenPyXL
- Jupyter Notebook

---

## 📁 Project Structure
cloud-cost-intelligence-energy/
│
├── src/
│   └── energy_cost_calculator.py
│
├── notebook/
│   └── energy_analysis.ipynb
│
├── data/
│   └── sample_data.xlsx
│
├── output/
│   └── cost_analysis_output.xlsx
│
├── README.md
└── requirements.txt

---

## 📥 Input
The system takes an Excel file with the following columns:
- timestamp  
- service  
- energy_type  
- usage_hours  
- cost_per_hour  

---

## 🔄 Process
- Load data from Excel  
- Clean and process data  
- Calculate total cost  
- Analyze cost by energy type and service  
- Detect anomalies (high cost)  
- Detect idle resources (low usage)  

---

## 📊 Output
The system generates an Excel file:

output/cost_analysis_output.xlsx

This file contains:
- Processed Data  
- Cost by Energy  
- Cost by Service  

---

## 🚀 How to Run

### 1. Install dependencies
pip install pandas matplotlib openpyxl

### 2. Run the Python script
python src/energy_cost_calculator.py

### 3. Run the Notebook (optional)
Open:
notebook/energy_analysis.ipynb

---

## ✨ Features
- Cost calculation  
- Energy-wise analysis  
- Service-wise analysis  
- Anomaly detection  
- Idle resource detection  
- Excel report generation  

---

## 📌 Conclusion
This project provides a simple and effective way to analyze cloud energy costs and identify optimization opportunities.

---

## 🔮 Future Scope
- Dashboard visualization  
- Real-time data integration  
- Cloud API integration  
- Advanced analytics  

---

## 👨‍💻 Author ##
Fariz U