import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="MathScanner - Resolvente", layout="centered")

st.title("📊 MathScanner: Calculadora de la Resolvente")
st.write("Herramienta interactiva para resolver ecuaciones de segundo grado.")

# Entradas de datos
col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("Valor de a", value=1.0)
with col2:
    b = st.number_input("Valor de b", value=0.0)
with col3:
    c = st.number_input("Valor de c", value=0.0)

if st.button("📝 RESOLVER"):
    if a == 0:
        st.error("El valor de 'a' no puede ser 0 en una ecuación cuadrática.")
    else:
        # Cálculo del Discriminante
        discriminante = b**2 - 4*a*c
        st.info(f"Discriminante (Δ) = {discriminante}")
        
        # Resolver
        if discriminante > 0:
            x1 = (-b + np.sqrt(discriminante)) / (2*a)
            x2 = (-b - np.sqrt(discriminante)) / (2*a)
            st.success(f"Dos raíces reales: x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif discriminante == 0:
            x = -b / (2*a)
            st.warning(f"Raíz doble: x = {x:.2f}")
        else:
            st.error("Las raíces son complejas (no tocan el eje X).")

        # Gráfica de la Parábola
        st.subheader("📈 Gráfica de la Función")
        x_vals = np.linspace(-10, 10, 400)
        y_vals = a*x_vals**2 + b*x_vals + c
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"{a}x² + {b}x + {c}")
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        st.pyplot(fig)

st.divider()
st.caption("Proyecto para la Feria de Ciencias - Creado por Carlos")
      
