# add_text
a method to display a options in screen and choose one to execute the function of the choosen option .


## How To Use  
from TerminalFramework call display_options() and it takes 2 parameters :

 1- options_list : list of the options you want to show in screen

 2- functions_list : list of functions each option take function by index


```python
TerminalFramework.display_options(options_list, functions_list)
```

**input**
```python
def option1_function():
    url_prompt = "Enter the URL: "
    url = Terminal_Framework.get_user_input(0,0,url_prompt)
    file_name = 'pic.jpeg'
    r = requests.get(url, timeout=10)
    if r.ok:
        with open(file_name, 'wb') as f:
            f.write(r.content)
def op2():
    print('jj')
def op3():
    print('tt')

options_list = ['Option 1', 'Option 2', 'Option 3']
functions_list = [option1_function, op2, op3]
Terminal_Framework.display_options(options_list, functions_list)
```
![Example](static/display_options.png)


**output**

 if you select option1 and press Enter Key the function of option1 will run .

 Note : fun1. download a picture from internet .

![Example](static/display_options_test.png)

 function1 complete execution....


 The Resulte : 

![Example](static/display_options_output.png)

