import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
image = Image.open('cover.png')
st.image(image,use_column_width=True)
st.sidebar.write("""# Solar DC Pump Designing
 ***By: Prateek Malhotra*** """)
link = '[Linkedin](https://www.linkedin.com/in/prateek-malhotra/)'
link1 = '[Github](https://github.com/pm1306)'
link2 = '[Blogger - Sun In City](https://sunincity.blogspot.com/)'
st.sidebar.markdown(link, unsafe_allow_html=True)
st.sidebar.markdown(link1, unsafe_allow_html=True)
st.sidebar.markdown(link2, unsafe_allow_html=True)




water = st.number_input('Water drawn/day (in liters)')
vertical_lift = st.number_input('Total vertical lift (in m)')
peak_sun_hours = st.number_input('Peak sunshine hours')


status = st.radio('Select your design: ',
                ('DC Pump with MPPT', 'DC Pump without MPPT'))



if (status == 'DC Pump without MPPT'):
    try:
        # DC Pump without MPPT
        drawdown = 2
        volume = water/1000
        water_density = 1000
        g = 9.8
        operating_factor = 0.75
        pump_efficiency = .3
        mismatch_factor = 0.85
        frictional_loss = (vertical_lift + drawdown) * 0.05
        TDH = vertical_lift + drawdown + frictional_loss
        hydraulic_energy = (water_density * volume * g * TDH) / 3600
        total_pv_wattage = hydraulic_energy / (peak_sun_hours * pump_efficiency * mismatch_factor * operating_factor)
        motor_rating = total_pv_wattage / 746

    except:
        st.write('Awaiting response')

    if(st.button('Calculate')):
    
        # print results
        st.write('''***Total Dynamic Head (THD): ***''',TDH, '''***m***''')
        st.write('''***PV Wattage required: ***''',total_pv_wattage, '''***watts***''')
        st.write('''***Rating of pump: ***''',motor_rating, '''***hp***''')
        
        image1 = Image.open('without MPPT.png')
        font_type = ImageFont.truetype('arial.ttf',50)
        draw = ImageDraw.Draw(image1)

        pv=str(format(total_pv_wattage, '.2f'))
        pv=pv+' Watt'
        draw.text(xy=(250,20),text=pv, fill=(255,69,0),font=font_type)

        elev = str(format(vertical_lift, '.2f'))
        elev = elev+' m'
        draw.text(xy=(950,420),text=elev, fill=(30,144,255),font=font_type)

        pump_rat = str(format(motor_rating, '.2f'))
        pump_rat = pump_rat+' hp'
        draw.text(xy=(600,820),text=pump_rat, fill=(30,144,255),font=font_type)

        vol = str(format(volume, '.2f'))
        vol = vol+' cm\u00b3'
        draw.text(xy=(1280,320),text=vol, fill=(0,0,0),font=font_type)

        st.image(image1,use_column_width=True)
    
        


if (status == 'DC Pump with MPPT'):
    try:
        # DC Pump with MPPT
        drawdown = 2
        volume = water/1000
        water_density = 1000
        g = 9.8
        operating_factor = 0.75
        pump_efficiency = .3
        mismatch_factor = 1
        MPPT_efficiency = .95
        frictional_loss = (vertical_lift + drawdown) * 0.05
        TDH = vertical_lift + drawdown + frictional_loss
        hydraulic_energy = (water_density * volume * g * TDH) / 3600
        total_pv_wattage = hydraulic_energy / (peak_sun_hours * pump_efficiency * mismatch_factor * operating_factor * MPPT_efficiency)
        motor_rating = total_pv_wattage / 746
    except:
        st.write('Awaiting response')
    
    if(st.button('Calculate')):
    
        # print results
        st.write('''***Total Dynamic Head (THD): ***''',TDH, '''***m***''')
        st.write('''***PV Wattage required: ***''',total_pv_wattage, '''***watts***''')
        st.write('''***Rating of pump: ***''',motor_rating, '''***hp***''')

        image1 = Image.open('with MPPT.png')
        font_type = ImageFont.truetype('arial.ttf',50)
        draw = ImageDraw.Draw(image1)

        pv=str(format(total_pv_wattage, '.2f'))
        pv=pv+' Watt'
        draw.text(xy=(250,20),text=pv, fill=(255,69,0),font=font_type)

        elev = str(format(vertical_lift, '.2f'))
        elev = elev+' m'
        draw.text(xy=(950,420),text=elev, fill=(30,144,255),font=font_type)

        pump_rat = str(format(motor_rating, '.2f'))
        pump_rat = pump_rat+' hp'
        draw.text(xy=(600,820),text=pump_rat, fill=(30,144,255),font=font_type)

        vol = str(format(volume, '.2f'))
        vol = vol+' cm\u00b3'
        draw.text(xy=(1280,320),text=vol, fill=(0,0,0),font=font_type)

        st.image(image1,use_column_width=True)










