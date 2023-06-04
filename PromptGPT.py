import openai
import yaml
import editJupyter

class PromptGPT:
    def __init__(self, config_path, output_path):
        
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        openai.api_key = self.config['OPENAI_KEY']
        self.output_path = output_path
        self.messages = [{"role": "system", "content": self.config['SYSTEM_VAR']},
                        {"role": "user", "content": "I want to predict wine quality"},
                        {"role": "assistant", "content": "#USER Can you tell me more about the dataset?"},
                        {"role": "user", "content": "I have columns acidity (int), location (string) and quality(int) 1-10"},
                        {"role": "assistant", "content": "#USER I would suggest starting with analyzing the data and determining: 1. Descriptive Statistics: calculate and view means 2. Boxplots: identify outliers and get distribution 3. Correlations: Identify linear relationships"},
                        {"role": "user", "content": "That sounds good, lets do it"},
                        {"role": "assistant", "content": "#SECTION Load Data #USER Here is the code for reading a dataframe and calculating summary statistics #CODE \nimport pandas as pd\n pd.read_csv('data.csv')\n #SECTION Data Analysis ##SUBSECTION Descriptive statistics #CODE \n #Calculate descriptive statistics\n desc_stats = df.describe()\n print(desc_stats)\n"}]
        
        # self.data = json.loads(self.config['FEW_SHOTS'])


    def generate_prompt(self, userPrompt):
        user_message = {"role": "user", "content": userPrompt}
        self.messages.append(user_message)
        return self.messages

    def logResponse(self, response):

        #So yeah super annoying this one:
        #The jupyter file can only be overwritten when open when it has been saved before.
        #To not be forced to interact with the VSCode API for extention programming I am using
        #pyautogui that presses command + save
        #Super hacky and requires to give access to VSCode in the confidentiality settings but the easiest way
        editJupyter.saveFile()

        #Ok the cell Dict still needs to be added to the identity's memory
        cellDict = editJupyter.process_string(response)

        with open(self.output_path,'w',encoding='UTF8') as f:
            f.write(str(self.messages))

        assistant_message = {"role": "assistant", "content": response}
        self.messages.append(assistant_message)

    def main(self, userPrompt):
        self.generate_prompt(userPrompt)
        
        response = "#SECTION Identify Primes with Different Approach #USER Sure, here's another implementation that uses the square root to check for prime numbers. #CODE\n\nimport math\n\ndef is_prime(num):\n  if num <= 1:\n    return False\n  \n  max_divisor = math.floor(math.sqrt(num))\n  \n  for i in range(2, 1 + max_divisor):\n    if num % i == 0:\n      return False\n  \n  return True\n\n#testing the function on simple cases\n\nfor i in range(20):\n  if is_prime(i):\n    print(i)"

        
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        

        print("HERE")
        print(response)
        print(response['choices'][0]['message']['content'])
        
        self.logResponse(response['choices'][0]['message']['content'])
        

        return response['choices'][0]['message']['content']

        """
        self.logResponse(response)