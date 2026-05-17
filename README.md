# DSA210-Project
# Celebrity & Influencer Scandals and Their Impact on Brand Interest

## Motivation

Celebrity culture plays a significant role in shaping public attention and consumer behavior in modern digital environments. Scandals and viral moments involving public figures often generate rapid shifts in online engagement, which may indirectly influence brand perception and financial outcomes.

I was particularly interested in how recent cases such as the Sydney Sweeney American Eagle attention dynamics highlighted noticeable changes in public interest patterns, especially when compared to KATSEYE’s brand partnership activity with GAP Denim.

These contrasting cases raised a key question: whether such attention movements are purely short term social media effects or whether they can be systematically observed and potentially linked to measurable changes in brand related behavior.

By combining Google Trends data with stock market information, I aim to explore the relationship between public attention and market dynamics across different types of celebrity-brand interactions.

## Project Overview
This project analyzes how celebrity and influencer-related scandals affect public interest in associated brands using Google Trends data. The goal is to compare different types of scandals and measure how search behavior changes before and after major events.

The study includes three cases with different levels of severity and context:
1. Kanye West – Adidas partnership termination
2. Sydney Sweeney – American Eagle related public controversy
3. Tiger Woods - Nike sponsorship during personal scandal

---

## Research Question
How do different types of celebrity and influencer scandals affect brand-related search interest, and how does the impact vary across global celebrities?

---

## Hypotheses Summary

| Hypothesis | Description | Interpretation | Result |
|------------|-------------|----------------|--------|
| H1 | Celebrity scandal events lead to short-term increases in public search interest for associated brands | Short-term spikes in search interest are observed in all cases, especially around event periods | Partially Supported |
| H2 | Celebrity scandal events lead to short-term decreases in public search interest depending on context | No consistent or systematic decrease in search interest is observed across cases | Not Supported |
| H3 | The direction and magnitude of the effect vary depending on celebrity type, industry context, and event characteristics | Strong variation is observed across cases (Kanye vs Sydney vs Tiger), confirming heterogeneous effects | Supported |
| H0 | There is no significant change in public interest following scandal events | Statistically significant changes are observed in at least some cases (e.g. Kanye, Sydney), but not all | Rejected (partially) |
---

## Data Source
Data was collected from:
- Google Trends (Worldwide search interest)
- Yahoo Finance
- Time series data for selected keywords

Keywords used:
- Kanye West, ADIDAS(Yeezy)
- Sydney Sweeney, American Eagle
- Tiger Woods, Nike

---

## Methodology

### 1. Data Collection
Google Trends data was collected for each case over an event-centered time window.
Brand stock market data from Yahoo Finance was collected over the scandal time

### 2. Event Study Approach
Each case is analyzed using an event-study framework, focusing on changes in search interest and market related variables within a defined time window (preevent vs postevent periods).

### 3. Explarotoary Data Analysis (EDA)
- Time series visualization of Stock Market and Google Trends
- Spike detection around the event dates
- Cross case comparison of attention dynamics

### 4. Statistical Analysis
- Preevent vs postevent mean comparison of search interest
- Independent sample t-tests to evaluate statistical significance of changes
- Correlation analysis between celebrity attention and brand interest
- Comparison of effect size and direction across different cases

### 5. Machine Learning Analysis
- Linear regression to evaluate relationship strength between search interest and stock movement
- Logistic regression for direction prediction (increase/decrease in market response)
- Decision tree models to capture non-linear relationships
- Evaluation using R2 , accuracy, and feature importance metrics across all 3 cases
---

## Case 1: Kanye West – Adidas
The first case analyzes the termination of the Adidas–Kanye West partnership in October 2022 using Google Trends and stock market data within an event study framework.

### Findings:
- A strong and immediate spike in search interest for Kanye West is observed following the scandal event.
- Adidas shows a moderate increase in attention.
- Yeezy related search interest exhibits mixed and unstable behavior across the event window.

### Statistical Results:
- Before vs after comparison shows a **statistically significant change** in mean search interest:
  - t-statistic = 3.46
  - p value = 0.00103
- Linear regression results indicate **extremely weak explanatory power** :
  - R² = 0.00115

### Machine Learning Results:
- Logistic Regression:
  - Train accuracy = 0.7727
  - Test accuracy = 0.2632
  - Indicates strong **overfitting and weak generalization** performance.

### Interpretation:
Although the statistical test indicates a significant short-term change in attention (p < 0.01), the regression results show that this change does not translate into a stable or predictive relationship with market behavior. The very low R² value suggests that the model explains almost none of the variance in the data, reinforcing the conclusion that attention spikes are short-term and non-predictive in nature.

---

## Case 2: Sydney Sweeney – American Eagle
The 2nd case analyzes the relationship between Sydney Sweeney related public attention and American Eagle using Google Trends and stock market data within an event study framework (July-August 2025).

### Findings:
- A clear synchronized spike is observed between Sydney Sweeney and American Eagle search interest between July 27 and August 3, 2025.
- Unlike the Kanye case, both the celebrity and brand exhibit more balanced and simultaneous attention dynamics, indicating a potential spillover effect.

### Statistical Results:
- Before vs after comparison shows a **statistically significant change** in mean search interest:
  - t-statistic = -12.74
  - p-value = 0.0000002088
- Linear regression results show **moderate explanatory power**:
  - R2 = 0.635

### Machine Learning Results:
- Logistic/linear modeling indicates moderate predictive performance:
  - Train accuracy = 0.875
  - Test accuracy = 0.50

### Interpretation:
The results indicate a stronger and more structured relationship between celebrity attention and brand interest compared to the first case. The relatively high R2 suggests that a meaningful portion of variance is explained, although predictive stability remains limited in out-of-sample performance.

## Case 3: Tiger Woods – Nike
The third case analyzes the impact of Tiger Woods’ personal scandal (late 2009) on search interest and its relationship with Nike using Google Trends & Stock Market and regression analysis.

An event window (October 2009 – February 2010) is used to compare preevent and postevent behavior.

### Findings:
- A clear spike in search interest for Tiger Woods is observed around the scandal period (December 2009).
- Nike shows minor fluctuations during the same period, but the reaction is weaker compared to the other cases.
- Overall, the relationship between Tiger Woods and Nike is less structurally pronounced.

### Statistical Results:
- Before vs after comparison:
  - t-statistic = -1.02
  - p-value = 0.3201
- These results indicate **no statistically significant difference** in mean search interest before and after the event.

### Machine Learning / Regression Results:
- Linear regression results show **very weak explanatory power**:
  - R² = 0.0504
- Model coefficients:
  - Coefficient = 0.000386
  - Intercept = -0.010745
- Logistic/ML results suggest limited predictive capability and weak generalization.

### Interpretation:
Unlike the Kanye and Sydney cases, the Tiger Woods and Nike relationship does not show statistically significant long term structural change. While short term attention spikes do exist, they dont translate into meaningful or predictive shifts in search interest or market-related behavior.

## Key Findings (Cross Case Comparison)

- Celebrity scandal effects are highly heterogeneous across different individuals and industries, rather than uniform or predictable.

  Kanye West -> Adidas case shows strong short term attention spikes accompanied by statistically significant changes in search interest (p ≈ 0.001), but extremely weak explanatory power (R² ≈ 0.001), indicating no stable predictive relationship.

 Sydney Sweeney –> American Eagle case exhibits both statistically significant effects (p ≈ 0.0000002) and moderate explanatory power (R² ≈ 0.635), suggesting a stronger and more structured attention spillover between celebrity and brand.

 Tiger Woods –> Nike case shows no statistically significant long term effect (p ≈ 0.320), and weak explanatory power (R² ≈ 0.05), indicating that observed attention spikes do not translate into structural changes.

- Overall, results indicate that while attention shocks are consistently observed around scandal events, their translation into measurable brand or market effects depends heavily on context, celebrity brand coupling, and event characteristics.

## Hypothesis Evaluation

H1: Partially supported  
Celebrity scandal events often lead to short-term increases in public search interest, but this effect is not consistent across all cases.

H2: Not supported as a general rule  
While some cases show decreases or weak effects, there is no consistent evidence of systematic short-term decrease in search interest.

H3: Supported  
The direction and magnitude of the effect vary significantly depending on the celebrity, industry context, and event characteristics.

H0: Rejected in part  
The null hypothesis of no change is rejected for cases with strong statistical significance (e.g., Kanye West and Sydney Sweeney), but not for all cases (e.g., Tiger Woods).

## Setup and Reproducibility

### Requirements
This project uses Python 3 and the following libraries:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy
- yfinance
- pytrends

Install all dependencies using:
```bash
pip install -r requirements.txt

## Installation
Clone the repository:

git clone https://github.com/kaanadaleti/DSA210-Project.git
cd DSA210-Project

## Running the Project

Open the project using Jupyter Notebook or VS Code.

Run the notebooks in the following order:

1. EDA / Analysis

notebooks/analysiskanye.ipynb
notebooks/analysissydney.ipynb
notebooks/analysistiger.ipynb

2. Stock Analysis

notebooks/stock_analysis/kanyestock.ipynb
notebooks/stock_analysis/sydneystockgercek.ipynb
notebooks/stock_analysis/analysistigerstock.ipynb

3. Machine Learning

notebooks/ml_analysis.ipynb

## Data

All datasets are included in the data/ folder.
No external data collection is required to reproduce results.

## Project Structure

DSA210-Project/

├── notebooks/
│   ├── analysiskanye.ipynb              # Kanye West & Adidas EDA analysis
│   ├── analysissydney.ipynb             # Sydney Sweeney & American Eagle EDA analysis
│   ├── analysistiger.ipynb              # Tiger Woods & Nike EDA analysis
│   ├── ml_analysis.ipynb                # Unified machine learning models
│   │
│   └── stock_analysis/
│       ├── kanyestock.ipynb            # Kanye stock & trends analysis
│       ├── sydneystockgercek.ipynb     # Sydney stock & trends analysis
│       ├── analysistigerstock.ipynb    # Tiger Woods stock & trend analysis
│
├── data/
│   ├── adidas_kanye_yeezy_trends.csv
│   ├── SydneyAmerican.csv
│   ├── tigerwoods.csv
│
├── figures/
│
├── README.md
├── .gitignore
└── dsa210 project proposal.pdf

## Limitations

- Google Trends data captures relative search interest rather than direct economic outcomes such as sales, revenue, or market capitalization, which are not publicly available at the same granularity.

- The analysis is based on observational data, meaning that causal relationships between celebrity scandals and brand/market behavior cannot be definitively established.

- Event timing is approximated using publicly reported dates, which may introduce measurement noise in defining the exact pre and post event windows.

- Machine learning models show limited generalization ability across cases, indicating that predictive performance is sensitive to feature selection and dataset structure.

## Tools Used

- Python (Pandas, NumPy, Matplotlib, Seaborn)
- Google Trends API (via Pytrends)
- Yahoo Finance data
- Scikit learn (Linear Regression, Logistic Regression, Decision Trees)
- SciPy (Statistical tests including t-test)
- Exploratory Data Analysis (EDA) techniques
- AI tools (used only for educational and documentation support purposes)
