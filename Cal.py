# weight_converter_app.py
import streamlit as st

def pounds_to_kilograms(pounds):
    return pounds * 0.45359237

def kilograms_to_pounds(kilograms):
    return kilograms / 0.45359237

def main():
    st.title("Weight Converter")

    weight = st.number_input("Enter weight:")
    unit = st.selectbox("Select unit:", ["Pounds", "Kilograms"])

    converted_weight = None

    if unit == "Pounds":
        converted_weight = pounds_to_kilograms(weight)
        st.write(f"{weight} pounds is equivalent to {converted_weight} kilograms.")
    elif unit == "Kilograms":
        converted_weight = kilograms_to_pounds(weight)
        st.write(f"{weight} kilograms is equivalent to {converted_weight} pounds.")

if __name__ == "__main__":
    main()
