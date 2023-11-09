import streamlit as st
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import pandas as pd
from rules import get_putaran_roda_control_rules, get_daya_cengkram_rem_control_rules, kecepatan_mobil, jarak, beban, putaran_roda, daya_cengkram_rem


# Sistem kontrol fuzzy
cb_ctrl = ctrl.ControlSystem(get_putaran_roda_control_rules() + get_daya_cengkram_rem_control_rules()
)

st.title('The Fuzzy Control System for Car Braking')

st.sidebar.header('Input Parameter')
kecepatan = st.sidebar.slider('Kecepatan Mobil', 0, 120, 40)
jarak = st.sidebar.slider('Selisih Jarak', 0, 20, 3)
beban = st.sidebar.slider('Beban', 10, 1750, 750)


# Simulasi sistem fuzzy
speed = ctrl.ControlSystemSimulation(cb_ctrl)
speed.input['kecepatan_mobil'] = kecepatan
speed.input['jarak'] = jarak
speed.input['beban'] = beban

speed.compute()

putaran_roda = speed.output['putaran_roda']
daya_cengkram_rem = speed.output['daya_cengkram_rem']

st.subheader('Result', divider='red')
st.write(f""" 
**Putaran Roda**: {putaran_roda} RPM
""")
st.write(f""" 
**Daya Cengkram Rem**: {daya_cengkram_rem} LBH
""")

st.subheader('Fuzzy Graph', divider='orange')

# Pilih jenis grafik fuzzy
selected_chart = st.sidebar.selectbox('Pilih Jenis Grafik Fuzzy:', ['kecepatan_mobil', 'putaran_roda', 'daya_cengkram_rem', 'jarak', 'beban'])

if selected_chart == 'kecepatan_mobil':
    st.subheader('_Grafik Fuzzy Kecepatan Mobil_ :car:')
    universe = np.linspace(0, 120, 1000)
    membership_functions = {
        'pelan' : fuzz.trimf(universe, [0, 0, 40]),
        'cukup_pelan' : fuzz.trimf(universe, [20, 40, 60]),
        'sedang' : fuzz.trimf(universe, [40, 60, 80]),
        'cukup_cepat' : fuzz.trimf(universe, [60, 80, 100]),
        'cepat' : fuzz.trimf(universe, [80, 100, 120])
    }
elif selected_chart == 'putaran_roda':
    st.subheader('_Grafik Fuzzy Putaran Roda_ :car::dash:')
    universe = np.linspace(0, 750, 1000)
    membership_functions = {
        'minimum': fuzz.trimf(universe, [0, 0, 350]),
        'slow': fuzz.trimf(universe, [250, 350, 450]),
        'medium': fuzz.trimf(universe, [350, 450, 550]),
        'fast': fuzz.trimf(universe, [450, 550, 650]),
        'maximum': fuzz.trimf(universe, [550, 650, 750])
        # 'output' : fuzz.trimf(universe, [[putaran_roda], [putaran_roda], [putaran_roda]])
    }
    output_values = putaran_roda
elif selected_chart == 'daya_cengkram_rem':
    st.subheader('_Grafik Fuzzy Daya Cengkram Rem_ :no_entry:')
    universe = np.linspace(2000, 4495, 1000)
    membership_functions = {
        'minimum' : fuzz.trimf(universe, [0, 0, 2895]),
        'slow' : fuzz.trimf(universe, [2495, 2895, 3295]),
        'medium' : fuzz.trimf(universe, [2895, 3295, 3695]),
        'hard' : fuzz.trimf(universe, [3295, 3695, 4095]),
        'maximum' : fuzz.trimf(universe, [3695, 4095, 4495])
    }
    output_values = daya_cengkram_rem
elif selected_chart == 'jarak':
    st.subheader('_Grafik Fuzzy Jarak_ :car:')
    universe = np.linspace(0, 20, 1000)
    membership_functions = {
        'sangat_dekat' : fuzz.trimf(universe, [0, 0, 11]),
        'dekat' : fuzz.trimf(universe, [8, 11, 14]),
        'sedang' : fuzz.trimf(universe, [11, 14, 17]),
        'jauh' : fuzz.trimf(universe, [14, 17, 20]),
    }
elif selected_chart == 'beban':
    st.subheader('_Grafik Fuzzy Beban_ :car:')
    universe = np.linspace(50, 1750, 1000)
    membership_functions = {
        'ringan' : fuzz.trimf(universe, [0, 0, 750]),
        'sedang' : fuzz.trimf(universe, [500, 750, 1000]),
        'berat' : fuzz.trimf(universe, [1000, 1250, 1500]),
        'sangat_berat' : fuzz.trimf(universe, [1250, 1500, 1750]),
    }  

# Membuat grafik fuzzy triangular dengan fungsi keanggotaan yang dipilih
fig, ax = plt.subplots()
for membership_function_name, membership_function_values in membership_functions.items():
    ax.plot(universe, membership_function_values, label=membership_function_name)


# Menambahkan garis atau area untuk nilai output
if selected_chart in ['putaran_roda', 'daya_cengkram_rem']:
    half_max_y = max(membership_function_values) / 2
    ax.axvline(output_values, color='r', linestyle='dashed', linewidth=2, label='Output Value')
    # ax.fill_betweenx(y=np.linspace(0, half_max_y, 100), x1=output_values, x2=universe.max(), color='red', alpha=0.1, label='Output Area')


ax.set_xlabel('Nilai Universe')
ax.set_ylabel('Keanggotaan')
ax.set_title('Grafik Fuzzy Triangular')
ax.legend()

st.pyplot(fig)
