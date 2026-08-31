import pickle

x, y, z = 1, 2, 3
s = "FishC"
l = ["小甲鱼", 520, 3.14]
d = {"one":1, "two":2}

with open("data.pkl", "wb") as f:
    pickle.dump((x, y, z, s, l, d), f)
