import uuid
import stix2
import os
import shutil

from stix2 import Identity
from stix2 import FileSystemStore
from uuid import UUID

# create the directories

tmp_directories = [
    "tmp_object_store/identity/cpe2stix",
    "tmp_object_store/identity/cti2arango",
    "tmp_object_store/identity/cve2stix",
    "tmp_object_store/identity/cwe2stix",
    "tmp_object_store/identity/disarm2stix",
    "tmp_object_store/identity/sigma2stix",
    "tmp_object_store/identity/signalscorps",
    "tmp_object_store/identity/signalscorps_demo",
    "tmp_object_store/identity/stix2arango",
   	"tmp_object_store/identity/txt2stix"
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
identity_class="system"
contact_information="https://www.signalscorps.com/contact/"
sectors=[
	"technology"
]

### mitre TLP:WHITE and stix4signalscorps

object_marking_refs=[
	"marking-definition--613f2e26-407d-48c7-9eca-b8e91df99dc9", 
	"marking-definition--" + str(uuid.uuid5(namespace, f"stix4signalscorps"))
]

github_link="https://github.com/signalscorps/"

# Create Identity SDOs
## https://stix2.readthedocs.io/en/latest/api/v21/stix2.v21.sdo.html

### cpe2stix

#### identity--de23ef3b-83bf-56a9-95c3-46bc1703966c

cpe2stix_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"cpe2stix")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="cpe2stix",
                        description=github_link+"cpe2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### cti2arango

#### identity--640fae1c-8fa5-5e9c-9809-6883c238fc24

cti2arango_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"cti2arango")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="cti2arango",
                        description=github_link+"cti2arango",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### cve2stix

#### identity--162e1800-92bd-573c-abbd-f359594ffad9

cve2stix_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"cve2stix")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="cve2stix",
                        description=github_link+"cve2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### cwe2stix

#### identity--762246cb-c8a1-53a7-94b3-eafe3ed511c9

cwe2stix_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"cwe2stix")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="cwe2stix",
                        description=github_link+"cwe2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### disarm2stix

#### identity--e9988722-c396-5a91-a08d-db742bd3624b

disarm2stix_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"disarm2stix")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="disarm2stix",
                        description=github_link+"disarm2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### sigma2stix

#### identity--efccc0ba-d237-5c9a-ad41-4f8bb6791be4

sigma2stix_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"sigma2stix")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="sigma2stix",
                        description=github_link+"sigma2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### signals corps

#### identity--aae8eb2d-ea6c-56d6-a606-cc9f755e2dd3

signalscorps_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"signalscorps")),
						created=created,
						modified=modified,
                    	name="signalscorps",
                        description=github_link,
                        contact_information= contact_information,
                        identity_class="organization",
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### signals corps demos

#### identity--d2916708-57b9-5636-8689-62f049e9f727

signalscorps_demo_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"signalscorps-demo")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="signalscorps-demo",
                        description=github_link,
                        contact_information= contact_information,
                        identity_class="organization",
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### stix2arango

#### identity--c54d8eea-d241-5a83-8bf1-619f215ce10b

stix2arango_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"stix2arango")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="stix2arango",
                        description=github_link+"stix2arango",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

### txt2stix

#### identity--9c259ff7-f413-5001-9911-70b4352af93f

txt2stix_IdentitySDO = Identity(
						id="identity--" + str(uuid.uuid5(namespace, f"txt2stix")),
						created_by_ref=created_by_ref,
						created=created,
						modified=modified,
                    	name="txt2stix",
                        description=github_link+"txt2stix",
                        contact_information= contact_information,
                        identity_class=identity_class,
                        sectors=sectors,
						object_marking_refs=object_marking_refs
                    )

# Write the objects to the filestore
## https://stix2.readthedocs.io/en/latest/guide/filesystem.html#FileSystemSource

### Creating FileSystemStore and adding IdentitySDO for each directory

fs_directories = {
    "tmp_object_store/identity/cpe2stix": cpe2stix_IdentitySDO,
    "tmp_object_store/identity/cti2arango": cti2arango_IdentitySDO,
    "tmp_object_store/identity/cve2stix": cve2stix_IdentitySDO,
    "tmp_object_store/identity/cwe2stix": cwe2stix_IdentitySDO,
    "tmp_object_store/identity/disarm2stix": disarm2stix_IdentitySDO,
    "tmp_object_store/identity/sigma2stix": sigma2stix_IdentitySDO,
    "tmp_object_store/identity/signalscorps": signalscorps_IdentitySDO,
    "tmp_object_store/identity/signalscorps_demo": signalscorps_demo_IdentitySDO,
    "tmp_object_store/identity/stix2arango": stix2arango_IdentitySDO,
    "tmp_object_store/identity/txt2stix": txt2stix_IdentitySDO
}

for directory, identity_sdo in fs_directories.items():
    fs_store = stix2.FileSystemStore(directory)
    fs_store.add([identity_sdo])

# Now move those files into the standardised locations for easy download

final_directories = [
    "objects/identity"
]

for directory in final_directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

shutil.move("tmp_object_store/identity/cpe2stix/identity/identity--" + str(uuid.uuid5(namespace, f"cpe2stix")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"cpe2stix")) + ".json")

shutil.move("tmp_object_store/identity/cti2arango/identity/identity--" + str(uuid.uuid5(namespace, f"cti2arango")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"cti2arango")) + ".json")

shutil.move("tmp_object_store/identity/cve2stix/identity/identity--" + str(uuid.uuid5(namespace, f"cve2stix")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"cve2stix")) + ".json")

shutil.move("tmp_object_store/identity/cwe2stix/identity/identity--" + str(uuid.uuid5(namespace, f"cwe2stix")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"cwe2stix")) + ".json")

shutil.move("tmp_object_store/identity/disarm2stix/identity/identity--" + str(uuid.uuid5(namespace, f"disarm2stix")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"disarm2stix")) + ".json")

shutil.move("tmp_object_store/identity/sigma2stix/identity/identity--" + str(uuid.uuid5(namespace, f"sigma2stix")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"sigma2stix")) + ".json")

shutil.move("tmp_object_store/identity/signalscorps/identity/identity--" + str(uuid.uuid5(namespace, f"signalscorps")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"signalscorps")) + ".json")

shutil.move("tmp_object_store/identity/signalscorps_demo/identity/identity--" + str(uuid.uuid5(namespace, f"signalscorps-demo")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"signalscorps-demo")) + ".json")

shutil.move("tmp_object_store/identity/stix2arango/identity/identity--" + str(uuid.uuid5(namespace, f"stix2arango")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"stix2arango")) + ".json")

shutil.move("tmp_object_store/identity/txt2stix/identity/identity--" + str(uuid.uuid5(namespace, f"txt2stix")) + "/20200101000000000.json", "objects/identity/identity--" + str(uuid.uuid5(namespace, f"txt2stix")) + ".json")

shutil.rmtree("tmp_object_store")