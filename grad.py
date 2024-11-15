from gradpyent.gradient import Gradient

# Define the start and end colors as RGB, HTML, or KML
start_color = 'ff0000ff'  # Red in RGB
end_color = 'ffff0000'  # Blue in HTML

# Instantiate the gradient generator, opacity is optional (only used for KML)
gg = Gradient(gradient_start=start_color, gradient_end=end_color, opacity=1.0)

# Define the input list
input_list = [0, 0.5, 1]

# Generate the gradient
gradient = gg.get_gradient_series(series=input_list, fmt='html')

print(gradient)
