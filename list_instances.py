import oci
import csv

# Archivo de salida
output_file = "all_instances_python.csv"

# Lista de OCIDs de los compartimentos
compartments = [
    "ocid1.tenancy.oc1..aaaaaaaasrpsmmkckbezqehtoa6yvnaogopanqhg",
    "ocid1.compartment.oc1..aaaaaaaaez4wxdboq6liltzcyb7fxj4jqm5a",
    "ocid1.compartment.oc1..aaaaaaaaqgjxmbvi5fn7sezwlmjq3vk6c5uq",
    "ocid1.compartment.oc1..aaaaaaaattvrfcmtj56shvkzlvltjnee2qig",
    "ocid1.compartment.oc1..aaaaaaaapigsl4oufy7nqqh7zwhqut3z6dx3",
    "ocid1.compartment.oc1..aaaaaaaacxfx4axpitvyksuqkzuqz25odaas",
    "ocid1.compartment.oc1..aaaaaaaauenavtskypvl3z4kmvejb62vui42",
]

# Configuración de OCI
config = oci.config.from_file()

# Crear un cliente para interactuar con el servicio de Compute
compute_client = oci.core.ComputeClient(config)

# Escribir el archivo CSV sin el ID y con ; como delimitador
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Name", "State", "Region", "Shape", "Compartment"])

    for compartment_id in compartments:
        print(f"Procesando compartimento: {compartment_id}")
        instances = compute_client.list_instances(compartment_id).data
        
        for instance in instances:
            writer.writerow([
                instance.display_name,
                instance.lifecycle_state,
                instance.region,
                instance.shape,
                compartment_id
            ])

print(f"Listo. Los detalles de todas las instancias se han guardado en {output_file}")
