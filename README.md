# DSA210-Project
# Celebrity & Influencer Scandals and Their Impact on Brand Interest

## Project Overview
This project analyzes how celebrity and influencer-related scandals affect public interest in associated brands using Google Trends data. The goal is to compare different types of scandals and measure how search behavior changes before and after major events.

The study includes three cases with different levels of severity and context:
1. Kanye West – Adidas partnership termination
2. Sydney Sweeney – American Eagle related public controversy
3. Dilan Polat – Beauty business scandal and financial controversy in Türkiye

---

## Research Question
How do different types of celebrity and influencer scandals affect brand-related search interest, and how does the impact vary across global celebrities, Hollywood actors, and social media influencers?

---
## Hypotheses
- H1: Celebrity scandals increase the public interest of their associated brand
- H2: Celebrity scandals decrease the public interest of their associated brand
- H0 (Null): Celebrity scandals have no significant relationship with the public interest of their associated brand
---

## Data Source
Data was collected from:
- Google Trends (Worldwide / regional search interest)
- Time series data for selected keywords

Keywords used:
- Kanye West, ADIDAS(Yeezy)
- Sydney Sweeney, American Eagle
- Tiger Woods, Nike

---

## Methodology

### 1. Data Collection
Google Trends data was collected for each case over an event-centered time window.

### 2. Event Study Approach
Each scandal is analyzed using a before-and-after comparison around the event date.

### 3. Explarotoary Data Analysis (EDA)
- Time series visualization
- Spike detection around the event dates
- Comparative trend analysis across cases

### 4. Statistical Analysis
- Before vs after mean comparison
- Change in search interest levels
- Cross-case comparison of impact magnitude

---

## Case 1: Kanye West – Adidas
1st case analyzes the termination of the Adidas Kanye West partnership in October 2022.

Findings:
- Significant spike in search interest for Kanye West after the event.
- Adidas shows a moderate increase in attention.
- Yeezy shows mixed or declining interest.

This suggests that attention is primarily concentrated on the individual rather than fully transferring to the brand.

---

## Case 2: Sydney Sweeney – American Eagle Controversy
A notable co-movement is observed between Sydney Sweeney and American Eagle search interest between July 27 and August 3, 2025. During this period, both series show synchronized spikes in attention. This indicates a potential attention spillover effect, where increased interest in the celebrity is closely associated with increased interest in the brand. Unlike the Kanye–Adidas case, the effect here appears more balanced and simultaneous.

## Case 3: Tiger Woods - Nike
3rd case examines the impact of the Tiger Woods personal scandal in late 2009 on search interest for both the athlete and Nike.
An event window (October 2009 – February 2010) is used to compare pre and post scandal behavior. The analysis includes time series visualization, correlation, and a t-test. Results show a clear spike in Tiger Woods search interest around December 2009. Nike also shows smaller fluctuations during the same period, indicating a possible spillover effect.
However, the t-test shows no statistically significant difference in mean search interest before and after the event (p > 0.05). This suggests that while short-term attention spikes exist, the long-term impact on average interest is limited.

Overall, the results indicate weak but observable co-movement between Tiger Woods and Nike during the scandal period.

## Key Findings (Cross-Case Comparison)

- Corporate scandals (Kanye–Adidas) create strong but structured brand-level effects.

---

## Limitations
- Google Trends reflects search interest, not actual sales or revenue (since those are private data).
- Causal relationships cannot be fully confirmed.
- Event timing is approximated based on public information.

---

## Future Work
- Incorporating social media sentiment analysis (Twitter/Reddit)
- Adding stock market data for financial impact
- Expanding dataset with more international influencer cases

---

## Tools Used
- Python (Pandas, Matplotlib)
- Google Trends
- Exploratory Data Analysis techniques
- AI (only for educational purposes)
