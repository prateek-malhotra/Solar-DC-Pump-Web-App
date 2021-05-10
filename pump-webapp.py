import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from PIL import Image
image = Image.open('cover.png')
st.image(image,use_column_width=True)
st.sidebar.write("""# Solar DC Pump Designing
 ***By: Prateek Malhotra*** """)
link = '[Linkedin](https://www.linkedin.com/in/prateek-malhotra/)'
st.sidebar.markdown(link, unsafe_allow_html=True)



# water = 25000
# vertical_lift = 10
# peak_sun_hours = 6
water = st.number_input('Water drawn/day (in liters)')
vertical_lift = st.number_input('Total vertical lift (in m)')
peak_sun_hours = st.number_input('Peak sunshine hours')


status = st.radio('Select your design: ',
                ('DC Pump without MPPT', 'DC Pump with MPPT'))



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

# if(st.button('Calculate')):
    
#     # print results
#     st.write('''***Total Dynamic Head (THD) is: ***''',TDH, '''***m***''')
#     st.write('''***PV Wattage required is: ***''',total_pv_wattage, '''***watts***''')
#     st.write('''***Rating of pump is: ***''',motor_rating, '''***hp***''')








