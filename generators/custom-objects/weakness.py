import uuid
import stix2
import os
import shutil

from stix2 import CustomObject
from stix2.properties import (
    BooleanProperty, ExtensionsProperty, ReferenceProperty,
    IDProperty, IntegerProperty, ListProperty, StringProperty,
    TimestampProperty, TypeProperty,
)
from stix2.v21.common import (
    ExternalReference,
)
from stix2.utils import NOW

from uuid import UUID

_type = 'weakness'
@CustomObject('weakness', [
    ('type', TypeProperty(_type, spec_version='2.1')),
    ('spec_version', StringProperty(fixed='2.1')),
    ('id', IDProperty(_type, spec_version='2.1')),
    ('created_by_ref', ReferenceProperty(valid_types='identity', spec_version='2.1')),
    ('created', TimestampProperty(default=lambda: NOW, precision='millisecond', precision_constraint='min')),
    ('modified', TimestampProperty(default=lambda: NOW, precision='millisecond', precision_constraint='min')),
    ('name', StringProperty(required=True)),
    ('description', StringProperty()),
    ('labels', ListProperty(StringProperty)),
    ('external_references', ListProperty(ExternalReference)),
    ('object_marking_refs', ListProperty(ReferenceProperty(valid_types='marking-definition', spec_version='2.1'))),
    ('extensions', ExtensionsProperty(spec_version='2.1'))
])
class Weakness(object):
    def __init__(self, **kwargs):
        pass

# create the directories

tmp_directories = [
    "tmp_object_store",
]

for directory in tmp_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# define UUID for generating UUIDv5s

namespace=UUID("8eba93d6-1673-4e93-84a9-87f2d11ee72a")

# define values that are recycled between objects

### signalscorps demo
created_by_ref="identity--" + str(uuid.uuid5(namespace, f"signalscorps-demo"))
created="2020-01-01T00:00:00.000Z"
modified="2020-01-01T00:00:00.000Z"

# Create Weakness SDO object

### weakness--519a9c84-3c54-5698-bd9a-99bd01f003d1

example_WeaknessSDO = Weakness(
                        id="weakness--"+ str(uuid.uuid5(namespace, f"A demo weakness")),
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="CWE Demo",
                        description="A demo weakness",
                        labels=[
                            "example-label"
                        ],
                        external_references=[
                            {
                                "source_name": "cwe",
                                "url": "http://cwe.mitre.org/data/definitions/117.html",
                                "external_id": "CWE-117"
                            }
                        ],
                        object_marking_refs=[
                            "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9", 
                            "marking-definition--" + str(uuid.uuid5(namespace, f"stix4signalscorps"))
                        ],
                        extensions={
                            "extension-definition--51650285-49b2-50ee-916c-20836485532d": {
                                "extension_type" : "new-sdo"
                            }
                        }
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_WeaknessSDO
}

for directory, weakness_sdo in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([weakness_sdo])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/weakness/weakness--" + str(uuid.uuid5(namespace, f"A demo weakness")) + "/20200101000000000.json", "objects/custom-object-examples/weakness--" + str(uuid.uuid5(namespace, f"A demo weakness")) + ".json")

shutil.rmtree("tmp_object_store")