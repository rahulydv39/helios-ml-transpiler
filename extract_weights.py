import re
import json

# read model.c
with open("model2.c", "r") as f:
    code = f.read()


def extract_array(name):

    pattern = rf"const float {name}\[\]\s*=\s*\{{(.*?)\}};"
    match = re.search(pattern, code, re.S)

    if not match:
        raise ValueError(f"{name} not found")

    nums = match.group(1)

    # remove newlines and C float suffix
    nums = nums.replace("\n", " ").replace("f", "")

    nums = nums.split(",")

    values = [float(n.strip()) for n in nums if n.strip() != ""]

    return values


# extract arrays
W1 = extract_array("W1")
B1 = extract_array("B1")
W2 = extract_array("W2")
B2 = extract_array("B2")
W3 = extract_array("W3")
B3 = extract_array("B3")

# flatten same order as original exporter
weights = []
weights.extend(W1)
weights.extend(B1)
weights.extend(W2)
weights.extend(B2)
weights.extend(W3)
weights.extend(B3)

data = {
    "architecture": [2,16,16,2],
    "weights": weights
}

# write JSON
with open("model_weights2.json", "w") as f:
    json.dump(data, f, separators=(',',':'))

print("JSON regenerated successfully")
print("Total parameters:", len(weights))