import streamlit
import pandas

import requests
import snowflake.connector
from urllib.error import URLError




streamlit.title('My Parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 🥗  🥑🍞 Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)




# Display the table on the page.
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), key = 'Lime')
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show )

#new request


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
#streamlit.text(fruityvice_response)
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)




my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains: ")
streamlit.dataframe(my_data_rows)

streamlit.header("Choose a fruit to add")
fruit_add= streamlit.text_input('What fruit would you like to add?','cherry')
streamlit.button('Add a Fruit to the List:')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
back_from_function = insert_row_snowflake(fruit_add)
my_cnx.close()
 
