import PromptGPT
# self.messages = [{"role": "system", "content": 'Answer in python code'}]


prompt_gpt = PromptGPT.PromptGPT(
    config_path="/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/config.yaml", 
    output_path='/Users/fhans/Documents/GenerativeBenchmarking/programmingIDE/wineQuality_project/output_sections.txt'
)

prompt_gpt.main('write a function to identiy primes')