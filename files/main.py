
with open("input/letter_template") as data:
    content = data.read()
    data.close()

with open("input/names") as name:
    nam = name.readlines()
    name.close()
updated = []
for i in nam:
    up = content.replace("name",i.strip())
    with open(f"letters/{i.strip()}_letter", 'w') as f:
        f.write(up)

