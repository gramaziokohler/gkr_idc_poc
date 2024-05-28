# Getting started

## installing the cadwork plugin

1. Create a new virtual environment called `SWaaEditor` in the cadwork plugin directory:
```bash
PLIGIN_DIR=C:\Users\Public\Documents\cadwork\userprofil_30\3d\API.x64\

> cd $PLUGIN_DIR
> virtualenv SWaaEditorIDC
> cd SWaaEditorIDC
```

2. Copy the contents of the `SWaaEditor` directory from this repository, along with the `requirements.txt` file to the newly created plugin folder.

3. Activate new virtual environment and install COMPAS dependencies:
```bash
> Scripts\activate
> (SWaaEditor) pip install -r requirements.txt
```

4. Open cadwork, a new user plugin called SWaaEditor should appear.