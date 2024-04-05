from app.io.input import *

def main():
    input_text = console_text_input()
    print(input_text)
    with open('output.txt', 'w') as file:
        file.write(input_text)
    input_text = py_file_read_input('input.txt')
    print(input_text)
    with open('output.txt', 'w') as file:
        file.write(input_text)
    input_text = pandas_file_read_input('input.txt')
    print(input_text)
    with open('output.txt', 'w') as file:
        file.write(input_text)





if __name__ == '__main__':
    main()

