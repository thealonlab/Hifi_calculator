import streamlit as st

# Function to calculate insert concentration
def calc_insert_concentration(vector_concentration, vector_length, insert_length, molar_ratio):
    """
    Calculate the required insert concentration based on 
    the provided vector concentration and lengths.
    """
    if vector_concentration <= 0 or vector_length <= 0 or insert_length <= 0 or molar_ratio <= 0:
        return None, "All input values must be positive numbers greater than zero."
    
    ratio = insert_length / vector_length
    insert_concentration = round(ratio * molar_ratio * vector_concentration)
    return insert_concentration, None

# Function to calculate dilution of insert
def calc_dilution(desired_concentration, current_concentration, volume):
    """
    Calculate the dilution factor based on the desired and current concentrations.
    Assumes the desired volume is per the user input."
    """
    if desired_concentration <= 0 or current_concentration <= 0:
        return None, "Concentration values must be positive numbers."
    
    dilution_factor = desired_concentration / current_concentration
    final_volume = volume / dilution_factor
    return round(final_volume, 1), None

# Streamlit App
def main():
    st.title("NEB HiFi Assembly Calculator")
    st.write("This tool helps you calculate the required insert amount and dilution for NEB HiFi Assembly.")

    # Input fields for the assembly calculation
    st.header("Insert Calculation")
    vector_concentration = st.number_input("Enter vector concentration (ng/µl):", min_value=1, max_value=500, value=50)
    vector_length = st.number_input("Enter vector length (bp):", min_value=1, value=5000, step=1)
    insert_length = st.number_input("Enter insert length (bp):", min_value=1, value=500, step=1)
    molar_ratio = st.number_input("Enter molar ratio:", min_value=1, value=2, step=1)

    if 'insert_amount' not in st.session_state:
        st.session_state.insert_amount = 0.1
    insert_amount = st.session_state.insert_amount
    if st.button("Calculate Insert Amount"):
        st.session_state.insert_message = ""
        result = calc_insert_concentration(vector_concentration, vector_length, insert_length, molar_ratio)
        if result:
            insert_amount, error = result
        else:
            insert_amount, error = None, None
        st.session_state.insert_amount = insert_amount
        insert_amount, error = calc_insert_concentration(vector_concentration, vector_length, insert_length, molar_ratio)
        
        if error:
            st.error(error)
        else:
            st.session_state.insert_message = f"### Amount of insert needed: {insert_amount} ng"

    if 'insert_message' in st.session_state and st.session_state.insert_message:
        st.success(st.session_state.insert_message)

    # Input fields for dilution calculation
    st.header("Dilution Calculation")
    insert_amount = st.number_input("Insert Amount (ng):", min_value=0.1, value=float(insert_amount), step=0.1)
    desired_insert_volume = st.number_input("Desired Insert Volume (µl):", min_value=0.1, value=1.0, step=0.1)
    current_concentration = st.number_input("Enter current concentration (ng/µl):", min_value=0.1, value=100.0, step=0.1)

    if st.button("Calculate Dilution"):
        dilution_volume, error = calc_dilution(insert_amount, current_concentration, desired_insert_volume)
        
        if error:
            st.error(error)
        else:
            st.success(f"""### To achieve {insert_amount} ng in {desired_insert_volume} µl, mix:
- **1 µl** of the current **{current_concentration} ng/µl** insert solution  
- **{round(dilution_volume-1, 2)} µl** of water""")


if __name__ == "__main__":
    main()
