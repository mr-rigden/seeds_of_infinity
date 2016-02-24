import gzip
import io
import json
import os
import time

import generators.creatures
import generators.misc


HOME_PATH = os.path.dirname(os.path.realpath(__file__))
RESOURCES_PATH = os.path.join(HOME_PATH, "resources")
JSON_PATH = os.path.join(RESOURCES_PATH, "json")

def json_formatter(data, title):
    data_dict = {}
    data_dict['meta'] = {}
    data_dict['meta']['author'] = "Jason Rigden"
    data_dict['meta']['generator'] = "https://github.com/jrigden/Seeds_of_Infinity"
    data_dict['meta']['license'] = "http://unlicense.org"
    data_dict['meta']['time_created'] = int(time.time())
    data_dict['meta']['title'] = title
    data_dict['data'] = data
    data_json = json.dumps(data_dict, ensure_ascii=False, indent=4, separators=(',', ': '), sort_keys=True)
    return data_json

def save_json(data, filename, title):
    file_path = os.path.join(JSON_PATH, filename)
    file_gz_path = os.path.join(JSON_PATH, filename + ".gz")
    data_json = json_formatter(data, title)
    with io.open(file_path, 'w', encoding='utf-8') as f:
        f.write(data_json)
    f_in = open(file_path, 'rb')
    f_out = gzip.open(file_gz_path, 'w')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()

def write_creatures_json():
    all_creatures = generators.creatures.get_all_creatures()
    save_json(all_creatures, "all_creatures.json", "all_creatures")

def write_misc_json():
    misc_dict = {}
    misc_dict['alignments'] = generators.misc.get_alignments()
    misc_dict['attributes'] = generators.misc.get_attributes()
    misc_dict['basic_colors'] = generators.misc.get_basic_colors()
    misc_dict['colors'] = generators.misc.get_colors()
    misc_dict['liquid_types'] = generators.misc.get_liquid_types()
    misc_dict['metals'] = generators.misc.get_metals()
    misc_dict['gems'] = generators.misc.get_gems()
    misc_dict['personalities'] = generators.misc.get_personalities()
    misc_dict['smells'] = generators.misc.get_smells()
    misc_dict['stones'] = generators.misc.get_stones()
    misc_dict['traits'] = generators.misc.get_traits()
    save_json(misc_dict, "misc.json", "misc")

if __name__ == "__main__":
    write_creatures_json()
    write_misc_json()
