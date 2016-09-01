import os
import tempfile

import arcpy

from processing import utils
from processing import arcplus


def process(sources):
    """
    Download sources and process the data to the specified output layer.

    :param sources: Source JSON file or directory of files.
    :param output: Output .gdb layer
    """
    os.environ["DOWNLOAD_CACHE"] = "download_cache"

    # create temp wksp
    temp_gdb = os.path.join(tempfile.gettempdir(), "temp_national_parks.gdb")
    arcplus.create_gdb(temp_gdb)

    # load all data sources to temp wksp
    temp_layers = []
    for path in utils.get_files(sources):
        fc_name = os.path.splitext(os.path.split(path)[1])[0]
        source = utils.read_json(path)
        fp = utils.download(source['url'])
        src = utils.extract(fp,
                            source['filetype'],
                            source['file'],
                            source.get("layer", None))
        temp = arcplus.transform_properties(src,
                                            os.path.join(temp_gdb, fc_name),
                                            source['properties'])
        arcpy.RepairGeometry_management(temp)
        temp_layers.append(temp)

    # project inputs to bc albers
    arcplus.project_all(temp_gdb,
                        os.path.join("projections",
                                     "NAD_1983_BC_Environment_Albers.prj"))
    # merge data into single layer
    arcpy.Merge_management(temp_layers,
                           os.path.join(temp_gdb, "national_parks"))
    # repair that geometry too, just in case
    arcpy.RepairGeometry_management(os.path.join(temp_gdb, "national_parks"))


if __name__ == '__main__':
    process("sources")
