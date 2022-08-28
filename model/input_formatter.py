

class InputFormatter():
    def __init__(self, lang = 'PT') -> None:
        self.lang = lang
        self.sep_preps = None
        self.connectors = None
        self.days = None
        self.months = None
        self.target_words = None
        self.numbers = None
        self.aux_numbers = None
        self.specs_dict = {'sep_preps':None, 'connectors':None, 'days':None, 'months':None, 'target_words':None, 'numbers':None, 'aux_numbers':None}
    
    def read_lang_specs(self):
        specs_file = f'model/langs/{self.lang}.txt'
        with open(specs_file, 'r+') as f:
            for line in f:
                key, value = line.split(' = ')
                self.specs_dict[key] = self.read_spec_value(value)

    def read_spec_value(self, raw_value):
        spec_value = []
        for value in raw_value.split(';'):
            spec_value.append(value)
        return spec_value

    def print_specs_dict(self):
        for key, value in self.specs_dict.items():
            print(f'Key: {key}\nValue: {value}')

if __name__ == "__main__":
    input_formatter = InputFormatter('PT')
    input_formatter.read_lang_specs()
    input_formatter.print_specs_dict()