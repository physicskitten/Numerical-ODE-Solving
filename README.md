# Numerical ODE Solving

The code provided uses Euler's method to numerically solve the ordinary differential equation (ODE) describing free-fall motion with air resistance.

## 1. Euler's Method Function

- `euler_method` takes a function `f` (which represents the ODE), initial value `y0`, time range `t0` to `tf`, and step size `h`. It computes the numerical solution using the Euler method.

## 2. ODE Definition

- The ODE for free-fall with air resistance is:

  \[
  \frac{dv}{dt} = g - \frac{k}{m}v
  \]

  where:
  - \( g \) is gravity (9.81 m/s²),
  - \( k \) is the air resistance constant (0.1),
  - \( m \) is the mass of the object (70 kg),
  - \( v \) is the velocity of the object.

## 3. Simulation Setup

- The initial velocity \( v_0 = 0 \) m/s (starting from rest).
- The time range is from \( t_0 = 0 \) to \( t_f = 10 \) seconds with a time step \( h = 0.01 \) seconds.

## 4. Plot

- The velocity over time is plotted using the results from Euler’s method.

Running this code will produce a graph of the velocity as a function of time, showing how air resistance affects the velocity of an object during free fall.
