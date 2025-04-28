# 📊 Power BI DAX Measures (Customer Lifecycle Lakehouse)

---

## 🏷️ Revenue Metrics

### Total Revenue
```dax
Total Revenue = SUM('FactTransactions'[Amount])
```

### Revenue by Product Category
```dax
Revenue by Category = 
SUMX(
    SUMMARIZE('FactTransactions', 'DimProduct'[Category], "CategoryRevenue", SUM('FactTransactions'[Amount])),
    [CategoryRevenue]
)
```

### Monthly Revenue Trend
```dax
Monthly Revenue = 
CALCULATE(
    [Total Revenue],
    DATESMTD('DimTime'[Date])
)
```

---

## 👥 Customer Lifecycle Metrics

### Churn Rate (%)
```dax
Churn Rate (%) = 
DIVIDE(
    CALCULATE(COUNTROWS('DimCustomer'), 'DimCustomer'[LifecycleStage] = "Churned"),
    COUNTROWS('DimCustomer')
)
```

### Retention Rate (%)
```dax
Retention Rate (%) = 
1 - [Churn Rate (%)]
```

### New Customer Cohort Count
```dax
New Customers (YTD) = 
CALCULATE(
    COUNTROWS('DimCustomer'),
    'DimCustomer'[LifecycleStage] = "Active",
    DATESYTD('DimTime'[Date])
)
```

### Churned Customers This Quarter
```dax
Churned Customers (QTD) =
CALCULATE(
    COUNTROWS('DimCustomer'),
    'DimCustomer'[LifecycleStage] = "Churned",
    DATESQTD('DimTime'[Date])
)
```

---

## 🎯 Engagement Metrics

### Average Engagement Score
```dax
Avg Engagement Score = AVERAGE('FactEngagement'[EngagementScore])
```

### High Engagement Customer Count
```dax
High Engagement Customers = 
CALCULATE(
    COUNTROWS('DimCustomer'),
    'FactEngagement'[EngagementScore] > 100
)
```

---

## 📈 Goal Tracking Metrics

### Goal Achievement Rate (MRR)
```dax
Goal Achievement Rate (MRR) = 
DIVIDE(
    CALCULATE(SUM('FactGoalTracking'[Actual]), 'FactGoalTracking'[Metric] = "MRR"),
    CALCULATE(SUM('FactGoalTracking'[Target]), 'FactGoalTracking'[Metric] = "MRR")
)
```

### Quarterly Goal Achievement (%)
```dax
Quarterly Goal Achievement (%) =
VAR SelectedQuarter = SELECTEDVALUE('FactGoalTracking'[Timeframe])
RETURN
DIVIDE(
    CALCULATE(SUM('FactGoalTracking'[Actual]), 'FactGoalTracking'[Timeframe] = SelectedQuarter),
    CALCULATE(SUM('FactGoalTracking'[Target]), 'FactGoalTracking'[Timeframe] = SelectedQuarter)
)
```

---

## 🔮 Forecasting

### Revenue Forecast (Next Quarter)
```dax
Revenue Forecast (Next Quarter) = 
VAR LastQuarterRevenue = 
    CALCULATE(
        [Total Revenue],
        DATESINPERIOD('DimTime'[Date], MAX('DimTime'[Date]), -1, QUARTER)
    )
RETURN
LastQuarterRevenue * 1.05  // Assuming 5% growth
```

### Churn Forecast (Next Month)
```dax
Churn Forecast (Next Month) = 
VAR LastMonthChurn = 
    CALCULATE(
        [Churn Rate (%)],
        DATESINPERIOD('DimTime'[Date], MAX('DimTime'[Date]), -1, MONTH)
    )
RETURN
LastMonthChurn * 1.02  // Assuming slight increase
```

---

## 🗓️ Time Intelligence

### YTD Revenue
```dax
YTD Revenue = 
CALCULATE(
    [Total Revenue],
    DATESYTD('DimTime'[Date])
)
```

### QTD Engagement Score
```dax
QTD Engagement Score = 
CALCULATE(
    [Avg Engagement Score],
    DATESQTD('DimTime'[Date])
)
```

---
