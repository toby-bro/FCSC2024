#!/bin/bash
source env/bin/activate

# Function to check if input is a number

# Define a function to retrieve elements from the file
get_element() {
    # Get the input number
    input_number="$1"

    # Decompose the input number into two parts
    first_part="${input_number:0:2}"
    second_part="${input_number:2}"

    # Remove leading zeros
    first_part=$(echo "$first_part" | sed 's/^0*//')
    second_part=$(echo "$second_part" | sed 's/^0*//')

    # Increment the parts
    first_part=$((first_part+13))
    ((second_part++))

    # Retrieve the element from the file
    result=$(awk -v row="$first_part" -v col="$second_part" 'BEGIN{FS=","; OFS=",";} NR==row {print $col}' arrange.py | cut -d "'" -f 2)

    # Print the result
    echo "$result"
}



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

## Decompose the input number
#num1y="${num1:0:2}"
#num1x="${num1:2}"
#
#num2y="${num2:0:2}"
#num2x="${num2:2}"
#
#num1=$(sed -n "$($num1y)p" "$temp_file" | awk -v col="$num1x" '{print $col}')

num1=$(get_element $1)
num2=$(get_element $2)

#echo $num1 $num2


# Replace the occurrences of num1 and num2 within the specified range
sed -i '13,29 {
    s/'"$num1"'/temp_value/g
    s/'"$num2"'/'"$num1"'/g
    s/temp_value/'"$num2"'/g
}' "$temp_file"

# Replace the original Python file with the modified one
mv "$temp_file" "$python_script"

#echo "Python file '$python_script' has been modified to exchange the two numbers between lines 13 and 20."
python arrange.py
#xdg-open output.png 2>/dev/null &
