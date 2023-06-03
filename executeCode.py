import subprocess
import os

def insert_text_into_file(text):
    filename = "sample.py"
    with open(filename, "w") as file:
        file.write(text)

def main(editor_content):
    # Take editor content and send to Judge0 code executor
    # Receive the output
    # Change current working directory to the desired path
    new_path = "/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/python_hello_world"
    insert_text_into_file(editor_content)
    
    
    os.chdir(new_path)

    # Update the current environment with the .env vars
    # os.environ.update(env_vars)

    #By the love of god, the subprocess does not run in the first way: subprocess.run(["sh", "./run_example.sh"])
    #It HAS to be done with a shell=True
    #Explanation of chatGPT:
    '''
    When you use subprocess.run() with shell=True, it doesn't "open a shell" in the way you might be thinking (like opening a new terminal window). Rather, it uses the system's shell to interpret the command string you pass.
    So when you pass shell=True and './run_example.sh' as the command, it's equivalent to typing ./run_example.sh in the terminal and hitting enter. In other words, it's already "passing the command" to the shell.
    '''
    # subprocess.run(["sh", "./run_example.sh"])
    result = subprocess.run('./run_example.sh', shell=True, capture_output=True, text=True)
    
    #Query results
    # print('stdout:', result.stdout)
    # print('stderr:', result.stderr)

    #The output is very wordy and contains a lot of unnecessary content.
    parts = result.stdout.split("Base64 decoded stdout:")
    decoded_stdout = parts[1].strip()

    response = decoded_stdout

    return response