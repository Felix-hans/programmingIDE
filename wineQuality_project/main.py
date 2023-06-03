import sys
import os

# Add the parent folder path to the sys.path list
sys.path.append('/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE')

#import getGPTResponse
import PromptGPT

#getGPTResponse.main('I want to create a data analysis pipeline')

# Create a PromptGPT object
prompt_gpt = PromptGPT.PromptGPT(
    config_path="/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/config.yaml", 
    output_path='/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/wineQuality_project/output_sections.txt'
)


while True:
    userPrompt = input("Input: ")
    prompt_gpt.main(userPrompt)
    if userPrompt.lower() == 'stop':
        break
    

#os.remove('/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/wineQuality_project/test3.ipynb')
#getGPTResponse.logResponse(response, '/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/wineQuality_project/test3.ipynb')