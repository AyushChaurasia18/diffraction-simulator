# Diffraction Simulator

**Numerical Simulation of Fresnel and Fraunhofer Diffraction using the
Angular Spectrum Method**

This project implements an interactive **optical diffraction simulator**
that visualizes how light propagates through different apertures.\
The simulation is built using **Python, NumPy, and Streamlit**, and
numerically solves the **Helmholtz equation** using the **Angular
Spectrum Method**.

By varying the propagation distance, the simulator naturally transitions
between **Fresnel (near-field)** and **Fraunhofer (far-field)**
diffraction regimes.

------------------------------------------------------------------------

# Overview

Diffraction occurs when a wave encounters an aperture or obstacle and
spreads as it propagates. Traditionally, diffraction is analyzed in two
regimes:

-   **Fresnel diffraction** -- near-field propagation where wavefront
    curvature is important.
-   **Fraunhofer diffraction** -- far-field propagation where the
    diffraction pattern approaches the Fourier transform of the
    aperture.

Instead of treating these separately, this simulator uses the **Angular
Spectrum Method**, which provides an **exact numerical solution for
free-space propagation**.

Changing the propagation distance (z) allows smooth transition between
the two regimes.

------------------------------------------------------------------------

# Mathematical Background

A monochromatic scalar field satisfies the **Helmholtz equation**

\[`\nabla`{=tex}\^2 U + k\^2 U = 0\]

Any field at (z = 0) can be decomposed into plane waves:

\[\
U(x,y,0) = `\iint `{=tex}`\tilde{U}`{=tex}(k_x,k_y)e\^{i(k_x x + k_y
y)}dk_x dk_y \]

Each plane wave propagates with phase

\[\
e\^{ik_z z} \]

where

\[\
k_z = `\sqrt{k^2 - k_x^2 - k_y^2}`{=tex} \]

The propagated field becomes

\[\
U(x,y,z)=
`\mathcal{F}`{=tex}\^{-1}`\left[\tilde{U}(k_x,k_y)e^{ik_z z}\right]`{=tex}\]

This formulation is implemented numerically using **Fast Fourier
Transforms (FFT)**.

------------------------------------------------------------------------

# Numerical Algorithm

The simulation follows these steps:

1.  Define the aperture function (U_0(x,y))
2.  Compute the Fourier transform using `fft2`
3.  Construct the spatial frequency grid
4.  Compute the propagation kernel

\[\
H = e\^{iz`\sqrt{k^2 - k_x^2 - k_y^2}`{=tex}} \]

5.  Multiply the spectrum by the kernel
6.  Perform inverse FFT using `ifft2`
7.  Compute intensity

\[\
I = \|U_z\|\^2 \]

------------------------------------------------------------------------

# Features

The simulator supports multiple aperture geometries:

-   Single slit
-   Double slit
-   Triple slit
-   Circular aperture
-   Annular (ring) aperture
-   Rectangular aperture
-   Gaussian aperture

Adjustable simulation parameters:

-   Wavelength
-   Propagation distance
-   Aperture dimensions
-   Grid resolution
-   Simulation window size

These controls allow real‑time exploration of diffraction behavior.

------------------------------------------------------------------------

# Fresnel vs Fraunhofer Regimes

The diffraction regime depends on propagation distance.

### Fresnel diffraction (near-field)

\[ z `\sim `{=tex}`\frac{a^2}{\lambda}`{=tex} \]

Wavefront curvature across the aperture is significant.

### Fraunhofer diffraction (far-field)

\[ z `\gg `{=tex}`\frac{a^2}{\lambda}`{=tex} \]

The diffraction pattern approaches the **Fourier transform of the
aperture**.

------------------------------------------------------------------------

# Installation

Clone the repository:

``` bash
git clone https://github.com/yourusername/diffraction-simulator.git
cd diffraction-simulator
```

Install dependencies:

``` bash
pip install numpy matplotlib streamlit
```

------------------------------------------------------------------------

# Running the Simulator

Launch the Streamlit application:

``` bash
streamlit run app.py
```

The simulator will open automatically in your browser.

------------------------------------------------------------------------

# Example Applications

This simulator can demonstrate:

-   Young's double slit experiment
-   Diffraction through circular apertures
-   Airy disk formation
-   Multi‑slit interference
-   Transition between Fresnel and Fraunhofer regimes

------------------------------------------------------------------------

# Technologies Used

-   Python
-   NumPy
-   Matplotlib
-   Streamlit

------------------------------------------------------------------------

# Author

**Ayush Chaurasia**\

------------------------------------------------------------------------

# Possible Future Improvements

-   Phase visualization
-   Log‑scale intensity display
-   Diffraction gratings
-   Propagation animation
-   GPU acceleration

------------------------------------------------------------------------
