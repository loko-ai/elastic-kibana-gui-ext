# Elastic-Kibana-Gui-ext

With this extensions you can use Elastic and Kibana inside Loko ;)

## Important!

This project will mount elasticsearch volume inside this path:
```bash
/var/opt/loko/elastic-kibana-gui-ext/elasticsearch/data
```
Before starting it the first time, run this command in your terminal:

```bash
sudo mkdir -p /var/opt/loko/elastic-kibana-gui-ext/elasticsearch/data && sudo chmod 777 /var/opt/loko/elastic-kibana-gui-ext/elasticsearch/data
```

## First connection elastic-kibana
In the project you will find a simple flow. Run it and follow the instruction in the console.