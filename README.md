# fda-510k-analysis
Utilizing basic data analysis techniques to review a new dataset and gain insights

This project analyzes U.S. FDA 510(k) medical device submissions using historical data to identify regulatory trends, decision timelines, and specialty-specific patterns. The goal is to provide insights into how different product categories and medical specialties influence review outcomes and durations.

## 📊 Dataset Overview

- **Source:** FDA 510(k) public release datasets.
- **Files Used:**
  - `Basecamp_combined_cleansed.csv`: Combined historical device submission records.
  - `Medical Specialties.csv`: Mapping of FDA advisory committee codes to medical specialties.

Each record includes information such as:
- Submission and decision dates
- Applicant and product code
- Decision type (e.g., SESE, DENG)
- Advisory committee (medical specialty)

## 🔍 Key Analyses

- **Trend Analysis**: Submission volume and average review time over the years.
- **Decision Outcomes**: Distribution of FDA decision types across specialties.
- **Product Categorization**: Most frequent product codes and their specialty mapping.
- **Specialty Focus**: Deep dive into top 5 medical specialties:
  - Cardiovascular
  - General & Plastic Surgery
  - General Hospital
  - Orthopedic
  - Radiology

## 📈 Insights

- **Submission Growth**: Cardiovascular and Radiology device submissions show steady growth, reflecting technological advancement.
- **Regulatory Timing**: Devices in Cardiovascular tend to have longer review times.
- **High Clearance Rate**: Most submissions fall under "Substantially Equivalent - SESE".
- **Product Code Concentration**: A small number of product codes dominate within each specialty.

## 🛠️ Technologies

- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook (via VSCode)
- Git/GitHub for version control and sharing

## 📁 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fda-device-analysis.git
   cd fda-device-analysis
