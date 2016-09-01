# BC National Parks
Combine National Parks in British Columbia into a single layer.

## Requirements

- ArcGIS 
- processing

## Installation
1. Open a windows command prompt and ensure that ArcGIS Python and scripts are inlcuded in the PATH. Use 34 bit Python (so the script is easily runnable from the desktop)  
  ```
  set PATH="E:\sw_nt\Python27\ArcGIS10.3";"E:\sw_nt\Python27\ArcGIS10.3\Scripts";%PATH%
  ```
2. Download and unzip the repository (or `git clone https://github.com/smnorris/national_parks.git` from a command line tool with git installed such as cygwin)


## Usage

To create a new national parks layer based on the existing input source definitions:

**From the command line:**  
`$ python national_parks.py C:\path\to\my_workspace.gdb\national_parks`

**From the ArcGIS toolbox:**  
Open the toolbox and run the script tool.

## Configuration

To modify the input layer sources, edit the inputs definition .json files in the `sources` folder. 

### JSON Tags

Sources use a standard set of attributes to allow for machine processing of
each source. Use these tags where applicable. Check out files in the
`./sources/` directory for examples


 Tag          | Required? | Note
------------- | --------- | ----
`url`         | Yes | A URL referencing the dataset. This should point to the raw data and not a web portal.
`filetype`    | Yes | A string containing the file type (only `shp`, and `gdb` are currently supported)
`attribution` | Yes | A string citing the owner/custodian of the data
`metadata`    | No  | A URL referencing metadata documenting the dataset.
`licence`     | Yes | A URL or string referencing the licence under which the data is published
`properties`  | Yes | An object mapping output property names to input properties. See below.
`query`       | No  | A string containing a valid sql WHERE clause used to filter the records extracted from the source
`crs`         | No  | A string referencing the data's coordinate reference system eg `EPSG:3005` Not required if input data includes a projection definition.

### Properties 

The properties tag/object:

- defines the output attributes/properties
- maps the output properties to the existing input properties
- defines how to process the input properties

Map output properties directly to input properties:
```
   "properties": {
      "ENGLISH_NAME": "NAME_E",
      "FRENCH_NAME": "NAME_F",
      "ABSOLUTE_ACCURACY": "ABS_ACCUR"
   }
```

Map output property to constant values (definition of output ArcGIS type is required):
```
   "properties": {
      "agency": {
        "static": "GeoBC",
        "type": "TEXT"
      },
      "accuracy": {
        "static": "100",
        "type": "INTEGER"
      }
   }
```

See `schemas/source.json` for an exact definition of what properties are allowed.  To validate any changes to the source schemas run the validation script:  
`python validate.py schemas/source.json sources`

## License

    Copyright 2016 Province of British Columbia

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at 

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

