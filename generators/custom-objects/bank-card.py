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

_type = 'bank-card'
@CustomObservable('bank-card', [
    ('type', TypeProperty(_type, spec_version='2.1')),
    ('spec_version', StringProperty(fixed='2.1')),
    ('id', IDProperty(_type, spec_version='2.1')),
    ('format', StringProperty()),
    ('number', StringProperty(required=True)),
    ('scheme', StringProperty()),
    ('issuer_name', StringProperty()),
    ('issuer_country', StringProperty()),
    ('cardholder_name', StringProperty()),
    ('valid_from', StringProperty()),
    ('valid_to', StringProperty()),
    ('security_code', StringProperty()),
    ('object_marking_refs', ListProperty(ReferenceProperty(valid_types='marking-definition', spec_version='2.1'))),
    ('extensions', ExtensionsProperty(spec_version='2.1'))
])
class BankCard(object):
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

# Create bank-card SCO

### bank-card--d362bd8e-4812-57ab-997b-c888ae23ca26

example_bankCardSCO = BankCard(
                    id="bank-card--"+ str(uuid.uuid5(namespace, f"4242424242424242")),
                    format="credit",
                    number="4242424242424242",
                    scheme="VISA",
                    issuer_name="Big Bank",
                    issuer_country="GBR",
                    cardholder_name="Signals Corps",
                    valid_from="01/99",
                    valid_to="01/00",
                    security_code="999",
                    extensions={
                            "extension-definition--592031e5-2fa4-5f9a-b624-b957d882f6e4": {
                                "extension_type" : "new-sco"
                            }
                        }
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_bankCardSCO
}

for directory, bankcard_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([bankcard_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/bank-card/bank-card--" + str(uuid.uuid5(namespace, f"4242424242424242")) + ".json", "objects/custom-object-examples/bank-card--" + str(uuid.uuid5(namespace, f"4242424242424242")) + ".json")

shutil.rmtree("tmp_object_store")