# DSA210-Project
# Celebrity & Influencer Scandals and Their Impact on Brand Interest

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
## Hypotheses

H1: Celebrity scandal events lead to a short term increase in public search interest for the associated brand.

H2: Celebrity scandal events lead to a short-term decrease in public search interest for the associated brand.

H3: The direction and magnitude of the effect vary depending on the type of celebrity, industry context, and event characteristics.

H0: There is no significant change in public search interest following celebrity related scandal events.

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
