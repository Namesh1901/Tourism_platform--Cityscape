from flask import Flask, render_template, request

import itertools
import re  # Add this line

app = Flask(__name__)

# ... (Rest of your code)


app = Flask(__name__)

def evaluate_expression(expression):
    return eval(expression)

def find_matching_combinations(values, target):
    matching_combinations = []

    for r in range(1, len(values) + 1):
        for subset in itertools.combinations(values, r):
            subset_sum = sum(subset)
            diff = target - subset_sum

            if diff == 0:
                matching_combinations.append(subset)

    return matching_combinations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    target_str = request.form['target']
    input_str = request.form['input_values']

    # Replace values in brackets with their negatives
    def replace_in_brackets(match):
        value = match.group(1)
        return str(-float(value))

    # Use regular expression to find values in parentheses
    pattern = r'\((-?\d+(\.\d+)?)\)'
    input_str = re.sub(pattern, replace_in_brackets, input_str)

    # Convert modified input string to list of floats
    input_values = list(map(float, input_str.split()))

    target_match = re.match(r'\((-?\d+(\.\d+)?)\)', target_str)
    target_value = float(target_match.group(1)) if target_match else float(target_str)

    matching_combinations = find_matching_combinations(input_values, target_value)

    if matching_combinations:
        print("Matching combinations found:")
        for subset in matching_combinations:
            print(subset)
    else:
        print("No matching combinations found.")

    return render_template('result.html', result=matching_combinations)

def run():
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=5000)

# ... (Your route handlers and other functions)

if __name__ == '__main__':
    run()
