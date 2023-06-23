# LinuxManProject
This code requires the ntlk and scikit-learn python packages to work properly.

This is my attempt to create a simplified linux manual that is easily searchable from the CLI. I decided to opt for two scripts, one for advanced user and one for beginners. The advanced command is 'search', the beginner one is 'manual'.
It uses two different scripts and 3 data files, commands.txt, commands2.txt, and commands.json.

The 'manual' script:
This script uses a json file to break down commands by type with a short description of each command. Once a specific command is searched for, it sends the user the entry for that command from the 'commands.txt' file. I believe that this script would be very useful for anyone trying to instruct beginners in Linux. The json file can be modified quite easily to group commands in any way the instructor desires. The commands.txt file can easily be modified to include specific notes on the various commands, or different sets of flags. I see this script essentially as a highly customizable teaching tool.

The 'search' script:
If you search for a command by name and it exists in the database, it should just return one search option, unless there is a very closely related command - this part of the script references the 'commands2.txt' file, which includes only the command names.
However, you can also send it a question (although without a question mark, as this is a command you can search in the database), such as "How can I make a file", or "How can I delete a file". Other queries can return more obscure options - simply typing in the query "encryption" will lead one to the crypt-setup entry. 
I have made the database more precise by including various terms people might use in the command descriptions, such a "display or show," "create or make". I specifically tried using some synonym analyzer python packages, but these proved far too cumbersome as they are large files.
While the search algorithm isn't perfect, I am mostly getting accurate information.
I have also modified the script using a regex (and the "re" python package) to recognize special characters, like "*|?[]" and such. 
I felt it would be helpful to have descriptions of these functions in the manual. I'm not sold on including ? however,
because if anyone phrases their query as a question with the '?', then the '?' manual entry pops up.
I think this is a good, if not yet exhaustive start on creating a stripped down, more readily searchable linux manual for beginners and sys admins alike.
I hope you find this little program useful.

So what's the motivation here? We have google, we have chatgpt. Why make this? I believe strongly in applied learning, and I've found that the more time a user can spend in the command line without having to go out to google can be very useful. Simply being able to query your own command line about how to do various tasks can be very iinstructive, especially since I configured the search script to return three responses, which can yield some very interesting search results. Plus, it's cool. 
