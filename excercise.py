def draw_shape(options):
  shape = ""

  for r in range(options['rows']):
    for c in range(options['cols']):
      shape += options['char']

    shape += "\n"

  return shape


your_code_goes_here = {'cols': 4, 'rows': 4, 'char': '*'}
print(draw_shape(your_code_goes_here))

your_code_goes_here = {'cols': 9, 'rows': 3, 'char': '0'}
print(draw_shape(your_code_goes_here))
