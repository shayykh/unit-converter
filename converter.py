import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    
    .stApp {
        background-color: linear-gradient(140deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    
    h1 {
        color: white;
        text-align: center;
        font-size: 30px;
    }
    
    h5 {
        color: white;
        text-align: center;
        font-size: 10px;
    }
    
    .stButton button {
        background-color: linear-gradient(45deg, #bcbcbc, #cfe2f3);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: white;
    }
    
    </style>
    """, unsafe_allow_html=True
    )

#title and description
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("<h5>Convert various units seamlessly using this simple application.</h5>", unsafe_allow_html=True)

st.write("")
#sidebar menu
conversion_option = st.sidebar.selectbox("Select the conversion option", ["Length", "Weight", "Temperature", "Area", "Volume"])

st.write("")

value = st.number_input("Enter the value", min_value=0.0, value=1.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_option == "Length":
    with col1:
        from_unit = st.selectbox("From", ["m", "cm", "mm", "km", "ft", "in", "mi","yard"])
    with col2:
        to_unit = st.selectbox("To", ["m", "cm", "mm", "km", "ft", "in", "mi","yard"])

elif conversion_option == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["kg", "g", "mg", "lb", "oz"])
    with col2:
        to_unit = st.selectbox("To", ["kg", "g", "mg", "lb", "oz"])

elif conversion_option == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["C", "F", "K"])
    with col2:
        to_unit = st.selectbox("To", ["C", "F", "K"])

elif conversion_option == "Area":
    with col1:
        from_unit = st.selectbox("From", ["m^2", "cm^2", "mm^2", "km^2", "ft^2", "in^2", "mi^2", "yard^2"])
    with col2:
        to_unit = st.selectbox("To", ["m^2", "cm^2", "mm^2", "km^2", "ft^2", "in^2", "mi^2", "yard^2"])

elif conversion_option == "Volume":
    with col1:
        from_unit = st.selectbox("From", ["m^3", "cm^3", "mm^3", "km^3", "ft^3", "in^3", "mi^3", "yard^3"])
    with col2:
        to_unit = st.selectbox("To", ["m^3", "cm^3", "mm^3", "km^3", "ft^3", "in^3", "mi^3", "yard^3"])

#conversion logic
def convert_length(value, from_unit, to_unit):
    length_factors = {
        "m": 1.0,
        "cm": 100.0,
        "mm": 1000.0,
        "km": 0.001,
        "ft": 3.28084,
        "in": 39.3701,
        "mi": 0.000621371,
        "yard": 1.09361,
    }
    return value * (length_factors[to_unit] / length_factors[from_unit])

def convert_weight(value, from_unit, to_unit):
    weight_factors = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 2.20462,
        "oz": 35.274,
    }
    return value * weight_factors[from_unit] / weight_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "F" and to_unit == "K":
        return (value + 459.67) * 5/9
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "K" and to_unit == "F":
        return (value - 273.15) * 9/5 + 32

def convert_area(value, from_unit, to_unit):
    area_factors = {
        "m^2": 1.0,
        "cm^2": 10000.0,
        "mm^2": 1000000.0,
        "km^2": 0.000001,
        "ft^2": 10.7639,
        "in^2": 1550.0031,
        "mi^2": 0.000000386102,
        "yard^2": 1.19599,
    }
    return value * area_factors[from_unit] / area_factors[to_unit]

def convert_volume(value, from_unit, to_unit):
    volume_factors = {
        "m^3": 1.0,
        "cm^3": 0.000001,
        "mm^3": 0.000000001,
        "km^3": 0.000000000001,
        "ft^3": 0.0353147,
        "in^3": 61023.7,
        "mi^3": 0.0000000000002599999,
        "yard^3": 1.30795,
    }   
    return value * volume_factors[from_unit] / volume_factors[to_unit]

#button to perform conversion
if st.button("Convert"):
    if conversion_option == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_option == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_option == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_option == "Area":
        result = convert_area(value, from_unit, to_unit)
    elif conversion_option == "Volume":
        result = convert_volume(value, from_unit, to_unit)
        
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)

st.write("")
#footer
st.markdown("<div class='footer'>Developed by <a href='https://github.com/shayykh'>@shayykh</a></div>", unsafe_allow_html=True)
