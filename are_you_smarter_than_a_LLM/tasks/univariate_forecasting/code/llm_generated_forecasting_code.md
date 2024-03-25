Sure, I will use the ARIMA model (AutoRegressive Integrated Moving Average) to fit this data. ARIMA is a popular time series forecasting model. 

First, we need to import the necessary libraries and load the data:

```python
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt

# Load the data
data = {'YearMonth': ['2025-1', '2025-2', '2025-3', '2025-4', '2025-5', '2025-6', '2025-7', '2025-8', '2025-9', '2025-10', '2025-11', '2025-12', '2026-1', '2026-2', '2026-3', '2026-4', '2026-5', '2026-6', '2026-7', '2026-8', '2026-9', '2026-10', '2026-11', '2026-12', '2027-1', '2027-2', '2027-3', '2027-4', '2027-5', '2027-6', '2027-7', '2027-8', '2027-9'],
        'Sales (m)': [72.45048, 73.99130, 76.11605, 80.27044, 73.10539, 66.66382, 65.98844, 69.48180, 78.51508, 65.89159, 79.67798, 79.84679, 72.09140, 83.17577, 79.14327, 85.82591, 70.41418, 68.81332, 63.79152, 75.34061, 84.93346, 72.78681, 79.18504, 86.33679, 82.31799, 85.83403, 84.32723, 88.56505, 72.16734, 76.71821, 65.23420, 77.73125, 85.45101]}
df = pd.DataFrame(data)
df['YearMonth'] = pd.to_datetime(df['YearMonth'])
df.set_index('YearMonth', inplace=True)
```

Next, we fit the ARIMA model to the data:

```python
# Fit the ARIMA model
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit(disp=0)
```

Finally, we use the model to forecast the sales for the last 3 months of 2027:

```python
# Forecast
forecast, stderr, conf_int = model_fit.forecast(steps=3)

# Print the forecast
for i in range(len(forecast)):
    print('Predicted Sales for 2027-%d: %.2f' % (i+10, forecast[i]))
```

Please note that the order of the ARIMA model (5,1,0) was chosen arbitrarily. In practice, you would use model selection techniques to choose the best order. Also, the ARIMA model assumes that the time series is stationary. If the time series is not stationary, you would need to transform it to make it stationary before fitting the model.
