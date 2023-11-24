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

_type = 'user-agent'
@CustomObservable('user-agent', [
    ('type', TypeProperty(_type, spec_version='2.1')),
    ('spec_version', StringProperty(fixed='2.1')),
    ('id', IDProperty(_type, spec_version='2.1')),
    ('string', StringProperty(required=True)),
    ('object_marking_refs', ListProperty(ReferenceProperty(valid_types='marking-definition', spec_version='2.1'))),
    ('extensions', ExtensionsProperty(spec_version='2.1'))
])
class UserAgent(object):
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

# Create UserAgent SCO

example_UserAgentSCO = UserAgent(
                    id="user-agent--"+ str(uuid.uuid5(namespace, f"Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")),
                    string="Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                    extensions={
                            "extension-definition--dc7cf6f0-f39f-5895-9f8b-9a111874b1fe": {
                                "extension_type" : "new-sco"
                            }
                        }
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_UserAgentSCO
}

for directory, useragent_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([useragent_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/user-agent/user-agent--" + str(uuid.uuid5(namespace, f"Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")) + ".json", "objects/custom-object-examples/user-agent--" + str(uuid.uuid5(namespace, f"Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")) + ".json")

shutil.rmtree("tmp_object_store")