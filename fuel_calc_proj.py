
import streamlit as st

st.header('FUEL PRICE CALCULATOR') #Creating a header for the app
fuels = {'Petrol':165, 'Diesel':670, 'Kerosene':680} #making a dictionary for the items I want to be selected
prices = ['Litres', 'Amount'] #creating a list
st.sidebar.header('MENU') #creating a header for the sidebar
fuel = st.sidebar.radio('SELECT ONE OF THE OPTIONS BELOW', fuels) #creating a radio button
price = st.sidebar.radio('SELECT ONE OF THE OPTIONS BELOW', prices) #creating another radio button
#st.sidebar.button('ENTER') #here I tried to make a button that when clicked would bring out the code below but it did not work
if fuel == 'Petrol' and price == 'Litres': #Using a boolean to make two options produce a code
    x = st.number_input('HOW MANY LITRES OF PETROL DO YOU WANT TO BUY?')
    if st.button('CALCULATE'):
        z = x * fuels['Petrol'] #value provided multiplied by the value assigned to the key in the dictionary.
        st.write (f'{x} Litres of Petrol is {z} Naira only')
elif fuel == 'Petrol' and price == 'Amount':
    x = st.number_input('HOW MANY LITRES OF PETROL CAN YOU BUY?')
    if st.button('CALCULATE'):
        z = x / fuels['Petrol'] #value provided multiplied by the value assigned to the key in the dictionary.
        z = round(z, 2) #rounding up the numbers to two decimal points only
        st.write (f'{x} Naira will give you {z} Litres of Petrol only')
elif fuel == 'Diesel' and price == 'Litres':
    x = st.number_input('HOW MANY LITRES OF DIESEL DO YOU WANT TO BUY?')
    if st.button('CALCULATE'):
        z = x * fuels['Diesel'] #value provided multiplied by the value assigned to the key in the dictionary.
        st.write (f'{x} Litres of Diesel is {z} Naira only')
elif fuel == 'Diesel' and price == 'Amount':
    x = st.number_input('HOW MANY LITRES OF DIESEL CAN YOU BUY?')
    if st.button('CALCULATE'):
        z = x / fuels['Diesel'] #value provided multiplied by the value assigned to the key in the dictionary.
        z = round(z, 2) #rounding up the numbers to two decimal points only
        st.write (f'{x} Naira will give you {z} Litres of Diesel only')
elif fuel == 'Kerosene' and price == 'Litres':
    x = st.number_input('HOW MANY LITRES OF KEROSENE DO YOU WANT TO BUY?')
    if st.button('CALCULATE'):
        z = x * fuels['Kerosene'] #value provided multiplied by the value assigned to the key in the dictionary.
        st.write (f'{x} Litres of Kerosene is {z} Naira only')
elif fuel == 'Kerosene' and price == 'Amount':
    x = st.number_input('HOW MANY LITRES OF KEROSENE CAN YOU BUY?')
    if st.button('CALCULATE'):
        z = x / fuels['Kerosene'] #value provided multiplied by the value assigned to the key in the dictionary.
        z = round(z, 2) #rounding up the numbers to two decimal points only
        st.write (f'{x} Naira will give you {z} Litres of Kerosene only')
