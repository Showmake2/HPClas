#!/usr/bin/env python
# coding: utf-8

# In[9]:


import argparse
import warnings

import featureGenerator
import prediction


# In[10]:


if __name__ == "__main__":
    # HPClas

    warnings.filterwarnings("ignore")
    parser = argparse.ArgumentParser(description='generate feature')
    parser.add_argument("--type", required=True,
                        choices=["benchmark", "predict"],
                        help="the encoding type")
    parser.add_argument('--fasta_file', type=str, help='input fasta file')
    parser.add_argument('--output_name', type=str, help='output file name')
    parser.add_argument('--threshold', type=float,help='prediction mode')
    args = parser.parse_args()

    if args.type=="benchmark":
        prediction.prediction()
    else:
        featureGenerator.generator(fasta_file=args.fasta_file, output_name=args.output_name)
        prediction.prediction(output_name=args.output_name,threshold=args.threshold)


# In[ ]:




