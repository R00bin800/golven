import random
import pandas as pd
import streamlit as st
from io import BytesIO

st.set_page_config(page_title="Random wave generator")
st.title("Random wave generator")
st.subheader("Generate some random waves and download it!")
st.markdown(
"This generator is compatible with my wave analysis site.  \n"
"Due to some weird error I'm not willing to fix, please keep amount of waves below 8500"
)
st.sidebar.markdown("# Wave generator")

waves = []
period = []

amount = st.number_input("The amount of waves to generate",min_value=0,max_value=8500) #ammount of waves to generate

min_height = st.number_input("minimum wave height",min_value=1,max_value=79) 
max_height = st.number_input("maxiumum wave height",min_value=min_height, max_value=80)

min_period = st.number_input("minimum wave period",min_value=1,max_value=119)
max_period = st.number_input("maxiumum wave period",min_value=min_period, max_value=120)

if min_height and max_height and min_period and max_period:
    for i in range(amount):
        waves.append(random.randint(min_height,max_height))
        period.append(random.randint(min_period,max_period))

    df = pd.DataFrame(list(zip(waves,period)),columns = ["golfhoogte", "golfperiode"]).transpose()
    df = df[df.columns[0:]].apply(lambda x: ', '.join(x.dropna().astype(str)),axis=1)
    def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, header=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        format1 = workbook.add_format({'num_format': '0'}) 
        worksheet.set_column('A:A', None, format1)  
        writer.save()
        processed_data = output.getvalue()
        return processed_data
    #excel_data = df.to_excel("test", index=False, header=False)
    st.download_button("📥 Download the generated data", data=to_excel(df),file_name="wavetestdata.xlsx")
