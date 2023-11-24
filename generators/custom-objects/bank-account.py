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

_type = 'bank-account'
@CustomObservable('bank-account', [
    ('type', TypeProperty(_type, spec_version='2.1')),
    ('spec_version', StringProperty(fixed='2.1')),
    ('id', IDProperty(_type, spec_version='2.1')),
    ('bank', StringProperty(required=True)),
    ('country', StringProperty()),
    ('currency', StringProperty()),
    ('owner_name', StringProperty()),
    ('iban_number', StringProperty()),
    ('swift_code', StringProperty()),
    ('object_marking_refs', ListProperty(ReferenceProperty(valid_types='marking-definition', spec_version='2.1'))),
    ('extensions', ExtensionsProperty(spec_version='2.1'))
])
class BankAccount(object):
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

# Create bank account SCO

### bank-account--0108d286-e7c6-523f-b5c6-e974d16334df

example_bankAccountSCO = BankAccount(
                    id="bank-account--"+ str(uuid.uuid5(namespace, f"GB33BUKB20201555555555")),
                    bank="Big Bank",
                    country="GBR",
                    currency="GBP",
                    owner_name="A customer",
                    iban_number="GB33BUKB20201555555555",
                    swift_code="DEMOGB22XXX",
                    extensions={
                            "extension-definition--33917e06-c460-5081-8e31-8abb56d90759": {
                                "extension_type" : "new-sco"
                            }
                        }
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_bankAccountSCO
}

for directory, bankaccount_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([bankaccount_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/bank-account/bank-account--" + str(uuid.uuid5(namespace, f"GB33BUKB20201555555555")) + ".json", "objects/custom-object-examples/bank-account--" + str(uuid.uuid5(namespace, f"GB33BUKB20201555555555")) + ".json")

shutil.rmtree("tmp_object_store")