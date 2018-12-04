
### Carme
This uses carme to manage environments. 
```
wget https://raw.githubusercontent.com/CarmeLabs/carme/master/scripts/get/get_carme_dev.sh
source get_carme_dev.sh
```

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
To enter the Carme environment, find the path to "carme-env" in whichever directory that you installed it in and activate the environment through this script
```
source ....../carme-env/bin/activate
```