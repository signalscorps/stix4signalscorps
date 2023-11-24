import uuid
import stix2
import os
import shutil

from stix2 import CustomObservable
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

_type = 'phone-number'
@CustomObservable('phone-number', [
    ('type', TypeProperty(_type, spec_version='2.1')),
    ('spec_version', StringProperty(fixed='2.1')),
    ('id', IDProperty(_type, spec_version='2.1')),
    ('number', StringProperty(required=True)),
    ('country_code', StringProperty()),
    ('connection', StringProperty()),
    ('provider', StringProperty()),
    ('object_marking_refs', ListProperty(ReferenceProperty(valid_types='marking-definition', spec_version='2.1'))),
    ('extensions', ExtensionsProperty(spec_version='2.1'))
])
class PhoneNumber(object):
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

# Create PhoneNumber SCO

example_PhoneNumberSCO = PhoneNumber(
                    id="phone-number--"+ str(uuid.uuid5(namespace, f"07890129093")),
                    number="07890129093",
                    country_code="44",
                    connection="Mobile",
                    provider="Big Network",
                    extensions={
                            "extension-definition--39bed241-8484-5211-b93c-16ccc20f588e": {
                                "extension_type" : "new-sco"
                            }
                        }
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_PhoneNumberSCO
}

for directory, phone_number_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([phone_number_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/phone-number/phone-number--" + str(uuid.uuid5(namespace, f"07890129093")) + ".json", "objects/custom-object-examples/phone-number--" + str(uuid.uuid5(namespace, f"07890129093")) + ".json")

shutil.rmtree("tmp_object_store")