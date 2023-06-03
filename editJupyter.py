import json
import re
import pyautogui
import time


def saveFile():
      #Windows and linux functionality not coded yet
      pyautogui.hotkey('command', 's')
      

def process_string(input_string):
    commands = ['SECTION', 'SUBSECTION', 'CODE', 'USER']
    current_command = None
    current_content = ''
    output = []

    # Use re.split to handle commands within input_string
    # The regular expression matches only the specified commands
    for word in re.split(r'(#SECTION|#SUBSECTION|#CODE|#USER)', input_string):
        if word.startswith('#') and word[1:] in commands:
            if current_command:
                # Process the previous content before starting a new one
                output.append(process_command(current_command, current_content.strip()))

            current_command = word[1:]
            current_content = ''
        else:
            current_content += word

    # Process the remaining content if there's any
    if current_command:
        output.append(process_command(current_command, current_content.strip()))

    # Load existing json file
    with open('/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/wineQuality_project/test3.ipynb', 'r') as json_file:
        data = json.load(json_file)
        # data = json.loads(json_file.read())

    # Insert output
    data['cells'] = output

    print(str(data))

    # write output to the json file
    with open('/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/wineQuality_project/test1.ipynb','w',encoding='UTF8') as json_file:
        # json_file.write(str(data))
        json.dump(data, json_file, indent=2)

def process_command(command, content):
    if command == 'SECTION':
        return {
          "cell_type": "markdown",
          "metadata": {},
          "source": [
            f"# {content}"
          ]
        }
    elif command == 'SUBSECTION':
        return {
          "cell_type": "markdown",
          "metadata": {},
          "source": [
            f"## {content}"
          ]
        }
    elif command == 'CODE':
        return {
          "cell_type": "code",
          "execution_count": None,
          "metadata": {},
          "outputs": [],
          "source": [
            f"{content}"
          ]
        }


# process_string('!#SECTION Data Analysis !#SUBSECTION Correlations !#CODE #Here is a comment print(\'Hello World!\')')
