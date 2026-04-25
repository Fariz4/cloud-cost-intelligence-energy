{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ad75856e-01d7-4127-82cf-26aa0461f172",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\more\\anaconda3\\lib\\site-packages (2.3.3)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\more\\anaconda3\\lib\\site-packages (from pandas) (2.3.5)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\more\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\more\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\more\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\more\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "35456267-ff49-47c8-9231-3b95c4a4ca0a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Total Cost: 29.5\n",
      "\n",
      "Cost by Energy:\n",
      " energy_type\n",
      "Grid     15.0\n",
      "Solar    10.0\n",
      "Wind      4.5\n",
      "Name: total_cost, dtype: float64\n",
      "\n",
      "Cost by Service:\n",
      " service\n",
      "Compute    25.0\n",
      "Storage     4.5\n",
      "Name: total_cost, dtype: float64\n",
      "\n",
      "Anomalies:\n",
      " Empty DataFrame\n",
      "Columns: [timestamp, service, energy_type, usage_hours, cost_per_hour, total_cost]\n",
      "Index: []\n",
      "\n",
      "Idle Resources:\n",
      " Empty DataFrame\n",
      "Columns: [timestamp, service, energy_type, usage_hours, cost_per_hour, total_cost]\n",
      "Index: []\n",
      "\n",
      "Results saved to: output\\cost_analysis_output.xlsx\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "class EnergyCloudCostCalculator:\n",
    "    def __init__(self, file_path):\n",
    "        self.file_path = file_path\n",
    "        self.df = None\n",
    "\n",
    "    def load_data(self):\n",
    "        if not os.path.exists(self.file_path):\n",
    "            raise FileNotFoundError(f\"File not found: {self.file_path}\")\n",
    "\n",
    "        self.df = pd.read_excel(self.file_path)\n",
    "        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])\n",
    "\n",
    "    def process_data(self):\n",
    "        self.df['total_cost'] = self.df['usage_hours'] * self.df['cost_per_hour']\n",
    "\n",
    "    def total_cost(self):\n",
    "        return self.df['total_cost'].sum()\n",
    "\n",
    "    def cost_by_energy(self):\n",
    "        return self.df.groupby('energy_type')['total_cost'].sum()\n",
    "\n",
    "    def cost_by_service(self):\n",
    "        return self.df.groupby('service')['total_cost'].sum()\n",
    "\n",
    "    def detect_anomalies(self):\n",
    "        threshold = self.df['total_cost'].mean() * 2\n",
    "        return self.df[self.df['total_cost'] > threshold]\n",
    "\n",
    "    def detect_idle_resources(self):\n",
    "        return self.df[self.df['usage_hours'] < 1]\n",
    "\n",
    "    def export_results(self):\n",
    "        os.makedirs(\"output\", exist_ok=True)\n",
    "\n",
    "        output_path = os.path.join(\"output\", \"cost_analysis_output.xlsx\")\n",
    "\n",
    "        with pd.ExcelWriter(output_path) as writer:\n",
    "            self.df.to_excel(writer, sheet_name=\"Processed Data\", index=False)\n",
    "            self.cost_by_energy().to_excel(writer, sheet_name=\"Cost by Energy\")\n",
    "            self.cost_by_service().to_excel(writer, sheet_name=\"Cost by Service\")\n",
    "\n",
    "        print(\"\\nResults saved to:\", output_path)\n",
    "\n",
    "    def run(self):\n",
    "        self.load_data()\n",
    "        self.process_data()\n",
    "\n",
    "        print(\"\\nTotal Cost:\", self.total_cost())\n",
    "        print(\"\\nCost by Energy:\\n\", self.cost_by_energy())\n",
    "        print(\"\\nCost by Service:\\n\", self.cost_by_service())\n",
    "\n",
    "        print(\"\\nAnomalies:\\n\", self.detect_anomalies())\n",
    "        print(\"\\nIdle Resources:\\n\", self.detect_idle_resources())\n",
    "\n",
    "        self.export_results()\n",
    "\n",
    "file_path =r\"C:\\Users\\More\\OneDrive\\Documents\\GitHub\\cloud-cost-intelligence-energy\\data\\sample_data.xlsx\"\n",
    "\n",
    "calculator = EnergyCloudCostCalculator(file_path)\n",
    "calculator.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3676c355-9ccd-47cd-901e-73a7c560fa42",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
