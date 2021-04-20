from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from rdkit.Chem.rdchem import Mol
from rdkit import rdBase
rdBase.DisableLog('rdApp.error')
rdBase.DisableLog('rdApp.info')  

import networkx as nx

import numpy as np
import pandas as pd

'''
=======================================================================================================================
Source:
https://github.com/dakoner/keras-molecules/blob/dbbb790e74e406faa70b13e8be8104d9e938eba2/convert_rdkit_to_networkx.py
'''
def mol_to_nx(smiles, addHs=False, explicitOnly=False):
    
    if type(smiles) is Chem.rdchem.Mol:
        mol = smiles
    else:
        mol = Chem.MolFromSmiles(smiles)
        
    if (addHs is True) and (explicitOnly is True):
        mol = Chem.RWMol(Chem.AddHs(mol), explicitOnly=True)
    elif (addHs is True) and (explicitOnly is False):
        mol = Chem.RWMol(Chem.AddHs(mol))
        
    try:
        Chem.Kekulize(mol, clearAromaticFlags=True)
    except:
        print('Unable to kekulize mol object')

    G = nx.Graph()


    for atom in mol.GetAtoms():
        G.add_node(atom.GetIdx(),
                   atomic_num=atom.GetAtomicNum(),
                   formal_charge=atom.GetFormalCharge(),
                   isotope = atom.GetIsotope(),
                   hybridization=atom.GetHybridization(),
                   num_explicit_hs=atom.GetNumExplicitHs())
        
    for bond in mol.GetBonds():
        G.add_edge(bond.GetBeginAtomIdx(),
                   bond.GetEndAtomIdx(),
                   bond_type=bond.GetBondType())
    return G

def nx_to_mol(G, Gin=None, atomic_nums=None, formal_charges=None, node_hybridizations=None, num_explicit_hss=None, isotopes=None):
    
    #G is subgraph
    #Gin is original graph
    
    mol = Chem.RWMol()
    
    #assume subgraph and graph are same if Gin is None
    if Gin is None:
        Gin = G
    
    #get arguments from graph if not passed from outside function
    if atomic_nums is None:
        atomic_nums = nx.get_node_attributes(Gin, 'atomic_num')
        
    if formal_charges is None:
        formal_charges = nx.get_node_attributes(Gin, 'formal_charge')
    
    if isotopes is None:
        isotopes = nx.get_node_attributes(Gin, 'isotope')

    if node_hybridizations is None:
        node_hybridizations = nx.get_node_attributes(Gin, 'hybridization')
    
    if num_explicit_hss is None:
        num_explicit_hss = nx.get_node_attributes(Gin, 'num_explicit_hs')
    node_to_idx = {}
    
    for node in G.nodes():
        a=Chem.Atom(atomic_nums[node])
        a.SetIsotope(isotopes[node])
        #hardcode to prevent bugs
        a.SetChiralTag(Chem.rdchem.ChiralType.CHI_UNSPECIFIED)
        a.SetIsAromatic(False)
        
        a.SetFormalCharge(formal_charges[node])
        a.SetHybridization(node_hybridizations[node])
        a.SetNumExplicitHs(num_explicit_hss[node])
        idx = mol.AddAtom(a)
        node_to_idx[node] = idx

    bond_types = nx.get_edge_attributes(G, 'bond_type')
    for edge in G.edges():
        first, second = edge
        ifirst = node_to_idx[first]
        isecond = node_to_idx[second]
        bond_type = bond_types[first, second]
        mol.AddBond(ifirst, isecond, bond_type)

    Chem.SanitizeMol(mol)
    return mol
