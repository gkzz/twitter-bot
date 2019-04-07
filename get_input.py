import yaml

BASE_DIR = "/mnt/c/workspace/twitter-bot"
INPUT_YML = "/input.yml"
input_file = BASE_DIR + INPUT_YML 

class GetInput:

    #BASE_DIR = "/mnt/c/workspace/twitter-bot"
    #INPUT_YML = "/input.yml"
    #input_file = BASE_DIR + INPUT_YML 

    def __init__(self, _file):  
      if type(_file) == str:
          self._file = _file
      else:
          raise ValueError(
              "type(_file): {}".format(type(_file))
          ) 
    
    def get_input_yml(self):
        try:
            with open(self._file, 'r+') as file:
                input = yaml.safe_load(file)
        except FileNotFoundError:
            return {}
        return input

#print(type(input_file))
obj = GetInput(input_file)
input = obj.get_input_yml()

dicts = {}
for key, value in input.items():
    dicts[key] = value
    #print("dicts: {}".format(dicts))

print("dicts: {}".format(dicts))
print("techblog" in dicts.keys())
