# NetLogo pathdir Extension
Version 3.1 - May 2019 (for NetLogo v6.1, 6.2 & 6.3)

* [Quickstart](#quickstart)
* [What is it?](#what-is-it)
* [Installation](#installation)
* [Examples](#examples)
* [Primitives](#primitives)
* [Depreciated primitives](#depreciated-primitives)
* [Building](#building)
* [Author](#author)
* [Feedback](#feedback-bugs-feature-requests)
* [Credits](#credits)
* [Terms of use](#terms-of-use)

## Quickstart

[Install the pathdir extension](#installation)

Include the extension in your NetLogo model (at the top):

    extensions [pathdir]

[back to top](#netlogo-pathdir-extension)

## What is it?

This package contains the NetLogo **pathdir extension**, which provides NetLogo with some file-related primitives not included in the standard language, particularly primitives related to manipulating directories, identifying the current NetLogo model, moving files, and finding the size and modification dates of files.

[back to top](#netlogo-pathdir-extension)

## Installation

First, [download the latest version of the extension](https://github.com/cstaelin/Pathdir-Extension/releases). Note that this version (v3.1.0) of this extension was compiled for NetLogo 6.1, 6.2 and 6.3, and will not work with earlier versions of NetLogo. If you are using v5.x of NetLogo you should download and install v2.0 of this extension.

Unzip the archive, rename the extracted directory to **pathdir**, and move the **pathdir** directory to the **extensions** directory inside your NetLogo application folder. The NetLogo application will normally be in the Applications folder on the Mac, or under C:\Program Files on Windows, and the **extensions** directory is in the **app** subdirectory of the NetLogo application.  Or you can place the pathdir directory in the same directory holding the NetLogo model in which you want to use this extension.

For more information on NetLogo extensions:
[http://ccl.northwestern.edu/netlogo/docs/extensions.html](http://ccl.northwestern.edu/netlogo/docs/extensions.html)

[back to top](#netlogo-pathdir-extension)

## Examples

See the **PathDir.nlogo** model for examples of usage.


[back to top](#netlogo-pathdir-extension)

## Primitives

**pathdir:get-separator**

*pathdir:get-separator*

Returns a string with the character used by the host operating system to separate directories in the path.  E.g., for Windows the string "\\\" would be returned (as the backslash must be escaped), while for Mac OSX and linux, the string "/" would be returned.  Useful for creating operating system-independent path strings.

---------------------------------------

**pathdir:get-model-path**

*pathdir:get-model-path*

Returns a string with the full (absolute) path to the directory in which the current model is located.

NOTE: Returns an empty string ("") if the current model has not yet been saved to a file.

---------------------------------------

**pathdir:get-model-file**

*pathdir:get-model-file*

Returns a string with the filename of the .nologo or .nlogo3d file containing the current model. 

NOTE: Returns an empty string ("") if the current model has not yet been saved to a file.

Stripping the .nlogo extension  (or any extension) is easily done:

    let modelName pathdir:get-model-name
    let shortName substring modelName 0 (length modelName - position "." reverse modelName - 1)

The model filename can also be concatenated with the path to it:

    let fullModelPath (word pathdir:get-model pathdir:get-separator pathdir:get-model-name)

---------------------------------------
**pathdir:get-model-name**

*pathdir:get-model-name*

Returns a string with the name of the current model. NetLogo sets the name of the model to the filename of the .nologo or .nlogo3d file containing the model, stripped of the file extension.

NOTE: Returns an empty string ("") if the current model has not yet been saved to a file, although NetLogo calls an unsaved model "Untitled".

---------------------------------------

**pathdir:get-home-path**

*pathdir:get-home-path*

Returns a string with the full (absolute) path to the user's home directory, as specified by the "user.home" environment variable of the host operating system.  This may not exist for all operating systems?

---------------------------------------

**pathdir:get-CWD-path**

*pathdir:get-CWD-path*

Returns a string with the full (absolute) path to the current working directory (CWD) as specified in the NetLogo context for the current model.  The CWD may be set by the NetLogo command set-current-directory.  Note that set-current-directory will accept a path to a directory that does not actually exist and subsequently using the nonexistent CWD, say to open a file, will normally cause an error.  Note too that when a NetLogo model first opens, the CWD is set to the directory from which the model is opened.

---------------------------------------

**pathdir:create**

*pathdir:create directory-string*

Creates the directory specified in the given string.  If the string does not contain an absolute path, i.e. the path does not begin at the root of the file system, then the directory is created relative to the current working directory.  Note that this procedure will create as many intermediate directories as are needed to create the last directory in the path.  So, if one specifies 

    pathdir:create "dir1\\dir2\\dir3" 

(using Windows path syntax) and if dir1 does not exist in the CWD, then the procedure will create dir1 in the CWD, dir2 in dir1, and finally dir3 in dir2.  If the directory to be created already exists, then no action is taken.

---------------------------------------

**pathdir:isDirectory?**

*pathdir:isDirectory? directory-string*

Returns TRUE if the file or directory given by the string both exists **and** is a directory.  Otherwise, returns FALSE.  (Note that the NetLogo command file-exists? can be used to see if a file or directory simply exists, but does not distinguish between files and directories.)  If the path given by the string is not an absolute path, i.e., it does not begin at the root of the file system, then the path is assumed to be relative to the current working directory.

---------------------------------------

**pathdir:list**

*pathdir:list directory-string*

Returns a NetLogo list of strings, each element of which contains an element of the directory listing of the specified directory.  If the path given by the string is not an absolute path, i.e., it does not begin at the root of the file system, then the path is assumed to be relative to the current working directory.  If the directory is empty, the command returns an empty list.  To get a listing of the CWD one could use 

    pathdir:list pathdir:get-CWD-path 

or, more simply, 

    pathdir:list "".

---------------------------------------

**pathdir:move**

*pathdir:move string1 string2*

Moves or simply renames the file or directory given by string1 to string2.  If either string does not contain an absolute path, i.e., the path does not begin at the root of the file system, then the path is assumed to be relative to the current working directory.  E.g.,

    let sep pathdir:get-separator    
    pathdir:move (word "dir1" sep "file1.csv") (word pathdir:get-home sep "keep.csv")

will rename and move the file "file1.csv" in dir1 of the CWD to "keep.csv" in the user's home directory.  If a file with the same name already exists at the destination, an error is returned.

---------------------------------------

**pathdir:delete**

*pathdir:delete directory-string*

Deletes the directory given by the string.  The directory must be empty and must not be hidden.  (**The check for a read-only directory currently does not work. Be careful!**)  If the path given by the string is not an absolute path, i.e., it does not begin at the root of the file system, then the path is assumed to be relative to the current working directory.  This command will return an error if the path refers to a file rather than a directory as there already is a NetLogo command for deleting a file: file-delete. Use pathdir:isDirectory? if there is any doubt. 

--------------------------------------

**pathdir:get-size**

*pathdir:get-size file-string*

Returns the size in bytes of the file given by the string. If the path given by the string is not an absolute path, i.e., it does not begin at the root of the file system, then the path is assumed to be relative to the current working directory.

--------------------------------------

**pathdir:get-date**

*pathdir:get-date file-string*

Returns the modification date of the file given by the string. The date is returned as a string in the form dd-MM-yyyy HH-mm-ss, where dd is the day in the month, MM the month in the year, yyyy the year, HH the hour in 24-hour time, mm the minute in the hour and ss the second in the minute. If the path given by the string is not an absolute path, i.e., it does not begin at the root of the file system, then the path is assumed to be relative to the current working directory.

--------------------------------------

**pathdir:get-date-ms**

*pathdir:get-date-ms file-string*

Returns the modification date of the file given by the string. The date is returned as the number of milliseconds since the base date of the operating system, making it easy to compare dates down to the millisecond. This time format is useful for comparing the modification dates of two files. If the path given by the string is not an absolute path, i.e., it does not begin at the root of the file system, then the path is assumed to be relative to the current working directory.

---------------------------------------

[back to top](#netlogo-pathdir-extension)

## Depreciated primitives

In Version 1 of this extension, the `get-model-path`, `get-home-path` and `get-CWD-path` primitives were named `get-model`, `get-home` and `get-current`, respectively. The old names are no longer recognized. 

---------------------------------------

[back to top](#netlogo-pathdir-extension)

## Building

The Makefile uses the NETLOGO environment variable to find the NetLogo installation. However, if NETLOGO has not been defined, the Makefile assumes that it is being run from the **app/extensions/pathdir** directory under the directory in which NetLogo has been installed. If compilation succeeds, `pathdir.jar` and `pathdir.jar.pack.gz` will be created.  See [Installation](#installation) for instructions on where to put the new `pathdir.jar` and `pathdir.jar.pack.gz` if they are not already there.

## Author

Charles Staelin<br>
Smith College<br>
Northampton, MA 01063

## Feedback? Bugs? Feature Requests?

Please visit the [github issue tracker](https://github.com/cstaelin/Pathdir-Extension/issues?state=open) to submit comments, bug reports, or feature requests.  I'm also more than willing to accept pull requests.

## Credits

Many thanks to the NetLogo developers and the NetLogo user community for answering my questions and suggesting  additional features.

## Terms of Use

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

The NetLogo pathdir extension is in the public domain.  To the extent possible under law, Charles Staelin has waived all copyright and related or neighboring rights.

[back to top](#netlogo-pathdir-extension)
