!pip install "git+https://github.com/MicroPyramid/forex-python.git"
import streamlit as st
from forex_python.converter import CurrencyRates
from datetime import date
c = CurrencyRates()
today = date.today()
header = st.container()

with header:
  st.title("Currency conventer")
  st.subheader(today)
  amount = st.number_input('Insert amount')
  currency1 = st.selectbox(
      'From:',
      (' ','USD','EUR','GBP','INR','SEK','PLN','TRY','DKK','CNY','CAD','CHF','BGN','HRK','CZK','ISK','HUF','NOK','MXN'))
  currency2 = st.selectbox(
      'To:',
      (' ','USD','EUR','GBP','INR','SEK','PLN','TRY','DKK','CNY','CAD','CHF','BGN','HRK','CZK','ISK','HUF','NOK','MXN'))
  


  if (currency1 ==' ') and (currency2 ==' '):
    st.text('Enter amount and select currencies')
  elif  (currency1 !=' ') and (currency2 ==' '):
    st.text('Select second currency ')
  elif  (currency1 ==' ') and (currency2 !=' '):
    st.text('Select first currency ') 
  else:
    rate = c.get_rate(currency1, currency2)
    st.text('Enter amount and select both currencies')
    result = amount * rate
    result = round(result,ndigits=2)
    st.text(f'{amount} {currency1} = {result} {currency2}')

