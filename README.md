### Installing Carme on Linux
The following script will install Carme:
```
wget https://raw.githubusercontent.com/CarmeLabs/carme/master/scripts/get/get_carme_conda.sh
source get_carme_conda.sh
```
In the case that you have not installed Pandoc, which Carme utilizes (and will give you an error if you do not have it installed), you can get Pandoc through this script
```
sudo apt-get install pandoc
```
In the case that you have not installed PyHamcrest, which Carme utilizes (and will give you an error if you do not have it installed), you can get PyHamcrest through this script
```
pip install pyhamcrest
```
### Finding the environment
To enter the Carme environment, find the path to "carme-env" in whichever directory that you installed it in and activate the environment through this script
```
source .../carme-env/bin/activate
```

### Setting up environment alias for easier access to the Carme environment
Finding the environment and activating it every time might be tedious, so we can set up an alias so that you can activate the environment with a single command. Follow the following steps:

(1) Find the path to the "activate" file in the Carme environment directory.
Usually, the path looks something like
```
.../carme-env/bin/activate
```
(2) Record that path, and now find your .bashrc file, which is the file that your bash/shell reads everytime it activates.
Usually, the .bashrc file is found the "~" directory, which is the base directory
```
cd ~
```
You can only view the .bashrc file if you view all of the hidden files in the "~" directory as well
```
ls -a
```
(3) Now open the file through an editor (possibly Vim) and add a line at the bottom in the following format with corresponding pathing to your activate file in the carme environment directory
```
alias carme-env='source .../carme-env/bin/activate'
```

Now you just need call the alias "carme-env" command on the terminal and you will activate the Carme environment. If you want to deactivate the environment, you just need to deactivate it with the following command
```
deactivate
```

