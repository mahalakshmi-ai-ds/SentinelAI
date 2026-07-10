import streamlit as st


def show_mitre(mitre):

    st.header("🛡️ MITRE ATLAS Mapping")

    if len(mitre) == 0:

        st.success("No MITRE AI attack techniques detected.")

        return

    for attack in mitre:

        with st.container():

            st.subheader(f"{attack['id']} — {attack['name']}")

            st.write(attack["description"])

            st.divider()