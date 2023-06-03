import openai


class promtGPT:
    
openai.api_key ="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"

def generate_prompt(userPrompt):

    '''
    promt = f"""Answer the prompt in python code. 
                At the end of the function, create a print(function) call with an input example.
                Any comments you want to make include in the code: {userPrompt}"""

    '''
    promt = f"""You are a helpful programming assistant for data scientist. Your objective is to help the user to identify his needs,
    structure the programming problem, confirm and challenge assumptions and logic, and code the solution.
    You are able to edit jupyter notebooks to implement the users needs.
    Let the user first confirm your ideas and assumptions. If he confirms, start implementing one section at a time and await feedback.
    If the user does not confirm, ask questions to iterate the problem.
    You are able to create sections in the jupyter notebook with the command #SECTION and ##/SECTION to close.
    You are also able to write subsections with the command ##SUBSECTION ##/SUBSECTION to close.
    You are able to write code blocks with the command #CODE and #/CODE to close the coding block.
    You are also able to communicate with the user if you provide structures or ask questions with the command #USER and #/USER to close.
    Do not answer anything outside of those blocks and sections. Only start coding and create sections once you understood the problem
    and got a confirmation from the user. Never include #USER blocks in sections. Always put the user block at the beginning.
      Here is the user input: {userPrompt}"""
    
    return promt



def appendChat(userPrompt):


def logResponse(response,output_path):
    with open(output_path,'w',encoding='UTF8') as f:
        f.write(response)

def main(userPrompt):
    # we receive the data from the input window and want to turn it into code via chatGPT
    with open('/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/config.yaml', 'r') as file:
            config = yaml.safe_load(file)



    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(userPrompt),
            temperature=0.6,
            max_tokens=2048,
        )
    
    logResponse(response.choices[0].text,'/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/wineQuality_project/output_sections.txt')
    
    print(response.choices[0].text)
    return response.choices[0].text

