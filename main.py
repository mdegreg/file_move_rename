"""
Definitions:
A Python module is a Python file ending in .py, which is imported into another script to be used there.
These are used to bring in functions, classes, etc. that are in the module. This allows for organizing of classes
and functions into files, and then used in your main script. Note that if you do this, the imported file must be
findable by your Python environment, i.e. in this case they are contained within the project folder.
Note: there isn't a functional difference between a module and a script--the only difference is intention. A module
is a script imported so you can use the stuff inside of it.

A Python package is a particular way of creating a folder structure that contains Python modules (or sub-folders
that contain Python modules), set up in such a way that it can be treated somewhat like a Python package. A large
set of classes and functions can be organized into multiple modules, sorted into different parts of a package.

An attribute is a characteristic that a Python object has. Things like height, ID, weight, hair color, etc.

A method is a thing that a Python object can do. Things like rowing a boat, adding things together, barking, whatever.

An instance is an object created from a particular class. Dog is a class, and a particular dog named
'Fido' is an instance of the Dog class.

Classes are the templates for an object. To go back to the Dog example, every Dog may have a class attribute 'species'
that has the value 'Canis familiaris'. Every dog can refer to this class attribute as its own. Every dog can also
bark(), wag_tail(), bite(), eat(), drink(), and move(). Since every dog can do this, these are made into methods for
the class.

Now, dogs aren't all the same. We may also want to give instance attributes, where a dog has its own name, age, breed,
height, and weight. These aren't the same for every dog, so we have to tell Python what those values are when we make
the instance of a Dog.

Example of an implementation of this sort of thing can be found in dog.py, with some more notes on classes vs.
instances.

----
When importing specific functions from packages into the environment directly, e.g.
> from <module> import <function>
would recommend using format:
> from <module> import <function1>, <function2>, <functino3>, etc.

In cases where you are importing a module within a package, you can give it a shortened name to use in your script
like so:
> import <package_name>.<sub_package_name>.<module_name> as short_name
And then, when you want to, say, call a function in the particular module that was imported, you can do it like this:
> short_name.do_stuff(foo, bar, spam)

You may also see import statements that look like:
> from <module> import *
What this does, is it imports everything that's inside the module into the main script, so instead of using a function
like:
> module.foo()
you can instead just do foo() and get the function that way, even though it's defined in a different module.

This is not really a very good way of doing things. Usually it's okay, but...
Imagine that you have a function named foo(). Now, the module you're trying to import also contains a function
called foo(). When you import the module, the foo() you have in the MAIN script will be overwritten by the foo()
in the MODULE script. This can lead to confusion and weird behavior, since the two functions may do completely
different things.

Note: I'm putting comments immediately before the line that they're relevant to. You might want to do it differently.
Doesn't really matter, mostly a personal preference thing. Good to be consistent though, whatever you choose.
"""

import os
import datetime

import logging
# This is a local file that is imported into the main script.
import logger_initializer

"""
You can use triple quotes (either single quote ' or double quote ") to make multi-line strings. If you don't assign
these strings to anything, but just have them floating like this, then you can also use them as multi-line comments.

Configuration variables such as these should be in all caps, to distinguish them from variables that are used and
edited by the script as it runs.

Generally, static filepaths, non-changing numbers like the number of days in a week, etc. should be constants.

These variables are not officially constant and unchangeable--it's just a signal to any other people who use
this script that these aren't meant to be changed while the script runs.

Note: filepaths are a pain in the ass. When I'm writing filepaths by hand, I use forward slashes because
it's a little shorter than double backslashes (which you need if you're using backslashes in the Windows filepath, as
it does by default). To join paths safely, use os.path.join() instead of messing with it yourself.

When you have a \<letter> type of thing in a string, like '\n', that's interpreted as something specific by the
computer. These are what we're talking about when we're talking about special characters. The example I have here
is a newline.

Example: Compare 'a\nb' and 'a\\nb'.
In the first one, the computer will print:
a
b
^ Notice the newline! :D

In the second one, the computer will print:
a\nb

Normally, \ symbolizes the start of a special character, but when we use it before another \, it means that
the computer should treat the special character '\' like a regular character.
"""


class ScriptConstants:
    """
    This is how you make a class in Python. Normally, classes are made to be used as a sort of template for objects.

    But, in this case, I'm using it to wrap up the constants used when running this file as a script. By doing it this
    way, I can avoid having these variables overwrite same-named variables that are in the script that imports this
    file.
    """
    SOURCE_FILEPATH = 'C:/Users/curio/Desktop/test_source_folder'

    # Location where files/folders should be placed--this is where we want files to go. We may want to make a folder
    # inside of this, and then put the files THERE instead. Either way works.
    TARGET_FILEPATH = 'C:/Users/curio/Desktop/test_target_folder'
    WINDOWS_DEFAULT_FILE_PATH_SEPARATOR = '\\'
    NORMAL_PERSON_FILE_PATH_SEPARATOR = '/'
    FILE_EXTENSION_SEPARATOR = '.'  # Not its only use, but oh well. Let's be explicit here.
    NUM_FILE_EXTENSIONS_IN_FILE_NAME = 1  # I mean, there may be more, but we really only care about one.


class FilePair:
    """
    One thing you can do with classes is create a template for objects to keep things organized.

    For example, in the script, I could just have a list of paths for the old files, and the paths for where I
    want those files to go. But I'm concerned that these lists could end up mismatched for some reason. So I use
    objects created from this class to make sure that the right file paths are kept paired together.
    """
    # This is a class variable. Note the difference between the assignment here, and the assignments below in the
    # __init__() method. EVERY FilePair object that I create will be able to see this attribute, and treat it as though
    # it were it's own. BUT, if I change this attribute, then every single FilePair object will now have the new value.
    # Every instance of the class will reflect the change, hence class variable vs. instance variable.
    _my_class_variable = "Hi! I am a class variable!"

    def __init__(self, old_file_path, new_file_path):
        """
        An __init__() method is a special Python-defined method that's used when you create an object using a
        particular class. This is the method that gets run when you make the object--you can assign initial values
        to the object's attributes here, and make sure that the user has given all the values that the object needs.
        """
        self.old_file_path = old_file_path
        self.new_file_path = new_file_path

    def say_hello(self):
        print(self._my_class_variable)


def get_path_contents(folder_path):
    """
    Get the entire contents of a path. Returns both files and folders at this path, and does not return
    filenames contained within sub-folders at this path.

    :param folder_path: a string containing a valid path to a computer directory
    :return: a list containing names of files and folders in the provided folder path
    """
    logging.info("Retrieving contents of path {}".format(folder_path))  # Look up formatting strings--very handy.
    folder_contents = os.listdir(folder_path)
    # The return keyword always forces the function to quit running the function, and it will
    # send the contents of the variable (or variables--we'll get to that later) that's named after it
    # as the returned value of the function.
    num_items_in_folder = len(folder_contents)
    logging.info("Contents retrieved. {} items found.".format(num_items_in_folder))
    return folder_contents


def get_files(folder_path):
    """
    Get the names for files (but not folders) contained at this location.

    :param folder_path: a string containing a valid path to a computer directory
    :return: a list of file names contained within the folder_path directory
    """
    logging.info('Getting absolute file paths from path {}'.format(folder_path))
    temp_contents = get_path_contents(folder_path)
    final_contents = list()  # Make a new empty list that we can fill with stuff we're interested in

    # If you want to make this more compact, you can try to turn this into a list comprehension. Look it up in the
    # Python docs--it's a pretty handy way to compactly create lists of things from lists of other things.
    for name in temp_contents:
        # Couple of things here.
        # First, when you add strings together, Python interprets that as string concatenation.
        # Second, keep track of whether or not you have a "/" at the end of your folder paths. Convention in
        # this script is to not have the "/" at the end of a folder path, and to add it when the path gets something
        # attached to the end of it. Again, big thing is to be consistent so it's easy to remember what you gotta do.
        full_file_path = os.path.join(folder_path, name)  # Just how this function is supposed to be called--
                                                            # root path string, then list of the other bits.
        if os.path.isfile(full_file_path):
            final_contents.append(name)
        else:
            # This isn't necessary. The 'pass' keyword is a placeholder keyword to say that the computer shouldn't
            # do anything. I want to be explicit about not doing anything, but you could just leave the else clause
            # out (or delete it) and it shouldn't affect anything.
            pass
    num_files = len(final_contents)
    logging.info('Returning files. {} files found.'.format(num_files))
    return final_contents


def move_file(file_path, target_path):
    """
    Generally, if you have 'and' in a function, it's a sign that the contents should be broken down into two
    functions--functions should be as simple as possible. But since the logic to do both is fairly simple, I've
    decided not to worry about that here.

    Spoiler: it's because I'm a terrible person.

    :param file_path: a string containing the complete path to a file.
    :param target_path: a string containing the absolute path to the location (with the new name) where the file should
    be stored.
    :return: None
    """
    logging.info('Moving {} to {}...'.format(file_path, target_path))
    target_path = target_path
    os.rename(file_path, target_path)
    logging.info('Move successful.')


def transform_file_name(original_file_name):
    """
    Now, this is just whatever I felt like. Whee.

    So in this function I could have just used 0 and 1 as my indices directly when I look at the different parts of
    the file name, but it's generally better to name these sorts of things, so people know *why* they're 0 and 1.
    Another benefit is that you now know exactly why these particular things are 0 and 1 without having to guess,
    and you know that these usages of 0 or 1 are different for other usages. For example, I have 2 usages of the
    value 1 in this function, but they serve different purposes.
    """
    # So script constants are in all caps. But when we're using constants inside a specific function or class or
    # something along those lines, then we do something a little different. These values are meant to be used
    # inside the function, but they're not meant to be used outside of it, returned, or anything like that. The leading
    # underscore is a signal to anyone else who uses this script to indicate that.
    _file_name_location = 0
    _file_type_ending_location = 1
    logging.info("Original file name: {}".format(original_file_name))
    # Split the original filename into parts once, based on the specified separator, exactly one time.
    # Also, do this by searching for the separator starting from the right-hand side of the string.
    file_name_parts = original_file_name.rsplit(
        # I don't want this line to be too long, so I've added line breaks here to keep things from getting too wide.
        ScriptConstants.FILE_EXTENSION_SEPARATOR,
        ScriptConstants.NUM_FILE_EXTENSIONS_IN_FILE_NAME
    )
    file_ending = file_name_parts[_file_type_ending_location]
    file_name = file_name_parts[_file_name_location]
    # I forget whether I mentioned this before, but when you add strings together, Python interprets it as
    # an instruction to concatenate the strings together (with no separator).
    new_file_name = file_name + '_derp_i_moved_this_thing' + ScriptConstants.FILE_EXTENSION_SEPARATOR + file_ending
    logging.info('New file name: {}'.format(new_file_name))
    return new_file_name


def create_file_path_pair(file_name, source_path, target_path):
    logging.info('Creating file path pair for {}'.format(file_name))
    source_absolute_file_path = os.path.join(source_path, file_name)
    transformed_file_name = transform_file_name(file_name)
    target_absolute_file_path = os.path.join(target_path, transformed_file_name)
    file_path_pair = FilePair(source_absolute_file_path, target_absolute_file_path)
    logging.info('FilePair instance created.')
    return file_path_pair


def main():
    """
    It's generally a good idea to wrap up the actual execution of things you want to do in the script into a main()
    function. Doing this allows you to import this script as a module for another script you make later, without
    running the contents of the script. Imports work by running the entire contents of the script, so if you just have
    the code to do various things at the outermost code level, it will be run when this file is imported.

    This structure prevents that.
    """
    logger_initializer.initialize_logger()
    logging.info('Retrieving files...')
    files = get_files(ScriptConstants.SOURCE_FILEPATH)
    file_path_pairs = list()  # Prep our empty list so that we can add to it from our loop
    logging.info('Generating target filepaths...')
    for file in files:
        new_file_pair = create_file_path_pair(file, ScriptConstants.SOURCE_FILEPATH, ScriptConstants.TARGET_FILEPATH)
        file_path_pairs.append(new_file_pair)
    logging.info('Moving files...')
    for file_path_pair in file_path_pairs:
        move_file(file_path_pair.old_file_path, file_path_pair.new_file_path)
    logging.info('All tasks completed.')


if __name__ == '__main__':
    """
    The __name__ variable can indicate whether the file that's being run is the core of the script that you're running.

    If the file is the core script, then it receives the special name '__main__'. If it's being run as an import, then
    __name__ contains the name of the module itself. So, the if statement that I'm using here will ensure that the
    main() function is only run if this is intended to be run as a script.
    """
    main()

