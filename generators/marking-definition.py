import uuid
import stix2
import os
import shutil
import json

from stix2 import Bundle
from stix2.base import STIXJSONEncoder
from stix2 import MarkingDefinition
from stix2 import FileSystemStore
from uuid import UUID

# create the directories

tmp_directories = [
    "tmp_object_store/marking-definition/cpe2stix",
    "tmp_object_store/marking-definition/arango_cti_processor",
    "tmp_object_store/marking-definition/cve2stix",
    "tmp_object_store/marking-definition/cwe2stix",
    "tmp_object_store/marking-definition/disarm2stix",
    "tmp_object_store/marking-definition/txt2stix",
    "tmp_object_store/marking-definition/sigma2stix",
    "tmp_object_store/marking-definition/stix4signalscorps",
    "tmp_object_store/marking-definition/stix2arango",
    "tmp_object_store/marking-definition/txt2stix"
]

for directory in tmp_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# define UUID for generating UUIDv5s

namespace=UUID("8eba93d6-1673-4e93-84a9-87f2d11ee72a")

# define values that are recycled between objects

### signalscorps
created_by_ref="identity--" + str(uuid.uuid5(namespace, f"signalscorps"))
created="2020-01-01T00:00:00.000Z"
definition_type="statement"
### mitre TLP:WHITE and stix4signalscorps
object_marking_refs=[
    "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9", 
    "marking-definition--" + str(uuid.uuid5(namespace, f"stix4signalscorps"))
]

# Create Marking Definition SMOs
## https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.common.html

### cpe2stix

#### marking-definition--de23ef3b-83bf-56a9-95c3-46bc1703966c

cpe2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"cpe2stix")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/cpe2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### arango_cti_processor

#### marking-definition--af79980e-cce7-5a67-becb-82ad5a68e850

arango_cti_processor_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"arango_cti_processor")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/arango_cti_processor"
                        },
                        object_marking_refs=object_marking_refs
                    )

### cve2stix

#### marking-definition--162e1800-92bd-573c-abbd-f359594ffad9

cve2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"cve2stix")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/cve2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### cwe2stix

#### marking-definition--762246cb-c8a1-53a7-94b3-eafe3ed511c9

cwe2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"cwe2stix")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/cwe2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### disarm2stix

#### marking-definition--e9988722-c396-5a91-a08d-db742bd3624b

disarm2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"disarm2stix")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/disarm2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### sigma2stix

#### marking-definition--efccc0ba-d237-5c9a-ad41-4f8bb6791be4

sigma2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"sigma2stix")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/sigma2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

### stix4signalscorps

#### marking-definition--3f588e96-e413-57b5-b735-f0ec6c3a8771

stix4signalscorps_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"stix4signalscorps")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/stix4signalscorps"
                        },
                        object_marking_refs=[
                            "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9"
                        ]
                    )

### stix2arango

#### marking-definition--c54d8eea-d241-5a83-8bf1-619f215ce10b

stix2arango_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"stix2arango")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/stix2arango"
                        },
                        object_marking_refs=object_marking_refs
                    )

### txt2stix

#### marking-definition--9c259ff7-f413-5001-9911-70b4352af93f

txt2stix_MarkingDefinitionSMO = MarkingDefinition(
                        id="marking-definition--" + str(uuid.uuid5(namespace, f"txt2stix")),
                        created_by_ref=created_by_ref,
                        created=created,
                        definition_type=definition_type,
                        definition= {
                            "statement": "This object was created using: https://github.com/signalscorps/txt2stix"
                        },
                        object_marking_refs=object_marking_refs
                    )

object_list = cpe2stix_MarkingDefinitionSMO, arango_cti_processor_MarkingDefinitionSMO, cve2stix_MarkingDefinitionSMO, cwe2stix_MarkingDefinitionSMO, disarm2stix_MarkingDefinitionSMO, sigma2stix_MarkingDefinitionSMO, stix4signalscorps_MarkingDefinitionSMO, stix2arango_MarkingDefinitionSMO, txt2stix_MarkingDefinitionSMO

BundleofAllObjects = Bundle(
                        id="bundle--" + str(uuid.uuid5(namespace, f"marking-definition-bundle")),
                        objects=object_list,
                        allow_custom=True
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store/marking-definition/cpe2stix": cpe2stix_MarkingDefinitionSMO,
    "tmp_object_store/marking-definition/arango_cti_processor": arango_cti_processor_MarkingDefinitionSMO,
    "tmp_object_store/marking-definition/cve2stix": cve2stix_MarkingDefinitionSMO,
    "tmp_object_store/marking-definition/cwe2stix": cwe2stix_MarkingDefinitionSMO,
    "tmp_object_store/marking-definition/disarm2stix": disarm2stix_MarkingDefinitionSMO,
    "tmp_object_store/marking-definition/sigma2stix": sigma2stix_MarkingDefinitionSMO,
    "tmp_object_store/marking-definition/stix2arango": stix2arango_MarkingDefinitionSMO,
    "tmp_object_store/marking-definition/stix4signalscorps": stix4signalscorps_MarkingDefinitionSMO,
    "tmp_object_store/marking-definition/txt2stix": txt2stix_MarkingDefinitionSMO
}

for directory, markingdefinition_smo in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([markingdefinition_smo])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/marking-definition"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

base_input_path = "tmp_object_store/marking-definition/"
base_output_path = "objects/marking-definition/"

file_names = [
    "cpe2stix/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"cpe2stix")) + ".json",
    "arango_cti_processor/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"arango_cti_processor")) + ".json",
    "cve2stix/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"cve2stix")) + ".json",
    "cwe2stix/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"cwe2stix")) + ".json",
    "disarm2stix/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"disarm2stix")) + ".json",
    "sigma2stix/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"sigma2stix")) + ".json",
    "stix4signalscorps/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"stix4signalscorps")) + ".json",
    "stix2arango/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"stix2arango")) + ".json",
    "txt2stix/marking-definition/marking-definition--" + str(uuid.uuid5(namespace, f"txt2stix")) + ".json"
]

for file_name in file_names:
    source_path = os.path.join(base_input_path, file_name)
    destination_path = os.path.join(base_output_path, file_name.split('/')[-1])
    shutil.move(source_path, destination_path)

shutil.rmtree("tmp_object_store")

## Print the bundle

print(BundleofAllObjects.serialize(pretty=True))