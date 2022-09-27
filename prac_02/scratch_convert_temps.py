temps_input = open('temps_input.txt', 'r')
temps_output = open('temps_output.txt', 'w')
for line in temps_input:
    fahrenheit = float(line)
    celsius = 5.0 / 9.0 * (fahrenheit - 32)
    print(celsius, file=temps_output)
temps_output.close()
results_file = open('temps_output.txt', 'r')
print(results_file.read())

