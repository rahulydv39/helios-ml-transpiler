import json

# load JSON
with open("model_weights.json","r") as f:
    data=json.load(f)

layers=data["layers"]

W1=layers[0]["W"]
B1=layers[0]["B"]

W2=layers[1]["W"]
B2=layers[1]["B"]

W3=layers[2]["W"]
B3=layers[2]["B"]


# flatten matrices
def flatten(matrix):
    return [v for row in matrix for v in row]

W1=flatten(W1)
W2=flatten(W2)
W3=flatten(W3)


def c_array(name,arr,cols):

    rows=[]
    for r in range(0,len(arr),cols):
        row=arr[r:r+cols]
        rows.append("    "+", ".join(f"{v:.6f}f" for v in row))

    return f"const float {name}[]={{\n"+",\n".join(rows)+"\n};\n\n"


c=""

c+="#include <stdio.h>\n"
c+="#include <math.h>\n\n"

c+=c_array("W1",W1,16)
c+=c_array("B1",B1,16)

c+=c_array("W2",W2,16)
c+=c_array("B2",B2,16)

c+=c_array("W3",W3,2)
c+=c_array("B3",B3,2)


c+="""
void model_predict(float input[2], float output[2])
{
    float h1[16];
    float h2[16];

    for(int j=0;j<16;j++)
    {
        h1[j]=B1[j];

        for(int i=0;i<2;i++)
        {
            h1[j]+=input[i]*W1[i*16+j];
        }

        h1[j]=tanh(h1[j]);
    }

    for(int j=0;j<16;j++)
    {
        h2[j]=B2[j];

        for(int i=0;i<16;i++)
        {
            h2[j]+=h1[i]*W2[i*16+j];
        }

        h2[j]=tanh(h2[j]);
    }

    for(int j=0;j<2;j++)
    {
        output[j]=B3[j];

        for(int i=0;i<16;i++)
        {
            output[j]+=h2[i]*W3[i*2+j];
        }
    }
}
"""


c+="""
int main()
{
    float input[2]={7.0f,3.0f};

    input[0]/=9.0f;
    input[1]/=9.0f;

    float output[2];

    model_predict(input,output);

    printf("theta1=%f\\n",output[0]);
    printf("theta2=%f\\n",output[1]);
}
"""


with open("model2.c","w") as f:
    f.write(c)

print("model2.c generated successfully")