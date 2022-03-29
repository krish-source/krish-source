## Business case:



A Retail company based in US requests to analyze & get insights on their sales database for years between 2018 to 20 

*Data source*: https://data.world/dataman-udit/us-regional-sales-data

### Report Summary:

Sales analysis insights dashboard is built to provide quantifiable insights to senior stakeholders about sales trends & aid the management in making data driven decision making  



### Report Requirements:  

- Top Selling Product category 2018 Q2 to 2020 Q4
- Top Customers contributing to yearly sales 2018 Q2 to 2020 Q4
- % Profit margins across 2018 Q2 to 2020 Q4
- Sales generation months not meeting company KPI (<$2600000)
- Revenue Analysis -Root cause analysis
- Major Influencers contributing to Sales
- Sales & Profit margin trend with supporting data
- Top performing Sales Teams & their respective Sparkline's, sales & profit contribution
- Sales Team not meeting KPI goal (<=$2900000)
- Anomaly events (if any) & their deep dive analysis 
- Bookmarks & Navigation
- Tool tips visual 
- Map visuals 
- Improved Presentations



### Security & Other details:

- User access is currently controlled via static RLS(Row Level Security) based on region's
- Each Sales team is responsible for each regions sales
- Admin would have total access 

### Methodology

| Phase                              | Action                                                       |
| ---------------------------------- | ------------------------------------------------------------ |
| Exploratory Data analysis - Python | Performed EDA & basic python viz. to check data set & identify trends |
| Dashboard - Power BI               | Loaded dataset to Power BI, performed data modeling, transformations, DAX measures, Calculated columns, Customizing Viz, Implementing RLS |
| Export                             | Exported Dashboard in .pbix  format for review               |



