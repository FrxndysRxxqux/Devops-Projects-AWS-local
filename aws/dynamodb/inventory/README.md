# Dynamo Inventory  :+1:
 Script de python para automatizar el proceso de inventario de las tablas de dynamoDB

 ## **Pasos**
 
  ### **1- Instalacion del AWS CLI** 
   Se sigue el paso a paso de la [documentacion oficial](https://docs.aws.amazon.com/es_es/cli/latest/userguide/getting-started-install.html)
    
  ### **2- Configuracion del AWS CLI**
   Para realizar la configuracion primero se necesita tener 
      a) Access key ID
      b) Secret access key
      
    Se ejecuta el siguiente comando en la terminal que deseee
      -> ~  aws configure
     
    En caso de que se desee configurar un perfil externo 
      -> ~ aws configure --profile #profile_name

   ### **3- Ejecucion del script**
    En la terminal que use se ejecuta el archivo .py
      -> ~ python dynamo_inventory.py

   ### **4- Revision de archivo .csv**
   Para finalizar debes revisar que se genero correctamente el archivo .csv con la informacion de las tablas, y deberia tener la siguiente estructura
   ![image](https://github.com/AgnerVillaFabrega/DynamoInventory/assets/57839642/81f7adb9-dfa8-4f62-8531-09577a89b6fc)
   ![image](https://github.com/AgnerVillaFabrega/DynamoInventory/assets/57839642/087ea270-dc10-4f55-88eb-5c8101dec761)