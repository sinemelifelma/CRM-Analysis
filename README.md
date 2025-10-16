# OmniChannel CRM Analysis (RFM Segmentation)

## 🎯 Objective
This project applies **RFM (Recency, Frequency, Monetary)** analysis to segment FLO’s OmniChannel customers (those shopping both online and offline) and uncover actionable insights for data-driven marketing.

---

## 📊 Dataset
The dataset contains records of customers who made their last purchases between **2020–2021**.

| Feature | Description |
|----------|-------------|
| `master_id` | Unique customer ID |
| `order_channel` | Purchase channel (Android, iOS, Desktop, Mobile, Offline) |
| `first_order_date` / `last_order_date` | Dates of first and last purchases |
| `order_num_total_ever_online/offline` | Total online/offline purchases |
| `customer_value_total_ever_online/offline` | Total online/offline spending |
| `interested_in_categories_12` | Purchased categories in the last 12 months |

---

## 🧠 Methodology
1. **Data Preparation**
   - Created `total_order_number` and `total_customer_value`
   - Converted date columns to `datetime`
   - Analyzed order and spending patterns by channel

2. **RFM Calculation**
   - Defined analysis date: `2021-06-01`
   - Computed `Recency`, `Frequency`, and `Monetary` metrics

3. **RFM Scoring**
   - Used `pd.qcut` to assign 1–5 scores for each metric
   - Combined into `RFM_SCORE` and `RF_SCORE`

4. **Segmentation**
   - Mapped scores to interpretable customer segments:
     *Champions, Loyal Customers, At Risk, Hibernating,* etc.

5. **Actionable Insights**
   - Exported customer lists for:
     - New women’s shoe brand promotion  
     - Men’s and kids’ product discount campaign

---

## 🧩 Tools
- Python (pandas, numpy, seaborn, datetime)
- Jupyter Notebook
- Kaggle

---

## 🚀 Results
- Identified 10 behavioral customer segments  
- Built actionable target lists for marketing  
- Improved data-driven decision-making for retention and growth  

---

## 🔗 Links
- [📖 Medium Article]([https://medium.com/@yourusername](https://medium.com/@sinemelifelma/customer-segmentation-with-rfm-understanding-omnichannel-shopping-behavior-through-data-3d46a8ef80b0)
- [💻 Kaggle Notebook](https://www.kaggle.com/code/sinemelifelma/omnichannel-crm-analysis-rfm-segmentation)
- [📂 GitHub Repository](https://github.com/yourusername/OmniChannel_CRM_Analysis)

