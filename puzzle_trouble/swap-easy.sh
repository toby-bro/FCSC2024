#!/bin/bash
source env/bin/activate

# Function to check if input is a number
is_number() {
    re='^[0-9]+$'
    if ! [[ $1 =~ $re ]]; then
        return 1
    else
        return 0
    fi
}

while true
do

# Prompt user to input two numbers
while true; do
    read -p "Enter the first number: " num1
    if is_number "$num1"; then
        break
    else
        echo "Invalid input. Please enter a valid number."
    fi
done

while true; do
    read -p "Enter the second number: " num2
    if is_number "$num2"; then
        break
    else
        echo "Invalid input. Please enter a valid number."
    fi
done

## Prompt user to input two numbers
#read -p "Enter the first number: " num1
#read -p "Enter the second number: " num2

pkill -f 'output.png'

# Modify the Python file
python_script="arrange.py"  # Replace with your Python file name
temp_file="temp.py"


# Check if the Python file exists
if [ ! -f "$python_script" ]; then
    echo "Error: Python file '$python_script' not found."
    exit 1
fi

# Create a temporary file to store modified Python code
cp "$python_script" "$temp_file"

# Replace the occurrences of num1 and num2 within the specified range
sed -i '13,20 {
    s/'"$num1"'/temp_value/g
    s/'"$num2"'/'"$num1"'/g
    s/temp_value/'"$num2"'/g
}' "$temp_file"

# Replace the original Python file with the modified one
mv "$temp_file" "$python_script"

#echo "Python file '$python_script' has been modified to exchange the two numbers between lines 13 and 20."
python arrange.py
xdg-open output.png 2>/dev/null &
done
