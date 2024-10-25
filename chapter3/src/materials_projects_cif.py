import pandas as pd
from tqdm import tqdm

from mp_api.client import MPRester

# あなたのMaterials ProjectのAPIキーをここに入力してください
YOUR_API_KEY = "RnqyA0tiXmBuAFbMEAIJM2n5AUaX8ZP7"

mpr = MPRester(YOUR_API_KEY)

df_cif = pd.read_csv("/workdir/practical-mi-guide/chapter3/input/material_projects_api_cif.csv")
extracted_ids = df_cif["id"].values
print(len(extracted_ids))
formulas = df_cif["formula"].values
print(len(formulas))

import os

# mids=mpr.materials.search(material_ids= material_id_list[0], fields=["structure"])

output_dir = "/workdir/practical-mi-guide/chapter3/input/material_projects_api_cif"

for i in tqdm(range(len(df_cif))):
    material_id_list_tmp = extracted_ids[i]
    formulas_tmp = formulas[i]
    search_results = mpr.materials.search(material_ids=material_id_list_tmp, fields=["structure"])
    
    # search_results はリストと仮定しています。
    # もし検索結果がリストでない場合、この部分を適切に修正する必要があります。
    for result in search_results:
        structure = result.structure
        filename = f"/workdir/practical-mi-guide/chapter3/input/material_projects_api_cif/cif_{material_id_list_tmp}_{formulas_tmp}.cif"
        structure.to(filename=filename, fmt='cif')