from nicegui import ui
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# === Function to plot ===
def f(x):
    return x**2

def df(x):
    return 2*x

# === Helper to plot curve and tangent ===
def plot_with_secant_and_tangent(a, h):
    x = np.linspace(-5, 5, 400)
    y = f(x)
    y_a = f(a)
    slope = df(a)
    # Tangent line: y = slope*(x - a) + y_a
    tangent_y = slope * (x - a) + y_a
    
    # Secant line
    a_h = a + h
    if h != 0:
        secant_slope = (f(a_h) - y_a) / h
        secant_y = secant_slope * (x - a) + y_a
    else:
        secant_slope = None
        secant_y = None

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x, y, label='f(x)')
    ax.plot(x, tangent_y, '--', label=f'Tangent at x={a:.2f}')
    ax.scatter([a], [y_a], color='red', zorder=5, label='Point (a, f(a))')
    if h != 0:
        ax.plot(x, secant_y, ':', color='green', label=f'Secant a→a+h (h={h:.2f})')
        ax.scatter([a_h], [f(a_h)], color='orange', zorder=5, label='Point (a+h, f(a+h))')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Derivative at a Point: Secant & Tangent')
    ax.legend()
    ax.grid(True)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 25)

    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    return f'data:image/png;base64,{img_b64}', secant_slope

# === UI ===
ui.label('Interactive Applet: Derivative at a Point').classes('text-h5 q-mb-md')
ui.label('Drag the slider to move the point. The tangent line and derivative value update in real time.')

ui.label('Choose x=a')
slider_a = ui.slider(min=-4, max=4, value=1, step=0.01)
ui.label('Choose h (distance from a):')
slider_h = ui.slider(min=-2, max=2, value=1, step=0.01)

img = ui.image('').classes('q-mt-md')
deriv_label = ui.label('').classes('q-mt-md')
secant_label = ui.label('').classes('q-mt-xs')
reflection_prompt = ui.label('What do you notice as h gets smaller?')
reflection_input = ui.textarea(placeholder='Type your thoughts here...').classes('q-mb-lg')

# Update plot and value on slider move
def update_plot(e=None):
    a = slider_a.value
    h = slider_h.value
    img_src, secant_slope = plot_with_secant_and_tangent(a, h)
    img.source = img_src
    deriv_label.text = f"Tangent slope f'({a:.2f}) = {df(a):.2f}"
    if h != 0:
        secant_label.text = f"Secant slope = (f({a:.2f}+{h:.2f}) - f({a:.2f})) / {h:.2f} = {secant_slope:.2f}"
    else:
        secant_label.text = "Secant slope is undefined when h = 0 (becomes tangent)."

slider_a.on('update:model-value', update_plot)
slider_h.on('update:model-value', update_plot)

# Initial plot
update_plot()

ui.run(title='Derivative at a Point', reload=False)
