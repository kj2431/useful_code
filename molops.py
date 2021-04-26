from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem.rdchem import Mol
from rdkit import rdBase
rdBase.DisableLog('rdApp.error')
rdBase.DisableLog('rdApp.info')  

import numpy as np
import pandas as pd


def canonical_smiles(smiles):
    """
    """
    return Chem.MolToSmiles(Chem.MolFromSmiles(smiles))

def murcko_scaffold(smiles):
    """
    """
    return Chem.Scaffolds.MurckoScaffold.MurckoScaffoldSmilesFromSmiles(smiles, includeChirality=False)


def morgan_fingerprints_array(smiles):
    """
    """
    return np.array(AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(s), 2))
