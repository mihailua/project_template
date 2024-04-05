import pandas as pd
def console_text_input():
    '''

    Function for user to input text
    saved in string format through console.

    :return:
    string - user input information
    User text typed in console from the function call
    till user pressing enter.
    '''
    return input("User text: ")

def py_file_read_input(filename):
    '''
     Function to input text from reading a file,
     text is saved in string format. Only python embedded methods used.

     Input:
     filename - name of the file to input information from
        string

     :return:
     string - file input information
     '''
    with open(filename, 'r') as file:
        text = file.read()
    return text

def pandas_file_read_input(filename):
    '''
       Function to input text from reading a file,
       text is saved in string format. PANDAS methods used.

     Input:
     filename - name of the file to input information from
        string

       :return:
       string - file input information
       '''
    df = pd.read_csv(filename)
    return df.to_string()



