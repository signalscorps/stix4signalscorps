import uuid
import stix2
import os
import shutil
import json

from stix2 import Bundle
from stix2.base import STIXJSONEncoder
from stix2 import ExtensionDefinition
from stix2 import FileSystemStore
from uuid import UUID

# create the directories

tmp_directories = [
    "tmp_object_store/extension-definition/new-sdo/weakness",
    "tmp_object_store/extension-definition/new-sco/bank-account",
    "tmp_object_store/extension-definition/new-sco/bank-card",
    "tmp_object_store/extension-definition/new-sco/cryptocurrency-transaction",
    "tmp_object_store/extension-definition/new-sco/cryptocurrency-wallet",
    "tmp_object_store/extension-definition/new-sco/phone-number",
    "tmp_object_store/extension-definition/new-sco/user-agent"
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
modified="2020-01-01T00:00:00.000Z"
schema_base="https://raw.githubusercontent.com/signalscorps/stix4signalscorps/main/objects/extension-definition/schemas"

### mitre TLP:WHITE and stix4signalscorps

object_marking_refs=[
    "marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9", 
    "marking-definition--" + str(uuid.uuid5(namespace, f"stix4signalscorps"))
]

# Create New Extension Defintion SMO
## https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.common.html

### Weakness SMO

#### extension-definition--51650285-49b2-50ee-916c-20836485532d

weakness_ExtensionDefinitionSMO = ExtensionDefinition(
                        id="extension-definition--" + str(uuid.uuid5(namespace, f"weakness")),
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="Weakness",
                        description="This extension creates a new SDO that can be used to represent weaknesses (for CWEs).",
                        schema=schema_base+"/extension-definition--" + str(uuid.uuid5(namespace, f"weakness")) + ".schema",
                        version="1.0",
                        extension_types=[
                            "new-sdo"
                        ],
                        object_marking_refs=object_marking_refs
                    )

### Bank Account SMO

#### extension-definition--33917e06-c460-5081-8e31-8abb56d90759

bank_account_ExtensionDefinitionSMO = ExtensionDefinition(
                        id="extension-definition--" + str(uuid.uuid5(namespace, f"bank-account")),
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="Bank Account",
                        description="This extension creates a new SCO that can be used to represent bank account details.",
                        schema=schema_base+"/extension-definition--" + str(uuid.uuid5(namespace, f"bank-account")) + ".schema",
                        version="1.0",
                        extension_types=[
                            "new-sco"
                        ],
                        object_marking_refs=object_marking_refs
                    )

### Bank Card SMO

#### extension-definition--592031e5-2fa4-5f9a-b624-b957d882f6e4

bank_card_ExtensionDefinitionSMO = ExtensionDefinition(
                        id="extension-definition--" + str(uuid.uuid5(namespace, f"bank-card")),
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="Bank Card",
                        description="This extension creates a new SCO that can be used to represent bank cards.",
                        schema=schema_base+"/extension-definition--" + str(uuid.uuid5(namespace, f"bank-card")) + ".schema",
                        version="1.0",
                        extension_types=[
                            "new-sco"
                        ],
                        object_marking_refs=object_marking_refs
                    )

### Cryptocurrency Transaction SMO

#### extension-definition--c54209ea-f533-5cf0-af31-a47da6db091b

cryptocurrency_transaction_ExtensionDefinitionSMO = ExtensionDefinition(
                        id="extension-definition--" + str(uuid.uuid5(namespace, f"cryptocurrency-transaction")),
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="Cryptocurrency Transaction",
                        description="This extension creates a new SCO that can be used to represent cryptocurrency transactions.",
                        schema=schema_base+"/extension-definition--" + str(uuid.uuid5(namespace, f"cryptocurrency-transaction")) + ".schema",
                        version="1.0",
                        extension_types=[
                            "new-sco"
                        ],
                        object_marking_refs=object_marking_refs
                    )

### Cryptocurrency Wallet SMO

#### extension-definition--1b6c4ed8-bf57-5f01-bbf2-2ca2c2822567

cryptocurrency_wallet_ExtensionDefinitionSMO = ExtensionDefinition(
                        id="extension-definition--" + str(uuid.uuid5(namespace, f"cryptocurrency-wallet")),
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="Cryptocurrency Wallet",
                        description="This extension creates a new SCO that can be used to represent cryptocurrency wallets.",
                        schema=schema_base+"/extension-definition--" + str(uuid.uuid5(namespace, f"cryptocurrency-wallet")) + ".schema",
                        version="1.0",
                        extension_types=[
                            "new-sco"
                        ],
                        object_marking_refs=object_marking_refs
                    )

### Phone number SMO

#### extension-definition--39bed241-8484-5211-b93c-16ccc20f588e

phone_number_ExtensionDefinitionSMO = ExtensionDefinition(
                        id="extension-definition--" + str(uuid.uuid5(namespace, f"phone-number")),
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="Phone Number",
                        description="This extension creates a new SCO that can be used to represent phone numbers.",
                        schema=schema_base+"/extension-definition--" + str(uuid.uuid5(namespace, f"phone-number")) + ".schema",
                        version="1.0",
                        extension_types=[
                            "new-sco"
                        ],
                        object_marking_refs=object_marking_refs
                    )

### User Agent SMO

#### extension-definition--dc7cf6f0-f39f-5895-9f8b-9a111874b1fe

user_agent_ExtensionDefinitionSMO = ExtensionDefinition(
                        id="extension-definition--" + str(uuid.uuid5(namespace, f"user-agent")),
                        created_by_ref=created_by_ref,
                        created=created,
                        modified=modified,
                        name="User Agent",
                        description="This extension creates a new SCO that can be used to represent user agents used in HTTP request. It is designed to be used when the Network Traffic SCO with HTTP request extension cannot be used due to lack of request information needed for the required properties.",
                        schema=schema_base+"/extension-definition--" + str(uuid.uuid5(namespace, f"user-agent")) + ".schema",
                        version="1.0",
                        extension_types=[
                            "new-sco"
                        ],
                        object_marking_refs=object_marking_refs
                    )

object_list = weakness_ExtensionDefinitionSMO, bank_account_ExtensionDefinitionSMO, bank_card_ExtensionDefinitionSMO, cryptocurrency_transaction_ExtensionDefinitionSMO, cryptocurrency_wallet_ExtensionDefinitionSMO, phone_number_ExtensionDefinitionSMO, user_agent_ExtensionDefinitionSMO

BundleofAllObjects = Bundle(
                        id="bundle--" + str(uuid.uuid5(namespace, f"extension-definition-bundle")),
                        objects=object_list,
                        allow_custom=True
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding IdentitySDO for each directory

fs_directories = {
    "tmp_object_store/extension-definition/new-sdo/weakness": weakness_ExtensionDefinitionSMO,
    "tmp_object_store/extension-definition/new-sco/bank-account": bank_account_ExtensionDefinitionSMO,
    "tmp_object_store/extension-definition/new-sco/bank-card": bank_card_ExtensionDefinitionSMO,
    "tmp_object_store/extension-definition/new-sco/cryptocurrency-transaction": cryptocurrency_transaction_ExtensionDefinitionSMO,
    "tmp_object_store/extension-definition/new-sco/cryptocurrency-wallet": cryptocurrency_wallet_ExtensionDefinitionSMO,
    "tmp_object_store/extension-definition/new-sco/phone-number": phone_number_ExtensionDefinitionSMO,
    "tmp_object_store/extension-definition/new-sco/user-agent": user_agent_ExtensionDefinitionSMO
}

for directory, extensiondefinition_smo in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([extensiondefinition_smo])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/extension-definition"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/extension-definition/new-sdo/weakness/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"weakness")) + "/20200101000000000.json", "objects/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"weakness")) + ".json")

shutil.move("tmp_object_store/extension-definition/new-sco/bank-account/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"bank-account")) + "/20200101000000000.json", "objects/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"bank-account")) + ".json")

shutil.move("tmp_object_store/extension-definition/new-sco/bank-card/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"bank-card")) + "/20200101000000000.json", "objects/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"bank-card")) + ".json")

shutil.move("tmp_object_store/extension-definition/new-sco/cryptocurrency-transaction/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"cryptocurrency-transaction")) + "/20200101000000000.json", "objects/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"cryptocurrency-transaction")) + ".json")

shutil.move("tmp_object_store/extension-definition/new-sco/cryptocurrency-wallet/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"cryptocurrency-wallet")) + "/20200101000000000.json", "objects/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"cryptocurrency-wallet")) + ".json")

shutil.move("tmp_object_store/extension-definition/new-sco/phone-number/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"phone-number")) + "/20200101000000000.json", "objects/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"phone-number")) + ".json")

shutil.move("tmp_object_store/extension-definition/new-sco/user-agent/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"user-agent")) + "/20200101000000000.json", "objects/extension-definition/extension-definition--" + str(uuid.uuid5(namespace, f"user-agent")) + ".json")

shutil.rmtree("tmp_object_store")

## Print the bundle

print(BundleofAllObjects.serialize(pretty=True))