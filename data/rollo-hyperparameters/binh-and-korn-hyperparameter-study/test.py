import numpy as np
import subprocess 
from jinja2 import Template 
import json

muts = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
cx = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for c in cx:
    with open("input_test_binh.json") as f:
        template = Template(f.read())
    input_file = template.render(cx_pb=str(c))
    with open('input_test_binh_gen.json', 'w') as f:
        json.dump(json.loads(input_file), f)
    subprocess.call("python ../../../rollo/ -i input_test_binh_gen.json", shell=True)
    subprocess.call("mv ./checkpoint.pkl checkpoint_120_5_cxpb_"+str(c)+".pkl", shell=True)

for i in range(1, 26):
    subprocess.call("python ../../../rollo/ -i input_test_binh.json", shell=True)
    subprocess.call("mv ./checkpoint.pkl checkpoint_120_5_cxpb_0.90_mutpb_0.3_"+str(i)+".pkl", shell=True)
