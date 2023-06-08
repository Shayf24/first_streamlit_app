import streamlit
streamlit.title('My Parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 🥗  🥑🍞 Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)



# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_to_show = my_fruit_list.loc[fruits_selected]



#new tasks
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
