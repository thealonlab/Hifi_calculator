import streamlit as st

# Define the pick and probability functions

def calc(vector,vector_bp,insert_bp,molar_ratio):
    ratio = insert_bp / vector_bp
    return round(ratio * molar_ratio * vector)

# Streamlit App
def main():
    st.title("NEB HiFi Assembly calculator")
#    st.write("Enter vectoSimulate and visualize the diversity of your nanobody library")

    # Streamlit input widgets
    vector = st.number_input("Enter vector concentration (ng/µl):", min_value=1, value=50, step=1)
    vector_bp = st.number_input("Enter vector length (bp):", min_value=1, value=5000, step=1)
    insert_bp = st.number_input("Enter insert length (bp):", min_value=1, value=500, step=1)
    molar_ratio = st.number_input("Enter molar ratio:", min_value=1, value=2, step=1)

    if st.button("Calculate"):
        # Calculate insert concentration
        insert_ng = calc(vector,vector_bp,insert_bp,molar_ratio)

        st.write(f"### Amount of insert needed: {insert_ng} ng")

if __name__ == "__main__":
    main()
