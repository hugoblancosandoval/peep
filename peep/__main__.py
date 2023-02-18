import crayons
import plac
from pathlib import Path
from peep import __app_name__, __version__, file_utils
import inquirer

@plac.opt('filename', 'Do you already know which ebook you want to take a peep into?', Path)
@plac.flg('debug', 'Enables debug mode')
@plac.flg('version', 'Show the version and exists')
def main(filename, debug=False, version=False):
    if version:
        print('{} v{}'.format(crayons.green(__app_name__), __version__))
        import sys; sys.exit()

    if not filename:
        files = file_utils.load()
        question = [inquirer.List('ebooks', message="Please an ebook", choices=files)]
        answers = inquirer.prompt(question)
        
    else:
        print('{}: Implement doing for one ebook '.format(crayons.red('TODO: ')))
    
if __name__ == "__main__":
    plac.call(main)
