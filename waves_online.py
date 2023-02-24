import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statistics as stat
import streamlit as st

st.set_page_config(page_title="Wave analysis")
st.title("Wave analysis")
st.subheader("Feed me your XLSX file")
st.markdown(
"Please make sure input data is structured as follows:  \n"
"Row 1(wave height): 1, 2, 3, 6, 3, 5  \n"
"Row 2(wave period): 3, 2, 9, 16, 2, 5"
)

uploaded = st.file_uploader("Choose an xlsx file", type="xlsx")
if uploaded:
    df = pd.read_excel(uploaded, header=None)
    df =df[0].str.split(', ', expand=True)
    df = df.transpose().astype(float)
    df.columns = ["Golfhoogte", "Golfperiode"]
    g_hoogte_list = df["Golfhoogte"].tolist()
    g_periode_list = df["Golfperiode"].tolist()

    height_average = stat.fmean(g_hoogte_list)                      #get the average height from the hoogte list
    period_average = stat.fmean(g_periode_list)                     #get the average period from the periode list

    Hs_list = [i for i in g_hoogte_list if i > np.percentile(g_hoogte_list, 66.666667)]
    Hs = stat.fmean(Hs_list)                                        #get the average height from the Hs_list, this is the significant wave height

    index = [i for i, j in enumerate(g_hoogte_list) if j in Hs_list]          #get the location of the significant waves in the orignial wave list.
    g_period_Hs = [g_periode_list[i] for i in index]    
    Tp = stat.fmean(g_period_Hs)                                    #Find the average wave period for the significant waves


    max_height = max(g_hoogte_list)                                 #get the highest wave and its corresponding peroid
    max_corresponding_period = g_periode_list[g_hoogte_list.index(max_height)]

    min_height = min(g_hoogte_list)                                 #get the lowest wave and its corresponding peroid
    min_corresponding_period = g_periode_list[g_hoogte_list.index(min_height)]

    longest_period = max(max_corresponding_period, min_corresponding_period)        #find the longest period between the lowest and highest wave


    x = np.arange(0,longest_period,0.1)                                             #store the values of 0.1 steps between 0 and the longest_period
    y = 0.5*max_height*np.sin((2*np.pi/max_corresponding_period)*x)                 #plot the highest wave
    z = 0.5*min_height*np.sin((2*np.pi/min_corresponding_period)*x)                 #plot the lowest wave
    w = y + z                                                                       #plot the sum

    steps = np.arange(0, longest_period, step=np.pi / 2)
    label = [str(j) + 'π' for j in np.arange(0, steps.size * 0.5, 0.5)]

    fig = plt.figure()
    plt.xlabel('time (s)')  # label on the x plane
    plt.ylabel('height (m)') #label on the y plane
    plt.title('Plot of wave height from 0 to %i seconds' %longest_period)   #title of the graph
    plt.grid(True, which='both')                                            #show the grid
    plt.plot(x,y,x,z,x,w)                                                   #plot everything for real
    plt.gca().legend(('Highest wave', 'lowest wave', 'combined waves'))      #titles of each graph
    plt.xticks(steps, label)                                                #show those value of pi
    plt.savefig("myplot.png", dpi = 'figure')
    plt.show()

    st.pyplot(fig)
    st.markdown(f"significante golfhoogte: {Hs:.2f} m")
    st.markdown(f"significante golfperiode: {Tp:.2f} sec")
    st.markdown(f"hoogste golf: {max_height:.2f} m")
    st.markdown(f"bijbehorende periode: {max_corresponding_period:.2f} s")
    st.markdown(f"laagste golf: {min_height:.2f} m")
    st.markdown(f"bijbehorende periode: {min_corresponding_period:.2f} s")





