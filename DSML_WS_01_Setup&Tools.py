#!/usr/bin/env python
# coding: utf-8

# # `DSML_WS_01` - Setup & Tools

# In this tutorial we will introduce the main tools we will be working with throughout the rest of the course. Everything shown here will become the basis on top of which we will build more sophisticated (and hopefully fun) data science and machine learning tasks.
# 
# We will go through the following:
# 
# - `Git` and `GitHub` as central course repository
# - `Anaconda` installation
# - `Jupyter Notebook` introduction
# - `Python` introduction

# ---

# ## `Git` and `GitHub`

# [Git](https://git-scm.com) is an open-source distributed version-control system that has gained increasing popularity in recent years. It allows large teams of software engineers or data scientists to collaboratively work on projects, while keeping track of changes.
# 
# In this course we will use a git repository hosted by [GitHub](https://github.com/about) to **share code**, **small data snippets**, links to **lecture material** and **course infromation** with you.
# 
# For the purpose of this course you will not require a deep understanding of Git. All you need is access to our Chair's public GitHub repository from where you can download code and data. This repo can be accessed here:
# - Navigate to [`https://github.com/IS3UniCologne/DSML_2021`](https://github.com/IS3UniCologne/DSML_2021)

# You should see a screen similar to this one (shown here in dark mode):

# ![GitLab home](DSML_WS_01_GitHub_Screen.png)

# You can view and follow this course via this `GitHub` repository. You can also download all material onto your local machines for when you need to work with code.
# 
# **Note**: If you have some experience with using `git` you may also whish to clone the repository on you local machine for ease of use. **We will give you a quick introduction into git in a future session once you have familiarized yourself a little with the tools presented today!**

# ### <font color='green'>Please download the course folder from `GitHub` now</font>

# ---

# ## `Anaconda`

# We highly recommend that you install the [Anaconda Python Distribution](http://docs.continuum.io/anaconda/install/). It will make your life much easier. You can download and install Anaconda on Windows, OSX and Linux.
# 
# There are two options:
# 
# - **Option 1** (probably the easiest): Install the full **Anaconda distribution**, which comes with a lot of pre-installed packages (incl. Jupyter Notebook) and a package manager graphical user interface (GUI). It is available for download [here](https://www.anaconda.com/distribution/).
# - **Option 2** (for slightly more advanced users and if your are short on disk space): Install the much lighter **MiniConda distribution** which essentially is just the Conda package manager and Python. From there your can simply install Python packages as required via the Terminal (Mac, Linux) or the Anaconda Command Prompt (Windows). It is available for download [here](https://docs.conda.io/en/latest/miniconda.html).

# ### <font color='green'>Please download and install `Anaconda` or `MiniConda` now and follow the below steps </font>

# After installing, open up a terminal:
# 
# * If you are on a **Windows** computer, use the "Anaconda Command Prompt" from the Start menu. 
# * On a **Mac**, start up the "Terminal". 
# * In **Linux**, use any of the terminals available.

# If you have installed the full Anaconda Distribution, to ensure all you packages are up to date, run the following two commands consecutively
# 
# ```
# conda update conda
# conda update jupyter numpy sympy scipy matplotlib pandas
# 
# ```

# If you have installed the Miniconda Distribution, which comes without any pre-installed packages, run the following three commands consecutively
# 
# ```
# conda update conda
# conda install jupyter
# conda install numpy scipy sympy matplotlib pandas
# 
# ```

# You can easily check which packes and libraries are installed by executing the following command in your respective terminal:
# 
# ```
# conda list
# 
# ```

# ---

# ## `Jupyter Notebook`

# The main computational tool we will be using during this course is the [Jupyter notebook](http://jupyter.org/). Notebooks are a convenient way to thread text, code and the output it produces in a simple file that you can then share, edit and modify. You can think of notebooks as the __Word document of Data Scientists__.
# 
# Jupyter is a browser-based coding environment, used extensively for prototyping and interactive development in data science applications.  Jupyter Notebook is an evolution of an older project called the IPython Noteboook (this is the origin of the notebook file extension ".ipynb").
# 
# The central unit within a Jupyter Notebook are "cells".  These cells can be either contain code or Markdown (a simple formatting language, which can also include things like LaTeX equations).  The dropdown menu at the top of the screen indicates the type of the current cell.  
# 
# In the following we explain the basic concepts of how to use Jupyter

# ### <font color='green'> Follow the below instructions to start up the notebook we are currently working in </font>

# ### Start a notebook

# In order to begin a notebook session, you need to do it from what is called the *command line*, a terminal window that allows you to interact with your computer through written commands. This is how you can start up a terminal:
# 
# * If you are on a **Windows** computer, you can start the "Anaconda Command Prompt" from the Start menu. 
# * On a **Mac**, fire up the Terminal utility. 
# * In **Linux**, use any of the terminals available.
# 
# Then type the following command
# 
# ```
# > conda activate base
# ```
# 
# **NOTE**: ignore `source` if you are on Windows and simply type `activate base`.
# 
# Then launch `Jupyter` by typing on the same terminal:
# 
# ```
# > jupyter notebook
# ```
# 
# This should bring up a browser window with a home page that looks more or less like this (although probably with a different list of files):

# ![Jupyter home](DSML_WS_01_JupyterNotebook_Start_Screen.png)

# Navigate to the folder where you have placed the `DSML_WS_01_Setup&Tools.ipynb` file for this tutorial and click on it. This will open the notebook on a different tab. You are now on the interactive version of the notebook!

# ![Jupyter home](DSML_WS_01_JupyterNotebook_Target_Folder.png)

# When you are finished with the session, you can save the notebook with `File -> Save and Checkpoint` or by clicking the save button. Everything you do on the notebook (text, code and output) is saved into an `.ipynb` file that you can open later, share, commit to a remote git repo, etc.

# ### Cells

# The main building block of notebooks are cells. These are chunks of content which can be cut, pasted, and moved around in a notebook. 
# 
# Code cells can be executed by pressing the <i class="fa fa-step-forward"></i> button at the top of the notebook, or 
# by simultaneously pressing `shift + enter` (execute and move to the next cell) or `ctrl + enter` (execute and stay on that cell).  All Python code is executed in a single running Python environment, called the "Kernel" in Jupyter Notebook.  Variables are shared across all cells, and the code is executed in the order in which the cells are run (not necessarily sequential in the notebook), which can get your notebook into rather confusing states if you don't always execute cells in order.
# 
# Cells can be of two types:
# 
# * **Text**, (or markdown) like the one where this is written.
# * **Code**, like the following one below:
# 
# **Tip**: you can easily switch between text (markdown) and code model via shortcuts. If you press `<escape>` and then `y` you switch to **Code**. If you press `<escape>` and then `m` you switch to **Text** (i.e. markdown).

# In[1]:


# below is a code cell


# In[2]:


# Let's type some code by assigning a variable and printing it

var = 5+7
print(var)


# In[3]:


# Below is a text cell
# Laslo 4 Life


# *this is some text*
# 
# 

# ### Shortcuts

# In[ ]:


# I love my life


# You can create a new cell by clicking `Insert` -> `Cell Above`/`Below` in the top menu. By default, this will be a code cell, but you can change that on the `Cell` -> `Cell Type` menu. Choose `Markdown` for a text cell. Once a new cell is created, you can edit it by clicking on it, which will create the cursor bar inside for you to start typing.
# 
# **Tip**: Alternatively, cells can also be created with shortcuts. If you press `<escape>` and then `b` (`a`), a new cell will be created below (above). 

# In[ ]:





# In[ ]:





# As eluded to above, shortcuts can make your life a lot easier. There is a whole bunch of shortcuts you can explore by pressing `<escape>` and `h` (press `<escape>` again to leave the help).

# ### Code and its output
# 
# A particularly useful feature of notebooks is that you can save, in the same place, the code you use to generate any output (tables, figures, etc.). As an example, the cell below contains a snipet of Python that returns a printed statement. This statement is then printed below and recorded in the notebook as output:

# In[4]:


# Print "hello world"


# In[5]:


print("Hello, world!!!")


# Note also how the notebook has automatic syntax highlighting support for Python. This makes the code much more readable and understandable. More on Python as a coding language below.

# ### Markdown

# Text cells in a notebook use the [Github Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/) markup language. This means you can write plain text with some rules and the notebook renders a more visually appealing version of it. Let's see some examples:
# 
# * **BOLD**:
# 
# `This is **bold**.`
# 
# Is rendered:
# 
# This is **bold**.
# 
# * **ITALIC**:
# 
# `This is *italic*.`
# 
# Is rendered:
# 
# This is *italic*.
# 
# * **LISTS**:
# 
# You can create unnumbered lists:
# 
# ```
# * Item 1
# * Item 2
# * ...
# ```
# 
# Which will produce:
# 
# * Item 1
# * Item 2
# * ...
# 
# Or you can create numbered lists:
# 
# ```
# 1. First element
# 1. Second element
# 1. ...
# ```
# 
# And get:
# 
# 1. First element
# 1. Second element
# 1. ...
# 
# Note that you don't have to write the actual number of the element, just using `1.` always produces a numbered list.
# 
# You can also nest lists:
# 
# ```
# * First unnumbered element, which can be split into:
# 
#     1. One numbered element
#     2. Another numbered element
# 
# * Second element.
# * ...
# ```
# 
# * First unnumbered element, which can be split into:
# 
#     1. One numbered element
#     2. Another numbered element
# 
# * Second element.
# * ...
# 
# This creates many oportunities to combine things nicely.
# 
# * **LINKS**
# 
# `You can easily create hyperlinks, for example to [WikiPedia](https://www.wikipedia.org/).`
# 
# You can easily create hyperlinks, for example to [WikiPedia](https://www.wikipedia.org/).
# 
# * **HEADINGS**: including `#` before a line causes it to render a heading.
# 
# ---
# 
# `# This is Header 1`
# 
# Turns into:
# 
# # This is Header 1
# 
# ---
# 
# `## This is Header 2`
# 
# Turns into:
# 
# ## This is Header 2
# 
# ---
# 
# `### This is Header 3`
# 
# Turns into:
# 
# ### This is Header 3
# 
# And so on...
# 
# ---
# 
# You can see a more in detail introduction in the following links:
# 
# >* https://help.github.com/articles/markdown-basics/
# 
# >* https://help.github.com/articles/github-flavored-markdown/

# If you use headers right the Table of Contents feature will provide a nice tool to navigate your notebook.

# ### Rich content in a notebook

# Notebooks can also include rich content from the web. For that, we need to import the `display` module. This module allows you to embed, for example:
# - Youtube videos
# - HTML code
# - interactive maps
# - sound content
# - etc.
# 
# We will not cover these aspects in great detail but leave this up to you to explore in your own time, if you are interested. A thorough exploration of these features is available at the following [link](https://notebook.community/CestDiego/emacs-ipython-notebook/tests/notebook/nbformat3/Display%20System).
# 

# ## `Python`

# The main bulk of the course relies on the [Python](https://www.python.org/) programming language. Python is a [high-level](https://en.wikipedia.org/wiki/High-level_programming_language) programming language widely used today. To give a couple of examples of its relevance, it is underlying [most of the Dropbox](https://www.quora.com/How-does-dropbox-use-python-What-features-are-implemented-in-it-any-tangentially-related-material?share=1) systems, but also heavily [used](https://www.python.org/about/success/usa/) to control satellites at NASA.
# 
# This course uses Python because it has emerged as one of the main and most solid options for Data Science, together with other free alternatives such as R. Python is widely used for data processing and analysis both in academia and in industry. There is a vibrant and growing scientific community, working at both universities and companies, that supports and enhances its capabilities for data analysis by providing new and refining existing extensions (a.ka.a. libraries, see below). All of this means that, whether you are thinking of continuing in Higher Education or trying to find a job in industry, Python will be an importan asset that employers will significantly value.
# 
# Being a high-level language means that the code can be "dynamically interpreted", which means it is run on-the-fly without the need to be compiled. This is in contrast to "low-level" programming languages, which first need to be converted into machine code (i.e. compiled) before they can be run. With Python, one does not need to worry about compilation and can just write code, evaluate, fix it, re-evaluate it, etc. in a quick cycle, making it a very productive tool. The rest of this tutorial covers some of the basic elements of the language, from conventions like how to comment your code, to the basic data structures available.
# 
# If the marterial covered here is all new to your and to support your learning process we recommend the following resources:
# - [Standard Python Tutorial](https://docs.python.org/3/tutorial/) 
# - [Python Data Science Handbook (free ebook)](https://github.com/jakevdp/PythonDataScienceHandbook)
# - [Data Science from Scratch (free ebook)](http://math.ecnu.edu.cn/~lfzhou/seminar/[Joel_Grus]_Data_Science_from_Scratch_First_Princ.pdf)
# 
# The most common "built-in" data types you will interact with when doing data science work are lists and dictionaries (there are of course additional types like Numpy Arrays, Pandas Dataframes, and others, but these are provided by external libraries).  It's good to have a brief understanding of how to use these data structures effectively.

# ### Python data structures

# The standard python you can access without importing any additional libraries contains a few core data structures that is very handy to know. Most of data analysis is done on top of other structures specifically designed for the purpose (numpy arrays and pandas dataframes, mostly. See the following sessions for more details), but some understanding of these core Python structures is very useful. In this context, we will look at three: `values` (intergers and floats), `lists`, and `dictionaries`.
# 
# An abundance of other data structures, which can be specific to external libraries are available (such as Numpy Arrays, for example). We will cover some of these in later tutorials

# #### Values 
# 
# These are the most basic elements to organize data and information in Python. You can think of them as numbers (integers or floats) or words (strings). Typically, these are the elements that will be stored in lists and dictionaries.
# 
# An `integer` is a whole number:

# In[12]:


# assign a value to a variable i and return type of i


# In[13]:


i = 5
type(i)


# A `float` is a number that allows for decimals:

# In[9]:


f = 5.5
type(f)


# In[10]:


fw = 5.
type(fw)


# In[11]:


fw == i


# Note that a float can also not have decimals and still be stored as such:

# In[11]:


fw = 5.
type(fw)


# The standard Python language includes some data types (e.g. lists, tuples, dictionaries, etc.) and allows many basic operations (e.g. sum, product, etc.). For example, right out of the box, and without any further action needed, you can use Python as a calculator:

# In[14]:


5 + 5


# In[15]:


2. / 3


# In[16]:


(3 + 5) * 2. / 3


# In[18]:


4%2 # this is called the modulo (returns the remainder of the division)


# A `string`is a word, which can be delimited by single or double quotation marks (quotes have to match): 

# In[19]:


A = "data science"
B = 'and machine learning'
print(A,B)


# In[20]:


type("check")


# In[21]:


type (A)


# Mathematical operations can be applied for strings but they have different function. Only sum `+` and multiply `*` can be used for strings. Note that the "+" operator concatenates two strings without a space in between, whereas using the print function and a comma in between several strings does add a space (see above).

# In[24]:


print(A, B)
print (A + B)
print (A + " " + B)
print ((A+"")*3)


# * **Lists**: a list is an ordered sequence of values that can be of mixed types. They are represented between squared brackets (`[]`) and, although not very efficient in memory terms, are very flexible and useful to "put things together".
# 
# For example, the following list of integers:

# In[25]:


l = [1, 2, 3, 4, 5]
l


# In[26]:


type(l)


# Or the following mixed one:

# In[27]:


m = ['a', 'b', 5, 'c', 6, 7.6]
m


# Lists can be queried and sliced. For example, the first element can be retrieved by:

# In[28]:


m[0]


# In[29]:


type(m[0])


# Or the third to the fourth:

# In[30]:


m[4]


# In[31]:


m[2:5]


# Lists can be added:

# In[32]:


l + m


# New elements added:

# In[33]:


l.extend(m)
l


# Or modified:

# In[34]:


m[1]


# In[35]:


m[1] = 'two'
m[1]


# In[36]:


m


# * **Dictionaries**: dictionaries are unordered collections of "keys" and "values". A key, which can be of any kind, is the element associated with a "value", which can also be of any kind. Dictionaries are used when order is not important but you need fast and easy lookup. They are expressed in curly brackets, with keys and values being linked through columns.
# 
# For example, we can think of a dictionary to store a series of names and the ages of the people they represent:

# In[43]:


ages = {'Ana': 24, 'John': 20, 'Li': 27, 'Ivan': 40, 'Tali':33}
ages


# In[44]:


type(ages)


# Dictionaries can then be queried and values retrieved easily by using their keys. For example, if we quickly want to know Li's age:

# In[46]:


ages['John']


# Similarly to lists, you can modify and assign new values:

# In[47]:


ages['Karsten'] = 28
ages


# Using this property, you can create entirely empty dictionaries and populate them later on:

# In[48]:


newdict = {}
newdict['key1'] = 1
newdict['key2'] = 2
newdict


# ### Variables

# A basic feature of Python is the ability to assign a name to different "things", or objects. These can also be called  "variables". We have already seen that in the example above but, to make it more explicit, let us make it even simpler. For example, an object can be a single number:

# In[49]:


flt = 3.1


# In[50]:


flt


# Or a name, also called "string":

# In[51]:


a = 'Hello World'


# You can check what type an object is also easily:

# In[52]:


type(a)


# `int` is short for "integer" which, roughly speaking, means an whole number. If you want to save a number with decimals, you will be using floats:

# In[53]:


c = 1.5
type(c)


# As mentioned, what we understand as letters in a wide sense (spaces and other signs count too) is called "strings" (`str` in short):

# In[54]:


b="this is a string"


# In[55]:


type(b)


# ### Help

# A very handy feature of Python is the ability to access on-the-spot help for its different functions. This means that you can check what a function is supposed to do, or how to access it, right inside your Python session. Of course, this also works handsomely inside a notebook. There are a couple of ways to access the help. 
# 
# 

# As you can see, this brings up a sub-window in the browser with all the information you need.
# 
# If, for whatever reason, you needed to print that info into the notebook itself, you can do the following:

# In[56]:


help(float)


# To call up the help menu another extremely useful shortcut is the key combination `shift+tab`. This, when pressed while your cursor is inside a function or method will produce a pop-up help menu.

# In[45]:


int(2.3)


# ### Control flow (a.k.a. `for` loops and `if` statements)

# Although this does not intend to be a comprehensive introduction to computer programming or general purpose Python (check the references for that, in particular Allen Downey's [book](http://www.greenteapress.com/thinkpython/thinkpython.html)), it is important to be aware of two building blocks of almost any computer program: `for` loops and `if` statements. 
# 
# 
# They can also come in very handy in cases where you some extra functionality out of standard methods. Without further ado, let us have a look and the two single most relevant tools of computer programming.

# * `for` loops
# 
# The general structure of a `for` loop is:
# 
# ```
# for conditional == True:
#     Do
# ```
# 
# These allow  you to repeat a particular action or task over a sequence. As an example, you can print your name ten times without having to type it yourself every single time:

# In[57]:


# let's define a list of values from 0 to 9

lst = [0,1,2,3,4,5,6,7,8,9]


# In[2]:


for i in lst:
    print('Denzel Washington')


# Note that you do not have to create a list for the sequence you want to loop over. Alternatively you can use the buil-in `range()`function.

# In[3]:


for i in range(10):
    print('Denzel Washington')


# Note a couple of features in the loop:
# 
# 1. You loop *over* a sequence, in this particular case the sequence of ten numbers defined in `lst`or created by `range(10)`.
# 1. In every step, for every element of the sequence in this case, you repeat an action. Here we are printing the same text, `my name`.
# 1. Although not used in this simple loop, each of the elements you loop over can be accessed inside the loop. This can be irrelevant, as in the loop above, or extremely useful, it depends on the context. For example, see a case where you use the value of the sequence in each step:

# In[60]:


for i in range(10):
    print("I am at step ", i)


# One more note: for convention, we are calling the element of the sequence `i` (for iterator), but this could be named anything. In fact, in many cases, more meaningful names make code much more readable. For example, you could think of a re-write of the loop above as:

# In[61]:


for step in range(10):
    print("I am at step ", step)


# * `if` statements
# 
# We have just seen how `for` loops allow you to repeat an action over a sequence. In the case of `if` statements, these allow you to select or restrict such actions to only those cases that meet a condition(s) you specify in the statement.
# 
# The general structure of `if` statements is:
# 
# ```
# if conditional 1:
#     statement 1
#     
# elif conditional 2:
#     statement 2 
#     
# else : 
#     statement 3
# ```
# 
# 
# For example, if you think of the loops written above, you might want to only print those that are odd, skipping those that are even:

# In[62]:


for i in range(10):
    if i%2 == 0:
        print(i)


# The part `i%2` (also called modulo), is one way Python can check if a number is odd (as the modulo returns the remainder of a division). The important bit in this loop, however, is that we are using an `if` statement to select only those candidates that meet the condition. In other words, what we are doing is looping over every number in the sequence from zero to nine and checking if they are even or odd (`i.e. if i%2 != 0` the number is odd). If they meet the condition, i.e. they are odd, then we proceed and print them on the screen.

# A full `if` statement also allows for an action to be taken if the original condition is not satisfied. This is called an "ifelse" statement. For example, you can think of a loop that prints the type of each number in a sequence:

# In[63]:


for i in lst:
    # Check if it is odd
    if i%2 != 0:
        print(i, ' is odd')
    # If not odd (even), then do the following
    else:
        print(i, ' is even')


# ### Functions

# The last part of quick overview relates to functions, or more properly termed, methods. The motivation is that, so far, we have only seen how you can create Python code that, if you want to run again somewhere else, you need to copy and paste entirely. However, as we will see in more detail later in the course, one of the main reasons why you want to use Python for data analysis, instead of a point-and-click graphical interface like SPSS, for instance, is that you can easily reuse code and re-run analyses easily. Methods help us accomplish this by encapsulating snippets of code that perform a particular task and making them available to be called.
# 
# We have already *used* methods here. When we call `range()`, we are using one of them. Now, we will see how to *create* a method of our own that performs the specific task we want it to do. For example, let us create a very simple method to reproduce the first loop we created above:

# In[64]:


def run_simple_loop():
    for i in range(10):
        print(i)
    return None


# Already with this simple method, there is a bunch of interesting things going on:
# 
# * First, note how we define a bit of code is a method, as oposed to plain Python: we use `def` followed by the name of our function (we have chosen `run_simple_loop`, but we anything could have done).
# * Second, we append `()` after the name, and finish the line with a colon (`:`). This is necessary and will allow us to specify requirements for the function (see below).
# * Third, realize that everything inside a function needs to be indented. This is a core property of Python and, although some people find it odd, it enhances readibility greatly.
# * Fourth, the piece of code to do the task we want, printing the sequence of numbers, is inside the function in the same way it was outside, only properly indented.
# * Fifth, we finish the method with a line starting by `return`. In this case, we follow it with `None`, but this will change as methods become more sophisticated. Essentially, this is the part of the method where you specify which elements you want it to return and save for later use.
# 
# Once we have paid attention to these elements, we can see how the method can be *called* and hence the code inside it executed:

# In[65]:


run_simple_loop()


# This is the simplest possile method you can write: you do not require anything, just executing it, and the code produces and output (the printout) but it is not saved anywhere. The rest of this section relaxes these two aspects to allow us to build more complex, but also more useful, methods.
# 
# First, you can specify "arguments" to be passed that modify the behaviour of the method. Remember how we called `np.arange` with a number that implied the length of the sequence we wanted returned. We can do the same thing in our own function. The main aspect to pay attention to in this context is that the arguments need to be variables, not particular values. Let us see a modified example of our method:

# In[66]:


def run_simple_loopX(x):
    for i in range(x):
        print(i)
    return None


# We have replaced the fixed length of the sequence (10) by a variable named `x` that allows us to specify *any value we want* when we call the method:

# In[67]:


run_simple_loopX(3)


# In[68]:


run_simple_loopX(2)


# Our function does not save (or more accurately return) anything:

# In[73]:


b = run_simple_loopX(3)


# In[6]:


#b


# We can modify this using the last line of a method. For example, let us assume we want to return a sequence as long as the series of numbers we print on the screen. The method should be:

# In[71]:


def run_simple_loopX(x):
    for i in range(x):
        print(i)
    return range(x)


# Note the main difference: instead of returning `None`, we are telling Python to return a sequence, which has the same length as the one used to specify the loop. Now, there is an alternative way of being more efficient in this method, and that is assigning the sequence to a new object and using it when necessary later on. The results are exactly the same, but there are less computations performed and, more critically, we minimize the chances of making mistakes.

# In[75]:


def run_simple_loopX(x):
    seq = range(x)
    for i in seq:
        print(i)
    return seq


# Either of these two new versions of the method return an output:

# In[76]:


a = run_simple_loopX(13)
#b = run_simple_loopXout(3)


# In[77]:


a


# In[78]:


b


# The advantage of methods, as oposed to straight code, is that they force us to think in a modular (object oriented) way, helping us identify exactly what it needs to be done, in what order, and what it is required. Encapsulating these atomic bits of functionality in methods allows us to write things once and flexibly use them everywhere, saving us time (and headaches) in the long run.

# A final note on functions. It is important that, whenever you create a function, you include some documentation about what it expects, what it does, and what it returns. Although there are many ways of doing this, the typical convention is as follows:

# In[79]:


def run_simple_loopXout(x):
    
    """
    Print out the values of a sequence of certain length
    ...
    
    Arguments
    ---------
    x     : int
            Length of the sequence to be printed out
    
    Returns
    -------
    seq   : np.array
            Sequence of values printed out
    """
    
    seq = np.arange(x)
    for i in seq:
        print(i)
    return seq


# Documentation, as any string, are highlighted in red on a notebook. Let us have a look at the structure and components of a well-made documentation (also called "docstring"):
# 
# * It is encapsulated between triple commas (`"""`).
# * Begins with a short description of what the method does. The shorter the better, the more concise, the even better.
# * There is a section called "Arguments" that lists the elements that the function expects. 
# * Each argument is then listed, followed by its type. In this case it is an object `x` that, as we are told, needs to be an integer.
# * The arguments are followed by another section that specifies what the function returns, and of what type the output is.
# 
# Documentation in this way is very useful to remember what a function does, but also to force yourself to write clearer code. A bonus is that, if you include documentation in this way, it can be checked with the standard `help` or `?` systems reviewed above:

# In[80]:


get_ipython().run_line_magic('pinfo', 'run_simple_loopXout')


# In[81]:


help(run_simple_loopXout)


# In[ ]:


run_simple_loopXout()


# ### Exercise to work on your own

# Write a properly documented python function that can perform the taks of a simple calculator with the following behaviour:
# 
# 1. The desired mathematical operation (plus, minus, divide, multiply)
# 
# 1. Two numbers shall be passed by user input
# 
# 1. The result shall be calculated and printed
# 
# 1. If the input for mathematical operation is not covered by the list from above, print "Please correct your input"
# 
# **You should use the following elements:** 
# 
# - If/elif/else statement
# - Functions
# - Mathematical experessions
# 
# 

# In[82]:


def simple_calc(first_num, ops, second_num):
    
    
    """
    Perform a mathematical operation between two numbers
    ...
    
    Arguments
    ---------
    first_num     : int/float
                    first number in calculation
                    
    ops           : str
                    mathematical operation; ops=[plus, minus, multiply, divide]
    
    second_num    : int/float
                    second number in calculation
    
    Returns
    -------
    seq   : str
            Operation and results of operation as string
    """
    
    
    user_input = "{} {} {} = ".format(first_num, ops, second_num)
    
    
    #### Your Code below
    
    # check numerical input
    
    
    
    
    
   

    # check selected operation is in [plus,minus,multiply,divide]
    
    
    
    
    
    
    
    #perform calculations
    

    

    
    
    
    # return user_input and result
    
    return print(user_input, result)
    


# In[83]:


simple_calc(6,"multiply",4)


# ---
