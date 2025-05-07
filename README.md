# fda-510k-analysis
Analyze trends and decision metrics from over 100K FDA 510(k) device approvals.

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

## 🚀 Features
- Time-to-decision analysis
- Trends by product code, advisory committee, decision type
- Clean visualizations for strategic insights

## 🛠️ Technologies

- Python (Pandas, Matplotlib, Seaborn)
- Jupyter Notebook (via VSCode)
- Git/GitHub for version control and sharing

## 📁 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fda-device-analysis.git
   cd fda-device-analysis

2. Install dependencies
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows
   pip install -r requirements.txt

3. jupyter notebook
# Open notebooks/exploratory_analysis.ipynb


##Average Decision Time by Product Code [sample]
| PRODUCTCODE | count |   mean |    std | min | 25% |   50% |    75% |  max |
| :---------- | ----: | -----: | -----: | --: | --: | ----: | -----: | ---: |
| DXN         |  1168 | 136.21 | 111.00 |   3 |  56 |   107 | 195.25 |  860 |
| DZE         |  1480 | 202.52 | 172.23 |   3 |  88 | 153.5 | 266.25 | 1440 |
| ...         |       |        |        |     |     |       |        |      |

🧪 Testing
Run tests with:
pytest tests/

🔗 Data Source
* U.S. FDA 510(k) Premarket Notification
* Optionally enriched via OpenFDA API


