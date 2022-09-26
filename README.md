# Elastic-Kibana-Gui-ext

With this extensions you can use Elastic and Kibana inside Loko ;)

## Important!

This proejct will mount elasticsearch volume inside this path.

```bash
/var/opt/loko/volumes/elastic-kibana-gui-ext/elasticsearch/data
```
Before starting it the first time, run this command in your terminal:

```bash
sudo mkdir -p /var/opt/loko/volumes/elastic-kibana-gui-ext/elasticsearch/data && sudo chmod 777 /var/opt/loko/volumes/elastic-kibana-gui-ext/elasticsearch/data
```
###### *If you want, you can change the mount path editing Line #6 in the file config.json using this structure:  "/your/new/path:/usr/share/elasticsearch/data"*
###### *Of course, remember to give the commands above with the new path!!*  

## First connection elastic-kibana
In the project you will find a simple flow. Run it and follow the instruction in the console.