import streamlit as st


st.set_page_config(page_title = "Curriculum Web Alonso Riquelme", page_icon = ":ocean:")

st.header("Hola! Mi nombre es Alonso Riquelme :wave:")
st.write("Soy Ingeniero Civil Industrial con especialización en Data :computer:")

with st.container():
        st.subheader("Acerca de mi: ")
        st.markdown("- Soy una persona preocupada por el **medioambiente**, por lo mismo es que soy vegano hace 3 años :herb: :broccoli:")
        st.markdown("- Soy un entusiasta de los **videojuegos**. Farmear equipo en Ragnarok Online, o una ranked en Overwatch? Claro que yes!! :video_game:")
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Mi experiencia laboral: ")
with middle_column:
    st.markdown("**Banco Internacional**")
    st.markdown("`Agosto 2022 - Diciembre 2022` Memoria de Título, Metodología e Infraestructura, Gerencia de Riesgo Financiero")
    st.markdown("- Lorem ipsum")
    st.markdown("- Lorem ipsum")
    st.markdown("- Lorem ipsum")
with right_column:
    st.markdown("**Banco de Crédito e Inversiones**")
    st.markdown("`Enero 2022 - Junio 2022` Práctica Profesional, Gerencia de Riesgo de Mercado y Liquidez")
    st.markdown("- Lorem ipsum")
    st.markdown("- Lorem ipsum")
    st.markdown("- Lorem ipsum")