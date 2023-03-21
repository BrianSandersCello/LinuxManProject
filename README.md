# LinuxManProject
This code requires the ntlk and scikit-learn python packages to work properly.

This is my attempt to create a simplified linux manual that is easily searchable using an alias (I opted to use the term "search") from the linux command line. 
It uses two databases, commands.txt and commands2.txt
If you search for a command by name and it exists in the database, it should just return one search option, unless there is a very closely related command.
However, you can also send it a question (although without a question mark, as this is a command you can search in the database).
"How can I make a file", or "How can I delete a file", return correct responses, at least somewhere in the 3 search options.
I have made the database more precise by including various terms people might use in the command descriptions, such a "display or show," "create or make".
While the search algorithm isn't perfect, I am mostly getting accurate information.
I have also modified the script using a regex (and the "re" python package) to recognize special characters, like "*|?[]" and such. 
I felt it would be helpful to have descriptions of these functions in the manual. I'm not sold on including ? however,
because if anyone phrases their query as a question, then the "?" manual entry pops up.
I think this is a good, if not yet exhaustive start on creating a stripped down, more readily searchable linux manual for beginners, as the man pages can be quite dense.
I hope you find this little program useful.
