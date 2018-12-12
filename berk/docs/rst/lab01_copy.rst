
Name: Email:

Class 1 Introductory Lab
========================

Welcome!

Before we get started, there are some administrative details.

Labs are required. Here is how you get credit. Get credit by submitting
a pdf version of the notebook.

Collaborating on labs is more than okay -- it's encouraged! You should
rarely be stuck for more than a few minutes on questions in labs, so ask
a neighbor or an instructor for help. (Explaining things is beneficial,
too -- the best way to solidify your knowledge of a subject is to
explain it.) Please don't just share answers, though.

Today's lab
^^^^^^^^^^^

In today's lab, you'll learn how to:

1. navigate Jupyter notebooks (like this one);
2. write and evaluate some basic *expressions* in Python, the computer
   language of the course;
3. call *functions* to use code other people have written; and
4. break down Python code into smaller parts to understand it.

This lab covers parts of `Chapter
3 <http://www.inferentialthinking.com/chapters/03/programming-in-python.html>`__
of the online textbook. This is usefule but not required.

.. code:: ipython3

    # Don't change this cell; just run it. 
    # The result will give you directions about how to log in to the submission system, called OK.
    # Once you're logged in, you can run this cell again, but it won't ask you who you are because
    # it remembers you. However, you will need to log in once per assignment.
    from client.api.notebook import Notebook
    ok = Notebook('lab01.ok')
    _ = ok.auth(inline=True)

.. code:: ipython3

    # Change the next line so that it computes the number of
    # seconds in a decade and assigns that number the name
    # seconds_in_a_decade.
    seconds_in_a_decade = 10 * 365 * 24 * 60 * 60;
    
    # We've put this line in this cell so that it will print
    # the value you've given to seconds_in_a_decade when you
    # run it.  You don't need to change this.
    seconds_in_a_decade




.. parsed-literal::

    315360000



.. code:: ipython3

    # Test cell; please do not change!
    _ = ok.grade('q32')


::


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-10-53329f5ad7f7> in <module>()
          1 # Test cell; please do not change!
    ----> 2 _ = ok.grade('q32')
    

    ~\Anaconda3\lib\site-packages\client\api\notebook.py in grade(self, question, global_env)
         56             # inspect trick to pass in its parents' global env.
         57             global_env = inspect.currentframe().f_back.f_globals
    ---> 58         result = check(path, global_env)
         59         # We display the output if we're in IPython.
         60         # This keeps backwards compatibility with okpy's grade method


    ~\Anaconda3\lib\site-packages\gofer\ok.py in check(test_file_path, global_env)
        285         # inspect trick to pass in its parents' global env.
        286         global_env = inspect.currentframe().f_back.f_globals
    --> 287     return tests.run(global_env, include_grade=False)
    

    ~\Anaconda3\lib\site-packages\gofer\ok.py in run(self, global_environment, include_grade)
        142         failed_tests = []
        143         for t in self.tests:
    --> 144             passed, hint = t.run(global_environment)
        145             if passed:
        146                 passed_tests.append(t)


    ~\Anaconda3\lib\site-packages\gofer\ok.py in run(self, global_environment)
         84     def run(self, global_environment):
         85         for i, t in enumerate(self.tests):
    ---> 86             passed, result = run_doctest(self.name + ' ' + str(i), t, global_environment)
         87             if not passed:
         88                 return False, OKTest.result_fail_template.render(


    ~\Anaconda3\lib\site-packages\gofer\ok.py in run_doctest(name, doctest_string, global_environment)
         43     with redirect_stdout(runresults), redirect_stderr(runresults), hide_outputs():
         44         doctestrunner.run(test, clear_globs=False)
    ---> 45     with open('/dev/null', 'w') as f, redirect_stderr(f), redirect_stdout(f):
         46         result = doctestrunner.summarize(verbose=True)
         47     # An individual test can only pass or fail


    FileNotFoundError: [Errno 2] No such file or directory: '/dev/null'


