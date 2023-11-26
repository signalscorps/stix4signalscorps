# stix4signalscorps (Signals Corps STIX 2.1 Objects)

This repository holds generic STIX 2.1 Objects that are imported to different Signals Corps products.

## Code generator

The python scripts found in `generators/` is what are used to generate the STIX objects in this repository.

If you just want to grab a copy of the unmodified STIX objects, this is not required.

If you do want to modify them, install it as follows;

```shell
# clone the latest code
git clone https://github.com/signalscorps/stix4signalscorps
# create a venv
cd stix4signalscorps
python3 -m venv stix4signalscorps-venv
source stix4signalscorps-venv/bin/activate
# install requirements
pip3 install -r requirements.txt
```

Make your modifications.

And then run each of the scripts as required. Or run them all;

```shell
rm -rf objects && \
python3 generators/identity.py && \
python3 generators/marking-definition.py && \
python3 generators/extension-definition.py && \
python3 generators/custom-objects/weakness.py && \
python3 generators/custom-objects/bank-account.py && \
python3 generators/custom-objects/bank-card.py && \
python3 generators/custom-objects/cryptocurrency-transaction.py && \
python3 generators/custom-objects/cryptocurrency-wallet.py && \
python3 generators/custom-objects/phone-number.py && \
python3 generators/custom-objects/user-agent.py
```

## Support

[Minimal support provided via Slack in the #support-oss channel](https://join.slack.com/t/signalscorps-public/shared_invite/zt-1exnc12ww-9RKR6aMgO57GmHcl156DAA).

## License

[Apache 2.0](/LICENSE).

## Useful supporting tools

* Existing STIX 2.1 schemas: [cti-stix2-json-schemas](https://github.com/oasis-open/cti-stix2-json-schemas): OASIS TC Open Repository: Non-normative schemas and examples for STIX 2
* To generate STIX 2.1 extensions: [stix2 Python Lib](https://stix2.readthedocs.io/en/latest/)
* STIX 2.1 specifications for objects: [STIX 2.1 docs](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html)