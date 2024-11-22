import streamlit as st
st.title("2205A21042 - PS6")
st.subheader("calculate the efficiency and copper losses at various loads")
def output(VA,CL,FCL,K,PF):
    CUL = (K**2)*FCL
    Eff= (K*VA*PF)/(K*VA*PF)+(CL+CUL)
    return Eff,CUL

col1,col2=st.columns(2)
with col1:
    VA=st.number_input("Rating innvolt-ams", value=100)
    CL=st.number_input("Core osses-watts", value=100)
    FCL=st.number_input("Ful load cupper losses watts", value=100)
    K=st.number_input("Loading", value=0.50)
    PF=st.number_input("Powerfactor:PF", value=0.50)
    compute=st.button("compute")

with col2:
    with st.container(border=True):
        if compute:
            Eff,CUL=output(VA,CL,FCL,K,PF)
            st.write(f"Efficiency={Eff:.2f}")
            st.write(f"CUL={ CUL:.2f} Watts")