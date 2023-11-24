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

_type = 'cryptocurrency-transaction'
@CustomObservable('cryptocurrency-transaction', [
    ('type', TypeProperty(_type, spec_version='2.1')),
    ('spec_version', StringProperty(fixed='2.1')),
    ('id', IDProperty(_type, spec_version='2.1')),
    ('symbol', StringProperty(required=True)),
    ('hash', StringProperty(required=True)),
    ('block_id', StringProperty()),
    ('fee', StringProperty()),
    ('execution_time', TimestampProperty()),
    ('input', ListProperty(StringProperty())),
    ('output', ListProperty(StringProperty())),
    ('object_marking_refs', ListProperty(ReferenceProperty(valid_types='marking-definition', spec_version='2.1'))),
    ('extensions', ExtensionsProperty(spec_version='2.1'))
])
class CryptocurrencyTransaction(object):
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

# Create CryptocurrencyTransaction SCO

example_CryptocurrencyTransactionSCO = CryptocurrencyTransaction(
                    id="cryptocurrency-transaction--"+ str(uuid.uuid5(namespace, f"3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5")),
                    symbol="BTC",
                    hash="3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5",
                    block_id="590001",
                    fee="0.00000728",
                    execution_time="2022-10-02T15:22:21Z",
                    input=[
                        {
                            "address_ref": "cryptocurrency-wallet--b1bc02bd-f10d-40e4-86d1-9e2ef3aa919f",
                            "amount": 0.84000000
                        }
                    ],
                    output=[
                        {
                            "address_ref": "cryptocurrency-wallet--3a3d6fb5-9eb1-499f-b2f6-3aae6b498f63",
                            "amount": 0.80000000
                        },
                        {
                            "address_ref": "cryptocurrency-wallet--4d18102a-f35a-4176-9509-f96a3370d067",
                            "amount": 0.04000000
                        }
                    ],
                    extensions={
                            "extension-definition--c54209ea-f533-5cf0-af31-a47da6db091b": {
                                "extension_type" : "new-sco"
                            }
                        }
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding MarkingDefinitionSMO for each directory

fs_directories = {
    "tmp_object_store": example_CryptocurrencyTransactionSCO
}

for directory, cryptocurrency_transaction_sco in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([cryptocurrency_transaction_sco])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/custom-object-examples"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/cryptocurrency-transaction/cryptocurrency-transaction--" + str(uuid.uuid5(namespace, f"3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5")) + ".json", "objects/custom-object-examples/cryptocurrency-transaction--" + str(uuid.uuid5(namespace, f"3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5")) + ".json")

shutil.rmtree("tmp_object_store")