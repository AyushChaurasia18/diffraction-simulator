import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("Diffraction Simulator")


st.sidebar.header("Simulation Parameters")

wavelength = st.sidebar.slider(
    "Wavelength (nm)", 400, 800, 633
) * 1e-9

z = st.sidebar.slider(
    "Propagation Distance z (cm)", 1.0, 50.0, 5.0
) / 100

N = st.sidebar.selectbox("Grid Size (Resolution)", [512, 1024, 2048], index=1)

L = st.sidebar.slider(
    "Physical Grid Size (mm)", 2.0, 10.0, 5.0
) * 1e-3

aperture_type = st.sidebar.selectbox(
    "Aperture Type",
    [
        "Single Slit",
        "Double Slit",
        "Triple Slit",
        "Circular",
        "Annular (Ring)",
        "Rectangular",
        "Gaussian"
        
    ]
)


k = 2*np.pi / wavelength
dx = L / N

x = np.linspace(-L/2, L/2, N)
y = np.linspace(-L/2, L/2, N)
X, Y = np.meshgrid(x, y)


aperture = np.zeros_like(X)

if aperture_type == "Single Slit":
    slit_width = st.sidebar.slider("Slit Width (mm)", 0.05, 1.0, 0.2) * 1e-3
    aperture = np.abs(X) < slit_width/2

elif aperture_type == "Double Slit":
    slit_width = st.sidebar.slider("Slit Width (mm)", 0.05, 1.0, 0.2) * 1e-3
    d = st.sidebar.slider("Slit Separation (mm)", 0.1, 2.0, 0.5) * 1e-3
    aperture = (np.abs(X - d/2) < slit_width/2) | (np.abs(X + d/2) < slit_width/2)

elif aperture_type == "Triple Slit":
    slit_width = st.sidebar.slider("Slit Width (mm)", 0.05, 1.0, 0.2) * 1e-3
    d = st.sidebar.slider("Slit Separation (mm)", 0.1, 2.0, 0.5) * 1e-3
    aperture = (
        (np.abs(X - d) < slit_width/2) |
        (np.abs(X) < slit_width/2) |
        (np.abs(X + d) < slit_width/2)
    )

elif aperture_type == "Circular":
    radius = st.sidebar.slider("Radius (mm)", 0.1, 2.0, 0.5) * 1e-3
    aperture = X**2 + Y**2 < radius**2

elif aperture_type == "Annular (Ring)":
    r_inner = st.sidebar.slider("Inner Radius (mm)", 0.1, 1.0, 0.3) * 1e-3
    r_outer = st.sidebar.slider("Outer Radius (mm)", 0.2, 2.0, 0.6) * 1e-3
    aperture = (X**2 + Y**2 < r_outer**2) & (X**2 + Y**2 > r_inner**2)

elif aperture_type == "Rectangular":
    width = st.sidebar.slider("Width (mm)", 0.1, 2.0, 0.5) * 1e-3
    height = st.sidebar.slider("Height (mm)", 0.1, 2.0, 0.5) * 1e-3
    aperture = (np.abs(X) < width/2) & (np.abs(Y) < height/2)

elif aperture_type == "Gaussian":
    sigma = st.sidebar.slider("Sigma (mm)", 0.1, 2.0, 0.5) * 1e-3
    aperture = np.exp(-(X**2 + Y**2)/(2*sigma**2))


U0 = aperture.astype(float)



fx = np.fft.fftfreq(N, dx)
fy = np.fft.fftfreq(N, dx)
FX, FY = np.meshgrid(fx, fy)

kx = 2*np.pi*FX
ky = 2*np.pi*FY


H = np.exp(1j * z * np.sqrt(np.maximum(0, k**2 - kx**2 - ky**2)))

U0_fft = np.fft.fft2(U0)
Uz_fft = U0_fft * H
Uz = np.fft.ifft2(Uz_fft)

I = np.abs(Uz)**2
I /= I.max()


col1, col2 = st.columns(2)

with col1:
    st.subheader("Aperture")
    fig1, ax1 = plt.subplots()
    ax1.imshow(U0, extent=[-L/2, L/2, -L/2, L/2])
    ax1.set_xlabel("x (m)")
    ax1.set_ylabel("y (m)")
    st.pyplot(fig1)

with col2:
    st.subheader(f"Intensity at z = {z:.3f} m")
    fig2, ax2 = plt.subplots()
    ax2.imshow(I, extent=[-L/2, L/2, -L/2, L/2])
    ax2.set_xlabel("x (m)")
    ax2.set_ylabel("y (m)")
    st.pyplot(fig2)

