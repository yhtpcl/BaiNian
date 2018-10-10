import yaml
import os
class ReadYaml():
    def __init__(self,filename):
        self.filepath=os.getcwd()+os.sep+"Data"+os.sep+filename
    def base_read_yaml(self):
        with open(self.filepath,"r",encoding="utf-8") as f:
            return yaml.load(f)
    def base_readyaml(self):
        with open("../Data/login.yaml","r",encoding="utf-8") as f:
            return yaml.load(f)
if __name__ == '__main__':
    datas=ReadYaml("login.yaml").base_readyaml()
    arrs=[]
    for data in datas.values():
        arrs.append((data.get("username"),data.get("password"),data.get("expect"),data.get("toast_expect")))

    print(arrs)